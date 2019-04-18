
# Pull base image.
FROM ubuntu:latest

# Update package
RUN apt update -y

# Install python setuptools
RUN apt install -y python3-setuptools
RUN apt-get install -y python3 python3-pip python3-dev build-essential wget

# Install
RUN apt-get install python3-pymysql
RUN apt install gcc
RUN apt install -y iputils-ping


# Add and install python modules
RUN mkdir /home/feature_request
WORKDIR /home/feature_request
ADD requirements.txt /home/feature_request
RUN pip3 install -r requirements.txt
ADD . /home/feature_request


# Expose
EXPOSE 5000

# RUN
CMD ["python3", "run.py"]
