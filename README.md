# Cinema Project

This project is a cinema management system built using Django.

## Accessing the Project

### Prerequisites
- Python 3.8+
- Django 3.2+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone <Your Repository URl>
   cd CINEMA_PROJECT

#### Runing the server
python manage.py runserver 0.0.0.0:8000

##### Open a web browser on any device connected to the same network and navigate to:
http://<your_local_ip>:8000/
For content management and administration:
http://<your_local_ip>:8000/admin/

##### ### ADD your host to the "ALLOWED_HOSTS"
To add your host to the ALLOWED_HOSTS setting in Django, follow these steps:

Open your settings.py file located in your Django project directory (CINEMA_PROJECT/cinema_project/settings.py).

Find the ALLOWED_HOSTS setting and uncomment it if it's commented out:

Copy code
ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
    '192.168.0.108',  # Add your host IP address here
]
Replace 'yourdomain.com' and 'www.yourdomain.com' with your actual domain names if your Django application is deployed on a server with a domain name.

Save the settings.py file.

Ensure that your Django server is restarted to apply the new settings.
