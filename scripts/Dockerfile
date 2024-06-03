# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file from the root folder to the working directory
COPY ../requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents of scripts into the container at /app
COPY . /app

# Run data_fetch.py when the container launches
CMD ["python", "/app/data_fetch.py"]
