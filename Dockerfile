FROM ubuntu:18.04
MAINTAINER Gokce Demir

ENV TZ=Europe/Istanbul
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /app
COPY ./requirements.txt .   
RUN pip install -r requirements.txt
ADD . .
ENTRYPOINT [ "python" ]
CMD [ "getDate.py" ]