FROM python:3.11-slim-bullseye

LABEL org.opencontainers.image.authors="Engels F. P. Souza <engels.franca@gmail.com>"
ENV PALESTINE=FREE

RUN useradd -m engels
USER engels
WORKDIR /home/engels

COPY . .

ENTRYPOINT [ "python", "menu.py" ]