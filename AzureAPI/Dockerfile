FROM ubuntu:latest

MAINTAINER Michael Levan

CMD tail -f /dev/null

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 80
EXPOSE 5000

COPY ./requirements.txt /AzureAPI/requirements.txt

WORKDIR /AzureAPI

RUN pip3 install -r requirements.txt

COPY . /AzureAPI

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

