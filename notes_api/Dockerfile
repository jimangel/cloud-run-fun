# Use the official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Make migrations
RUN python manage.py makemigrations notes

# Apply migrations
RUN python manage.py migrate

# Collect static files
#RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
