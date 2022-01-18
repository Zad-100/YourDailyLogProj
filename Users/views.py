from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register a new user to the app"""
    
    if request.method != 'POST':
        # Display blank registration form.
        formForRegistration = UserCreationForm() # creating an instance
    else:
        # Process completed form
        formForRegistration = UserCreationForm(data=request.POST)

        if formForRegistration.is_valid():
            newUser = formForRegistration.save()

            # Log the user in and then return to the home page
            login(request, newUser)

            return(redirect('YourDailyLog_App:index'))

    # Display a blank or invalid form
    context = {"formForRegistration": formForRegistration}

    return(render(request, "registration/register.html", context))