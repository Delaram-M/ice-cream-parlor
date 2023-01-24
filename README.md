# Ice Cream Parlor

This website is designed to be used by an ice cream parlor.
Users can order ice cream (flavors and pickup time). Admins
can view orders, change pickup times and flavors.

User interface: domain </br>
Admin interface: domain/admin

## How to Run
1. Create an ".env" file containing SECRET_KEY and HOST


2. Install requirements:

       install -r requirements.txt

3. Fill database with fixtures:

       python manage.py loaddata flavor.json
       python manage.py loaddata prepduration.json

