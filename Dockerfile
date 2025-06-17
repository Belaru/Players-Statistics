FROM ubuntu:22.04

# Avoids interactive prompts during package install
# ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3, pip, and dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-tk && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install matplotlib

CMD ["python3", "main.py"]
