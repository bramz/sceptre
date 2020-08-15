FROM python:3.8-alpine
RUN apk update

COPY . /sceptre/

RUN cd sceptre/ && \
    pip install poetry

WORKDIR /sceptre

RUN poetry install

ENTRYPOINT [ "python", "sceptre" ]