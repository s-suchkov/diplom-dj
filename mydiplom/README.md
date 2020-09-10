Установка

cd mydiplom
pip install -r requirements.txt

!!! Перед началом работы в в файле settings.py заполнить поля EMAIL_HOST_USER, EMAIL_HOST_PASSWORD !!!

python manage.py makemigrations
python manage.py migrate

В другом терминальном окне запуститть команду redis-server:
\diplom-dj-master\redis>redis-server
Создать еще один терминал и запустить команду
celery -A mydiplom worker --pool=solo -l info


python manage.py runserver

Запуск тестов

python manage.py test

API также опубликовано на сервере POSTMAN:

https://explore.postman.com/templates/12401/mydiplom