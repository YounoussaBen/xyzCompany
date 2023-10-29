from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import JobCategory, Job, Company
# Create your views here.



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
