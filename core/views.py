from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForm
from .models import JobCategory, Job, Company
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import JobApplicationForm
import mimetypes


def home_view(request):
    # Get categories and job listings, customize this as needed
    categories = JobCategory.objects.all()
    job_listings = Job.objects.all()
    companies = Company.objects.all()

    # Prepare data to pass to the template
    context = {
        'categories': categories,
        'job_listings': job_listings,
        'companies': companies, 
        
    }

    return render(request, 'home.html', context)


def questionnaire(request):
    # Add logic to handle the questionnaire URL or redirect to the actual survey URL
    # For example, redirecting to an external survey link:
    return redirect('https://htionline.tue.nl/limesurvey/index.php/476626?lang=en')

def category_view(request, category_id):
    # Retrieve the selected category based on its ID
    category = get_object_or_404(JobCategory, pk=category_id)

    # Retrieve the jobs associated with the selected category
    jobs = Job.objects.filter(categories=category)

    context = {
        'category': category,
        'jobs': jobs,
    }

    return render(request, 'category.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job  # Associate the application with the job
            application.save()

            # Send email to the company with the application data
            subject = f'New Job Application for {job.title}'
            message = f'You have received a new job application from {application.name}. Details:\n\n' \
                      f'Name: {application.name}\n' \
                      f'Email: {application.email}\n' \
                      f'Portfolio: {application.portfolio}\n' \
                      f'Cover Letter:\n{application.cover_letter}\n'

            from_email = 'felixkoranteng290@gmail.com'  # Sender's email
            recipient_list = [job.company.email]  # Company's email

            # Attach the resume file
            resume = application.resume
            if resume:
                email = EmailMessage(
                    subject, message, from_email, recipient_list
                )

                # Determine the MIME type of the file
                content_type, _ = mimetypes.guess_type(resume.name)
                if not content_type:
                    content_type = "application/octet-stream"  # Default to binary if MIME type is not found

                email.attach(resume.name, resume.read(), content_type)
                email.send()

            # Notify the user
            send_mail(
                'Application Received',
                'Your job application has been received. We will get in touch with you soon.',
                'felixkoranteng290@gmail.com',  # Sender's email
                [application.email],  # User's email
                fail_silently=False,
            )

            return redirect('home')  # Redirect to the home page after sending the email

    else:
        form = JobApplicationForm()

    context = {
        'job': job,
        'form': form,
    }

    return render(request, 'job_detail.html', context)


def full_time_jobs(request):
    full_time_jobs = Job.objects.filter(job_type='Full Time')
    return render(request, 'job_list.html', {'jobs': full_time_jobs, 'category_name': 'Full Time Jobs'})

def part_time_jobs(request):
    part_time_jobs = Job.objects.filter(job_type='Part Time')
    return render(request, 'job_list.html', {'jobs': part_time_jobs, 'category_name': 'Part Time Jobs'})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                f'From: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['geazyskay@gmail.com'],  # Replace with your email address
                fail_silently=False,
            )
            return redirect('contact')  # Redirect to the contact page after sending the email

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

