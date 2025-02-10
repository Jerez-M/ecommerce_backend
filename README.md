## Ecommerce backend

Setup Instructions

1. Clone the Repository

git clone <your-repo-url>
cd <your-project-folder>

2. Create a Virtual Environment and Activate It

python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Database Setup

Since this project uses SQLite, the database file (db.sqlite3) is included. However, if you want to reset the database, run:

python manage.py migrate

To load the existing data (data.json):

python manage.py loaddata data.json

5. Run the Development Server

python manage.py runserver

The API will be available at:

http://127.0.0.1:8000/swagger/