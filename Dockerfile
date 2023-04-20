# Use alpine with Python pre-installed
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src /app/src

# Env Variables
ENV APP_PORT 8087

ENV FRANKLIN_URL http://franklin.whatever

# Logging Level
ENV LOG_LEVEL INFO

EXPOSE $APP_PORT

# Run the application
CMD ["python", "src/main.py"]