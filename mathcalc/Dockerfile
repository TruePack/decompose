# Base image.
FROM python:3

# Сreate a folder where the application will be deployed.
RUN mkdir -p /mathcalc

# Сhange directory to created folder.
WORKDIR /mathcalc 

# Copy all the files from the current directory (where the Dockerfile
# is located) to the current directory in the image (/mathcalc).
COPY . /mathcalc

# Download all dependencies.
RUN pip install -r requirements.txt

# Start Django-server.
CMD python ./manage.py runserver 0.0.0.0:8000 

#Forward port to host system.
EXPOSE 8000
