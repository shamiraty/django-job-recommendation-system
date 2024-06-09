from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Job, JobApplication
from .recommender import get_similar_jobs
from .recommender import get_similar_jobs_nlp

from .recommender import get_similar_jobs, get_predicted_jobs

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

from django.contrib.auth.decorators import login_required

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    similar_jobs = Job.objects.filter(category=job.category).exclude(pk=job_id)[:15]

    # Ensure user ID is available before calling get_predicted_jobs
    if request.user.is_authenticated:
        recommended_jobs = get_similar_jobs(request.user.id)
        predicted_jobs = get_predicted_jobs(request.user.id)
        nlp_similar_jobs = get_similar_jobs_nlp(request.user.id)
    else:
        recommended_jobs = []
        predicted_jobs = []
        nlp_similar_jobs = []

    return render(request, 'job_detail.html', {
        'job': job,
        'similar_jobs': similar_jobs,
        'recommended_jobs': recommended_jobs,
        'predicted_jobs': predicted_jobs,
        'nlp_similar_jobs': nlp_similar_jobs,
    })


from .forms import *
@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_applied.html',{'job':job})



from .forms import CustomUserCreationForm
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



from django.contrib.auth.forms import AuthenticationForm
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout
    template_name = 'logged_out.html'  # Your logged out template

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
