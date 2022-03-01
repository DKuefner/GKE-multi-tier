FROM ubuntu:20.04
COPY src/requirements.txt .
RUN apt-get update
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
RUN apt-get install -y mysql-client
RUN mkdir /code
COPY src /code
WORKDIR /code
EXPOSE 5000
ENTRYPOINT ["python3", "webapp.py"]