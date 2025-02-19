# Social-Media-App
Welcome to the Social Media App repository! This project is a simple social media application built with Django. Users can register, log in, create posts with images, update posts, and delete posts. The application also includes user messages for actions like login, logout, create post, update post, and delete post.

Key Features
User Authentication: Secure user login, registration, and logout using Django's built-in authentication system.

Post Management: Create, update, and delete posts with image uploads.

User Feedback: Real-time feedback messages for various actions like login, logout, post creation, and deletion.

Responsive Design: Utilizes Bootstrap for a responsive and visually appealing interface.

Security: Ensures only authenticated users can access certain pages and protects forms with CSRF tokens.

Setup Instructions
Prerequisites
Python 3.x

Django 3.x or higher

pip (Python package installer)

Setup Instructions


Clone the Repository:
git clone https://github.com/Istiak-Hossen-Shihab/Social-Media-App.git
cd Social-Media-App


Create and Activate a Virtual Environment:
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`


Install Dependencies:
pip install -r requirements.txt


Configure the Database:
Apply migrations to set up the database:
python manage.py makemigrations
python manage.py migrate


Create a Superuser:
Create a superuser to access the Django admin panel:
python manage.py createsuperuser


Run the Development Server:
Start the Django development server:
python manage.py runserver
Access the Application:

Open your browser and go to http://127.0.0.1:8000/ to access the application



Configuration
Ensure that your settings.py file includes the following configurations:

Media Settings:
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Messages Framework:
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
URLs Configuration
Ensure your urls.py files are correctly configured to include app URLs and serve media files during development.

Main urls.py:
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Users urls.py


from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]


Design Rationale
User Authentication:
1.Utilizes Django's built-in authentication system for secure user login, registration, and logout.

2.Custom logout view to provide user feedback using Django's messages framework.

Post Management:

1.Users can create, update, and delete posts with images.

2.Image upload and storage configured using Django's media settings.

User Messages:

1.Implements Django's messages framework to provide feedback for actions such as login, logout, post creation, post update, and post deletion.

2.Messages are displayed using Bootstrap alerts for a consistent and responsive UI.

Responsive Design:

1.Uses Bootstrap for a responsive and visually appealing design.

2.Ensures a consistent look and feel across different devices and screen sizes.

Security:

1.Protects views with login_required decorators to ensure only authenticated users can access certain pages.

2.Uses CSRF tokens in forms to protect against Cross-Site Request Forgery attacks.

Contributing
*Feel free to submit issues or pull requests. Contributions are welcome!

License
*This project is licensed under the MIT License.
