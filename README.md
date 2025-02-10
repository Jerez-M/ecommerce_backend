# E-Commerce Platform RESTful API

The E-Commerce Platform RESTful API is a highly scalable and secure API built using Django and PostgreSQL. It supports advanced features such as user authentication, product management, order processing, reviews, and real-time notifications. The project also includes an analytics dashboard and deployment instructions for AWS Lightsail.
Installation

## Use the following steps to set up the project locally.

Clone the repository:

```bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up database:

    Use the sqlite3 db which already contains the test data.
    alternative: If you don’t want to use my db.sqlite3, you can create your own db and then import the test data that i put in data.json file. use the command below to import it into your databbase.

    ```bash
    python manage.py loaddata data.json
    ```

Run migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Access api on [http://127.0.0.1:8000/swagger/]


## Deployment to AWS Lightsail

Create a Lightsail instance:

    Log in to your AWS Lightsail account.

    Create a new instance using the "OS Only" option and select Ubuntu 20.04 LTS.

    Connect to your instance using SSH.


Install dependencies on the instance:

```bash
sudo apt-get update
sudo apt-get install python3-pip python3-venv postgresql postgresql-contrib redis
```

Set up PostgreSQL:

    Create a new PostgreSQL database and user.

    Update the DATABASES setting in settings.py with your database credentials.

Clone the repository:

```bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Run migrations:

```bash
python manage.py migrate
```

Set up Gunicorn:

Install Gunicorn:

```bash
pip install gunicorn
```

Create a Gunicorn service file:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add the following content:

    ```ini
    [Unit]
    Description=gunicorn daemon
    After=network.target

    [Service]
    User=ubuntu
    Group=www-data
    WorkingDirectory=/home/ubuntu/ecommerce-api
    ExecStart=/home/ubuntu/ecommerce-api/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/ecommerce-api/ecommerce.sock ecommerce.wsgi:application

    [Install]
    WantedBy=multi-user.target
    ```

Start and enable the Gunicorn service:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```
Set up Nginx:

Install Nginx:

```bash
sudo apt-get install nginx
```

Create a new Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/ecommerce
```

Add the following content:
    nginx

    server {
        listen 80;
        server_name your_domain_or_ip;

        location / {
            proxy_pass http://unix:/home/ubuntu/ecommerce-api/ecommerce.sock;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

Enable the Nginx configuration:

```bash
sudo ln -s /etc/nginx/sites-available/ecommerce /etc/nginx/sites-enabled/
```
Test the Nginx configuration:

```bash
sudo nginx -t
```
Restart Nginx:

```bash
sudo systemctl restart nginx
```

Set up CI/CD:

We can use GitHub Actions or any too like jenkins to setup CI/CD to automate the the deployments.