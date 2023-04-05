FROM python:3.8-alpine
WORKDIR src
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY controller.py controller.py
CMD kopf run -A controller.py --verbose