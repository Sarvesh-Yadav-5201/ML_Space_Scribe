# Using an official Python 3.8 slim as an base Image
FROM python:3.10-slim

# Setting the working directory to /app
WORKDIR /app

# Ensuring we have an up-to-date baseline and install any OS dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Adding a user 'app'
RUN useradd -ms /bin/bash app

# Copying the local directory to the container
COPY . .

# Installing necessary packages using pipenv
RUN pip install --no-cache-dir pipenv && \
    pipenv sync

# # Set the entry point to /bin/bash
ENTRYPOINT ["/bin/bash"]

# Setting the command to open up pipenv shell
# CMD ["pipenv", "run", "python","data_extraction.py"]