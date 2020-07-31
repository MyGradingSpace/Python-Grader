FROM python:3.8 as base
WORKDIR /app
RUN chmod 777 /app
COPY . /app
RUN pip install requests
CMD [ "python", "main.py" ]