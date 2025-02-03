FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Install dependencies required by mysqlclient and pkg-config
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 8001 to communicate with the host
EXPOSE 8001

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
