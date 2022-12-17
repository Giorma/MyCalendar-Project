from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .forms import DateForm


def home(request):
    time_threshold = datetime.now() + timedelta(hours=4)

    return render(request, 'home.html', {
        'current_date': time_threshold,

    })


def user(request):
    if request.method == 'POST':
        form = DateForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            input_date = form.cleaned_data['date']
            current_date = datetime.now().date()
            years_passed = current_date.year - input_date.year

            # Check if the current month and day are before the input month and day
            if current_date.month < input_date.month or (
                    current_date.month == input_date.month and current_date.day < input_date.day):
                years_passed -= 1
            years_passed = f"{years_passed}, Years Passed After {first_name}'s Birth "
            first_name = f'First Name: {first_name.capitalize()}'
            last_name = f'Last Name: {last_name.capitalize()}'

            return render(request, 'user.html', {'form': form, 'years_passed': years_passed,
                                                 'first_name': first_name,
                                                 'last_name': last_name})

    else:
        form = DateForm()
    return render(request, 'user.html', {'form': form})
