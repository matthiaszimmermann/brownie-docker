FROM python:3.9

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

RUN apt-get update && apt-get install -y \
    npm

RUN npm install -g ganache-cli

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install eth-brownie

WORKDIR /projects

ENTRYPOINT [ "bash" ]