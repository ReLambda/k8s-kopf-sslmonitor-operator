FROM python:3.8-alpine
RUN pip3 install --upgrade pip

WORKDIR src
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY controller.py controller.py
CMD kopf run -n * controller.py --verbose