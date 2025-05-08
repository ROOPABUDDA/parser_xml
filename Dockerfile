# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install required Python libraries
RUN pip install --no-cache-dir lxml jsonschema

# Set the command to run the Python script when the container starts
CMD ["python", "xml_to_json.py"]
