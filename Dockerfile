# this dockerfile from https://github.com/eth-brownie/brownie
FROM python:3.7

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install linux dependencies
RUN apt-get update && apt-get install -y libssl-dev
RUN apt-get update && apt-get install -y npm

RUN npm install --global ganache-cli

RUN wget https://raw.githubusercontent.com/eth-brownie/brownie/master/requirements.txt

RUN pip install -r requirements.txt
RUN pip install eth-brownie

WORKDIR /projects

ENTRYPOINT [ "bash" ]