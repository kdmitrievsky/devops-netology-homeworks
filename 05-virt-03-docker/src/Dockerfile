FROM ubuntu:jammy

MAINTAINER Konstantin Dmitrievsky "kdm77@mail.ru"

RUN apt-get -y update

RUN apt-get install -y nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY ./index.html /usr/share/nginx/html/index.html

CMD [ "nginx" ]

EXPOSE 80
