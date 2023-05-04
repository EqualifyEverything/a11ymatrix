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

# Set the Database vars
ENV DB_HOST postgres
ENV DB_PORT 5432
ENV DB_USER a11ydata
ENV DB_PASSWORD a11yAllTheThings!
ENV DB_NAME a11ydata


# Logging Level
ENV LOG_LEVEL INFO

EXPOSE $APP_PORT

# Run the application
CMD ["python", "src/endpoints.py"]
