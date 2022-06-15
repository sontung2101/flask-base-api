FROM python:3.8-slim

RUN apt-get -y update && apt-get install -yq supervisor

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./ /home/
WORKDIR /home/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV ENV=production

#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
