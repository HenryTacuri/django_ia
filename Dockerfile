FROM python:3.11.1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential g++ libffi-dev python3-dev gcc make libmagic-dev postgresql-server-dev-all

COPY requirements.txt ./

RUN pip install numpy==2.0.2 scikit-learn==1.4.2 pandas==2.2.2 tensorflow==2.18.0 djangorestframework==3.15.2

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
