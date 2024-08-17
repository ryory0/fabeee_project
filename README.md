docker build -t my-django-app .

docker run -d --name my-django-container -p 8000:8000 my-django-app
