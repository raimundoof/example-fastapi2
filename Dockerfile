FROM python:3.9.7

WORKDIR /usr/srv/app

COPY requirements.txt ./

RUN pip install --no-cache -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


