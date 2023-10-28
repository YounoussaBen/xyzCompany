from django.db import models

# Define a Company model to store company information, including the logo and email
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='static/company_logos/')
    email = models.EmailField()

    def __str__(self):
        return self.name

# Define a JobCategory model for classifying jobs
class JobCategory(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, default='fa fa-tasks') # Add the field for the category's icon class
    vacancy = models.PositiveIntegerField(default=0)  # Add the field for the number of vacancies in this category

    def __str__(self):
        return self.name

# Define a Job model to represent the job posting
class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')])
    salary_range = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()

    # Add a Many-to-One relationship to associate the job with a company
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # Add a Many-to-Many relationship to categorize the job with one or more categories
    categories = models.ManyToManyField(JobCategory)

    def __str__(self):
        return self.title
