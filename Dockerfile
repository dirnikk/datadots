# Stage 1: Build Stage
FROM python:3.12-slim AS build

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Flask in the production image
RUN pip install --no-cache-dir Flask

# Expose port 5000 to allow communication to/from the Flask web server
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
