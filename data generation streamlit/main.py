import streamlit as st
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random
st.set_page_config(layout="wide")




# Initialize Faker to generate fake data
fake = Faker('en_US')
st.title('DATA SCIENCE')
st.title("OPEN FAKE DATA GENERATION")


# Academic and technical terms
academic_terms = [
    "Data Analysis", "Programming", "Statistical Modeling", "Machine Learning", "Database Management",
    "Web Development", "Network Security", "Algorithms", "Software Engineering", "Cybersecurity",
    "Finance", "Economics", "Marketing", "Accounting", "Management", "Human Resources", "Public Relations",
    "Environmental Science", "Civil Engineering", "Mechanical Engineering", "Electrical Engineering", "Physics",
    "Biology", "Chemistry", "Medicine", "Psychology", "Sociology", "Education", "Architecture","Artificial Intelligence", "Robotics", "Quantum Computing", "Astrophysics", "Geology",
"Environmental Engineering", "Aerospace Engineering", "Biomedical Engineering", "Nuclear Engineering", "Genetics",
"Microbiology", "Virology", "Immunology", "Neuroscience", "Pharmacology",
"Toxicology", "Biochemistry", "Molecular Biology", "Ecology", "Botany",
"Zoology", "Marine Biology", "Oceanography", "Meteorology", "Climatology",
"Geophysics", "Geochemistry", "Materials Science", "Nanotechnology", "Renewable Energy",
"Bioinformatics", "Computational Biology", "Theoretical Physics", "Particle Physics", "Condensed Matter Physics",
"Optics", "Plasma Physics", "Mathematics", "Applied Mathematics", "Statistics",
"Operations Research", "Data Science", "Information Technology", "Computer Science", "Computer Engineering",
"Embedded Systems", "Telecommunications", "Signal Processing", "Image Processing", "Pattern Recognition",
"Control Systems", "Manufacturing Engineering", "Industrial Engineering", "Systems Engineering", "Engineering Management",
"Supply Chain Management", "Logistics", "Project Management", "Operations Management", "Strategic Management",
"International Business", "Entrepreneurship", "Business Analytics", "E-commerce", "Digital Marketing",
"Consumer Behavior", "Brand Management", "Advertising", "Sales Management", "Public Administration",
"Political Science", "International Relations", "Law", "Criminology", "Forensic Science",
"Anthropology", "Archaeology", "Linguistics", "Literature", "Philosophy",
"History", "Religious Studies", "Cultural Studies", "Gender Studies", "Media Studies",
"Film Studies", "Art History", "Visual Arts", "Performing Arts", "Music",
"Theater", "Dance", "Creative Writing", "Journalism", "Communications",
"Library Science", "Museum Studies", "Urban Planning", "Real Estate", "Tourism",
"Hospitality Management", "Culinary Arts", "Event Management", "Sports Management", "Kinesiology",
]

technical_terms = [
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML/CSS", "Linux", "Git", "AWS", "TensorFlow",
    "Excel", "PowerBI", "Tableau", "Google Cloud", "Docker", "Kubernetes", "React", "Vue.js", "Angular",
    "Cybersecurity", "Network Administration", "Ethical Hacking", "Robotics", "IoT", "CAD/CAM", "MATLAB","R", "PHP", "Ruby", "Swift", "Objective-C", "Go", "Perl", "Scala", "Kotlin", "Django",
"Flask", "Spring", "Hibernate", "ASP.NET", "jQuery", "Node.js", "Express.js", "Bootstrap", "SASS", "Less",
"TypeScript", "C#", "Bash", "PowerShell", "Ansible", "Puppet", "Chef", "Terraform", "OpenStack", "Jenkins",
"Travis CI", "CircleCI", "GitLab CI", "Nagios", "Prometheus", "Grafana", "Splunk", "Elasticsearch", "Logstash", "Kibana",
"Redis", "MongoDB", "Cassandra", "CouchDB", "PostgreSQL", "SQLite", "MariaDB", "Oracle Database", "Firebase", "GraphQL",
"Apache Hadoop", "Apache Spark", "Apache Kafka", "Apache Hive", "Apache Pig", "Presto", "AWS Lambda", "AWS S3", "AWS EC2", "Google BigQuery",
"Google Kubernetes Engine", "Google Cloud Functions", "Microsoft Azure", "Azure DevOps", "Azure Functions", "Salesforce", "SAP", "Oracle ERP", "Workday", "ServiceNow",
"Splunk", "Tableau Prep", "QlikView", "Looker", "D3.js", "Plotly", "Seaborn", "ggplot2", "Jupyter Notebook", "Spyder",
"PyCharm", "Visual Studio Code", "Eclipse", "IntelliJ IDEA", "NetBeans", "Xcode", "Android Studio", "Selenium", "Appium", "JIRA",
"Confluence", "Trello", "Asana", "Slack", "Microsoft Teams", "Zoom", "Figma", "Sketch", "Adobe XD", "InVision"
]

# Tanzanian cities
tanzanian_cities = [
    "Dar es Salaam", "Dodoma", "Mwanza", "Arusha", "Mbeya", "Morogoro", "Tanga", "Kahama", "Tabora", "Zanzibar",
    "Kigoma", "Sumbawanga", "Songea", "Mtwara", "Moshi", "Bukoba", "Singida", "Shinyanga", "Njombe", "Iringa","Bujumbura", "Kampala", "Nairobi", "Addis Ababa", "Kigali", "Juba", "Khartoum", "Cairo", "Alexandria", "Casablanca",
"Marrakesh", "Accra", "Kumasi", "Lagos", "Abuja", "Nairobi", "Mombasa", "Harare", "Bulawayo", "Lusaka",
"Livingstone", "Blantyre", "Lilongwe", "Windhoek", "Gaborone", "Maputo", "Beira", "Antananarivo", "Toamasina", "Port Louis",
"Victoria", "Algiers", "Oran", "Tunis", "Sousse", "Tripoli", "Benghazi", "Monrovia", "Freetown", "Conakry",
"Bamako", "Ouagadougou", "Dakar", "Praia", "Bissau", "Nouakchott", "Niamey", "Abidjan", "Yamoussoukro", "Lomé",
"Cotonou", "Porto-Novo", "Libreville", "Brazzaville", "Kinshasa", "Lubumbashi", "Kananga", "Goma", "Kisangani", "Bujumbura",
"Kigali", "Dar es Salaam", "Dodoma", "Mwanza", "Arusha", "Mbeya", "Morogoro", "Tanga", "Kahama", "Tabora",
"Zanzibar", "Kigoma", "Sumbawanga", "Songea", "Mtwara", "Moshi", "Bukoba", "Singida", "Shinyanga", "Njombe",
"Iringa", "Bangui", "N'Djamena", "Douala", "Yaoundé", "Libreville", "Malabo", "São Tomé", "Luanda", "Lubango",
"Benguela", "Maseru", "Mbabane", "Manzini", "Asmara", "Djibouti", "Hargeisa", "Mogadishu", "Berbera", "Bosaso",
]

# Function to generate random job records
def generate_jobs(num_records=10000):
    jobs = []
    categories = ["Software Development", "System Analyst", "Accountant", "Public Officer", "Loan Officer","Data Scientist", "Network Engineer", "Database Administrator", "Project Manager", "Product Manager",
"Human Resources Manager", "Marketing Manager", "Sales Manager", "Operations Manager", "Financial Analyst",
"Business Analyst", "Quality Assurance Engineer", "IT Support Specialist", "Web Developer", "Mobile Developer",
"UX/UI Designer", "Graphic Designer", "Content Writer", "SEO Specialist", "Digital Marketing Specialist",
"Social Media Manager", "Brand Manager", "Event Planner", "Supply Chain Manager", "Logistics Coordinator",
"Customer Service Representative", "Technical Support Engineer", "Cybersecurity Analyst", "Information Security Manager", "Cloud Architect",
"DevOps Engineer", "Machine Learning Engineer", "AI Specialist", "Data Engineer", "Data Architect",
"Solutions Architect", "Software Architect", "Systems Administrator", "Network Administrator", "Help Desk Technician",
"Biomedical Engineer", "Civil Engineer", "Mechanical Engineer", "Electrical Engineer", "Chemical Engineer",
"Environmental Engineer", "Industrial Engineer", "Construction Manager", "Urban Planner", "Architect",
"Interior Designer", "Landscape Architect", "Teacher", "Professor", "Research Scientist",
"Laboratory Technician", "Medical Doctor", "Nurse", "Pharmacist", "Physiotherapist",
"Dentist", "Veterinarian", "Psychologist", "Therapist", "Social Worker",
"Economist", "Statistician", "Actuary", "Financial Planner", "Investment Banker",
"Real Estate Agent", "Property Manager", "Insurance Agent", "Legal Assistant", "Paralegal",
"Attorney", "Judge", "Journalist", "Editor", "Publisher",
"Translator", "Interpreter", "Librarian", "Archivist", "Museum Curator",
"Tour Guide", "Travel Agent", "Chef", "Restaurant Manager", "Hotel Manager",
"Fitness Trainer", "Sports Coach", "Athlete", "Musician", "Actor",
"Producer", "Director", "Film Editor", "Photographer", "Videographer",]
    

    education_levels = ["Certificate", "Higher Certificate", "Diploma", "Higher Diploma", "Postgraduate Diploma", "Bachelor Degree","Associate Degree", "Professional Diploma", "Graduate Certificate", "Advanced Certificate", "Advanced Diploma",
"Master's Degree", "Executive Master's", "Professional Master's", "Doctoral Degree", "PhD",
"Doctor of Medicine", "Doctor of Dental Surgery", "Doctor of Veterinary Medicine", "Juris Doctor", "Postdoctoral Fellowship",
"Professional Certification", "Trade Certification", "Vocational Training", "Apprenticeship", "Professional License",
"Continuing Education Certificate", "Online Certificate", "Professional Development Certificate", "Specialist Certificate", "Foundation Degree",
"Technical Diploma", "Chartered Qualification", "Membership Certification", "Industry Certification", "Research Degree",
"Clinical Fellowship", "Residency", "Fellowship", "Teaching Certificate", "TESOL Certificate",
"TEFL Certificate", "CELTA Certificate", "MBA", "Executive MBA", "LLM",
"MFA", "MPhil", "MRes", "EdD", "PsyD",
"DMin", "DSW", "DNP", "EngD", "PharmD",
"Certificate of Completion", "Professional Development Award", "Skill Certificate", "Competency Certificate", "Proficiency Certificate",
"Completion Diploma", "Honours Degree", "Double Degree", "Joint Degree", "Integrated Master's",
"Graduate Diploma", "Postgraduate Certificate", "Executive Certificate", "Mini MBA", "Nano Degree",
"Micro Credential", "Skill Badge", "Technical Certificate", "National Certificate", "International Diploma",
"Academic Certificate", "Specialized Diploma", "Leadership Certificate", "Innovation Certificate", "Management Certificate",
"Digital Badge", "Certified Diploma", "Specialist Diploma", "Expert Certificate", "Competence Diploma",
"Short Course Certificate", "Summer School Certificate", "Winter School Certificate", "Intensive Course Certificate", "Workshop Certificate",
"Training Certificate", "Seminar Certificate", "Conference Certificate", "Professional Achievement Certificate", "Certification of Excellence",]

    for _ in range(num_records):
        title = fake.job()
        description = fake.text(max_nb_chars=200)
        company = fake.company()
        location = random.choice(tanzanian_cities) + ", City"
        category = random.choice(categories)
        created_date = fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')
        deadline = (datetime.now() + timedelta(days=random.randint(1, 90))).strftime('%Y-%m-%d')
        salary = round(random.uniform(10000, 1000000), 2)
        requirements = " ".join([fake.word(ext_word_list=academic_terms) for _ in range(random.randint(3, 6))])
        responsibilities = [fake.text(max_nb_chars=100) for _ in range(random.randint(3, 5))]  # Initial responsibilities

        # Generating responsibilities using academic and technical terms
        academic_responsibilities = [fake.sentence(ext_word_list=academic_terms) for _ in range(random.randint(1, 3))]
        technical_responsibilities = [fake.sentence(ext_word_list=technical_terms) for _ in range(random.randint(1, 2))]
        responsibilities.extend(academic_responsibilities)
        responsibilities.extend(technical_responsibilities)

        contact_email = fake.email()
        required_skills = " ".join([fake.word(ext_word_list=technical_terms) for _ in range(random.randint(3, 6))])
        education_level = random.choice(education_levels)

        jobs.append({
            'title': title,
            'description': description,
            'company': company,
            'location': location,
            'category': category,
            'created_date': created_date,
            'deadline': deadline,
            'salary': salary,
            'requirements': requirements,
            'responsibilities': responsibilities,
            'contact_email': contact_email,
            'required_skills': required_skills,
            'education_level': education_level
        })

    return jobs

# Generate job records
jobs_data = generate_jobs()

# Convert to DataFrame
df = pd.DataFrame(jobs_data)

# Save as CSV
df.to_csv('generated_jobs.csv', index=False)

# Display data
st.dataframe(df,use_container_width=True)

# Download link for CSV
st.markdown("""
    ### Download Generated Data

    [Download CSV](generated_jobs.csv)
""")
