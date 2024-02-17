FROM python:latest
RUN mkdir -p /DockerWorkspace
WORKDIR /DockerWorkspace
COPY /dependencies/chromedriver_linux64/chromedriver /usr/local/bin/
COPY requirements.txt ./
RUN ls -ltr
RUN pip install --upgrade pip
RUN pip install behave selenium
RUN pip install -r requirements.txt
COPY . .
CMD ["behave"]