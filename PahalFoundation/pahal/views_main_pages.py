from django.shortcuts import render, HttpResponse
from .models import NewVolunteer, ContactUs
from django.contrib import messages

# Create your views here.

def about(request):
    return render(request, 'pahal/aboutUs.html')
def volunteer(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        interest_area = request.POST.get("interestArea")
        about_me = request.POST.get("about")
        try:
            new_volunteer = NewVolunteer(fullName=fullname, email=email, phoneNo=phone,
                                         interestArea=interest_area, about=about_me)
            new_volunteer.save()
            messages.success(request, "Data saved successfully!")

        except Exception as e:
            messages.error(request, f"Error saving data: {e}")

    return render(request, 'pahal/volunteer.html')
def get_involved(request):
    return render(request, 'pahal/get_involved.html')
def contact(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        try:
            contact_us = ContactUs(fullName=fullname, email=email, phoneNo=phone,
                                   subject=subject, message=message)
            contact_us.save()
            messages.success(request, "Data saved successfully!")

        except Exception as e:
            messages.error(request, f"Error saving data: {e}")

    return render(request, 'pahal/contactUs.html')
def donate(request):
    return render(request, 'pahal/donate.html')
