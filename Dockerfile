FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /django-test

# Install dependencies
COPY requirements.txt /django-test/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /django-test/
