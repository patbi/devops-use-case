# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install any needed packages specified in requirements.txt
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

LABEL MAINTAINER=biyagapatrick@gmail.com
LABEL version=1.0

# ARG folder
ARG folder=/app

# Set the working directory WORKDIR /app
WORKDIR $folder

# Copy the current directory contents into the container at /app
COPY . $folder/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]