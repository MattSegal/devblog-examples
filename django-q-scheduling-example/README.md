# Example Django Q scheduling app

Setup instructions - requires virtualenv, python3

In one terminal window set up Django

```bash
virtualenv env
. env/bin/activate
pip install -r requirements.txt
cd shop
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
# visit localhost:8000/admin and create a Discount
```

In a separate terminal window, create your schedule in the database, then start your Q cluster

```bash
. env/bin/activate
cd shop
# Create a repeating schedule using Django shell
./manage.py shell
from django_q.models import Schedule
Schedule.objects.create(func='discounts.tasks.delete_expired_discounts', minutes=1, repeats=-1)
# Exit the Django shell, then run the Q cluster
./manage.py qcluster
```
