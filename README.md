1) docker pull rabbitmq |
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
2) http://127.0.0.1:15672 |
celery -A myshop worker -l info -P eventlet
3) stripe login |
stripe listen --forward-to localhost:8000/payment/webhook/
4) python manage.py runserver
