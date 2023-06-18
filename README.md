1) Check that you have launched PostgreSQL with db like in project settings
2) `python manage.py migrate`
3) if you want to upload data from initial_data.json file run:
   - `python manage.py loaddata initial_data.json`