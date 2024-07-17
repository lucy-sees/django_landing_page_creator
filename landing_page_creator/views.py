import os
import subprocess
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import CreateAppForm

def home(request):
    form = CreateAppForm()
    return render(request, 'create_landing_page.html', {'form': form})


def create_app(request):
    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        if app_name:
            try:
                # Change to the project root directory
                os.chdir(settings.BASE_DIR)
                
                # Run the Django command to start a new app
                subprocess.run(['python', 'manage.py', 'startapp', app_name], check=True)
                
                # Add the new app to INSTALLED_APPS
                with open(os.path.join(settings.BASE_DIR, 'your_project_name', 'settings.py'), 'a') as f:
                    f.write(f"\nINSTALLED_APPS.append('{app_name}')")
                
                messages.success(request, f'Successfully created new app: {app_name}')
                return redirect('home')  # Redirect to home page or wherever appropriate
            except subprocess.CalledProcessError as e:
                messages.error(request, f'Error creating app: {str(e)}')
            except Exception as e:
                messages.error(request, f'Unexpected error: {str(e)}')
        else:
            messages.error(request, 'App name is required')
    
    return render(request, 'create_landing_page.html')