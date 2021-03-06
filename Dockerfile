FROM ubuntu:16.04
RUN ln -sf /bin/bash /bin/sh
MAINTAINER Sachin Muralidhara <sachin.muralidhara@colorado.edu>

RUN apt-get update && apt-get install -y build-essential python-dev python-pip virtualenv git

RUN cd
RUN mkdir -p /home/capio_challenge

WORKDIR /home/capio_challenge

RUN git clone https://github.com/sachinmurali/capio.git

RUN cd capio && pip install -r requirements.txt

WORKDIR /home/capio_challenge/capio/src/
CMD ["python", "app.py"]