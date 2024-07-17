import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "landing_page_project.settings")
django.setup()

# Create project directory
project_name = "landing_page_project"
os.makedirs(project_name, exist_ok=True)
os.chdir(project_name)

# Create Django project
execute_from_command_line(["django-admin", "startproject", project_name, "."])

# Create app
app_name = "landing_page"
execute_from_command_line(["django-admin", "startapp", app_name])

# Update settings.py
settings_path = os.path.join(project_name, "settings.py")
with open(settings_path, "a") as f:
    f.write(f"\nINSTALLED_APPS.append('{app_name}')")

# Create views.py content
views_content = """
from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = "landing_page/index.html"
"""

with open(os.path.join(app_name, "views.py"), "w") as f:
    f.write(views_content)

# Create urls.py content for the app
app_urls_content = """
from django.urls import path
from .views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
]
"""

with open(os.path.join(app_name, "urls.py"), "w") as f:
    f.write(app_urls_content)

# Update project urls.py
project_urls_path = os.path.join(project_name, "urls.py")
with open(project_urls_path, "r+") as f:
    content = f.read()
    f.seek(0, 0)
    f.write("from django.urls import path, include\n" + content)
    f.write("\nurlpatterns.append(path('', include('{}.urls')))".format(app_name))

# Create templates directory and index.html
os.makedirs(os.path.join(app_name, "templates", app_name), exist_ok=True)
index_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Our Landing Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .container {
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Our Amazing Product</h1>
        <p>Discover the future of innovation right here.</p>
        <a href="#" class="cta-button">Learn More</a>
    </div>
</body>
</html>
"""

with open(os.path.join(app_name, "templates", app_name, "index.html"), "w") as f:
    f.write(index_html_content)

print("Django landing page project created successfully!")
print("To run the server, use the following command:")
print("python manage.py runserver")