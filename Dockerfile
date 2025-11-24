# Use Python as the base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all files to the container
COPY . .

# Expose the HTTPS port
EXPOSE 443

# Run the app
CMD ["python", "app.py"]