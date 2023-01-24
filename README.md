# Ice Cream Parlor

This simple website is designed to be used by an ice cream parlor
to take online orders.
Customers can order ice cream providing name, phone number,
desired flavors and pickup time. 
Admins can view orders' details, change pickup times and flavors.

Customer interface: domain <br>
Admin interface: domain/admin

## How to Run
1. Create an ".env" file containing SECRET_KEY and HOST


2. Install requirements:

       install -r requirements.txt

3. Fill database with fixtures:

       python manage.py loaddata flavor.json
       python manage.py loaddata prepduration.json

4. Create the first admin:

       python manage.py createsuperuser


