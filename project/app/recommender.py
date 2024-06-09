import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from sklearn.neighbors import NearestNeighbors
from .models import JobApplication, Job
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .models import JobApplication, Job



def get_user_job_matrix():
    applications = JobApplication.objects.all()
    
    if not applications.exists():
        return None, None  # Return None if there are no job applications

    data = {
        'user': [app.user.id for app in applications],
        'job': [app.job.id for app in applications],
    }

    df = pd.DataFrame(data)
    df['interaction'] = 1  # Create an interaction column

    user_job_matrix = df.pivot(index='user', columns='job', values='interaction').fillna(0)
    return user_job_matrix, df





def get_similar_jobs(user_id, k=5):
    # Check if the user has any job applications
    user_applications = JobApplication.objects.filter(user_id=user_id)
    
    # If the user has no applications, return a default list of recommended jobs
    if not user_applications.exists():
        return Job.objects.all()[:k]
    
    # Get all job applications
    applications = JobApplication.objects.all()

    data = {
        'user': [app.user.id for app in applications],
        'job': [app.job.id for app in applications],
    }

    df = pd.DataFrame(data)
    df['interaction'] = 1  # Create an interaction column

    user_job_matrix = df.pivot(index='user', columns='job', values='interaction').fillna(0)

    # Ensure enough users are present
    n_users = user_job_matrix.shape[0]
    if n_users <= 1:
        return []  # Return an empty list if there are not enough users to make recommendations

    k = min(k, n_users - 1)

    # Check if the user exists in the matrix
    if user_id not in user_job_matrix.index:
        # If the user does not exist, create an empty row for the user
        user_job_matrix.loc[user_id] = 0

    # Fit the NearestNeighbors model
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(user_job_matrix)

    # Find similar users
    user_index = user_job_matrix.index.tolist().index(user_id)
    distances, indices = model.kneighbors([user_job_matrix.iloc[user_index]], n_neighbors=k+1)
    
    similar_users = user_job_matrix.index[indices.flatten()[1:]]  # Exclude the user itself

    # Get jobs liked by similar users
    similar_user_jobs = user_job_matrix.loc[similar_users].sum(axis=0).sort_values(ascending=False)
    
    # Get job IDs
    job_ids = similar_user_jobs.index.tolist()
    
    return Job.objects.filter(id__in=job_ids[:k])










def get_similar_jobs_nlp(user_id, k=10):
    applications = JobApplication.objects.filter(user=user_id)
    
    if not applications.exists():
        return []  # Return an empty list if the user has not applied to any jobs

    # Get job descriptions
    job_descriptions = [app.job.description for app in applications]

    # Vectorize job descriptions
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(job_descriptions)

    # Compute similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Get index of the user's applied jobs
    applied_jobs_index = [app.job.id - 1 for app in applications if app.job.id <= cosine_sim.shape[0]]

    if not applied_jobs_index:
        return []  # Return empty list if there are no valid applied jobs

    # Get similar jobs
    similar_jobs_indices = np.argsort(cosine_sim[applied_jobs_index])[:, ::-1][:, 1:k+1].flatten()

    similar_job_ids = [app.job.id for app in applications]  # Initialize with applied job IDs
    similar_job_ids += [job.id for i, job in enumerate(Job.objects.all()) if i in similar_jobs_indices]

    return Job.objects.filter(id__in=similar_job_ids[:k])




def get_predicted_jobs(user_id, k=10):
 try:
    user_job_matrix, df = get_user_job_matrix()

    if user_job_matrix is None or user_job_matrix.shape[0] < 2:
        print("Not enough data for prediction")
        return []  # Return an empty list if there are no job applications or not enough users

    # Convert the matrix to a DataFrame
    matrix_df = user_job_matrix.reset_index()

    # Prepare the data for training
    X = matrix_df.drop(columns=['user'])
    y = matrix_df['user']

    # Ensure there are enough samples to split
    if X.shape[0] <= 1:
        print("Not enough samples to train the model")
        return []  # Not enough samples to train the model

    # Fit k-nearest neighbors model
    try:
        neigh = NearestNeighbors(n_neighbors=5)
        neigh.fit(X)
    except Exception as e:
        print(f"Error during model fitting: {e}")
        return []  # Return an empty list if there is an error during fitting

    # Get nearest neighbors for the user
    user_vector = user_job_matrix.loc[user_id].values.reshape(1, -1)
    try:
        distances, indices = neigh.kneighbors(user_vector)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return []  # Return an empty list if there is an error during prediction

    # Extract job IDs for the predicted user IDs
    nearest_user_ids = y.iloc[indices[0]].tolist()
    predicted_job_ids = df[df['user'].isin(nearest_user_ids)]['job'].unique()

    return Job.objects.filter(id__in=predicted_job_ids[:k])
 except KeyError:
        #print(f"Error during prediction: {e}")
        return []  # Return an empty list if user_id is not found in user_job_matrix