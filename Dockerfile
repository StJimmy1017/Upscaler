FROM python:3.10-slim

RUN pip install requirements.txt

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
    
ENV FLASK_ENV=production

COPY . /opt/

EXPOSE 80

WORKDIR /opt

ENTRYPOINT ["python", "app.py", "--port", "80"]
