FROM python:3.11-slim-bullseye

LABEL org.opencontainers.image.authors="Engels F. P. Souza <engels.franca@gmail.com>"
LABEL org.opencontainers.image.url="github.com/es99/poo-python-projeto-biblioteca.git"

ENV PALESTINE=FREE

RUN useradd -m engels
USER engels
WORKDIR /home/engels

COPY . .

ENTRYPOINT [ "python", "menu.py" ]