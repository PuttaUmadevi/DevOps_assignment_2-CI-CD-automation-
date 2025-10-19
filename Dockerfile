FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install Flask
EXPOSE 5000

CMD ["python", "app.py"]
