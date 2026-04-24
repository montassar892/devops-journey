# Start from a Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install the requests library
RUN pip install requests

# Copy your script into the container
COPY app.py .

# Run the script when the container starts
CMD ["python", "app.py"]
