FROM python:3.8-alpine
RUN apk update

COPY . /sceptre/

RUN cd sceptre/ && \
    poetry install

WORKDIR /sceptre
ENTRYPOINT [ "python", "sceptre" ]