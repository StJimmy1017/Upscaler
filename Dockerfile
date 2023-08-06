FROM python:3.10-slim

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV=production

COPY . /opt/

EXPOSE 80

WORKDIR /opt

ENTRYPOINT ["python", "app.py", "--port", "80"]
