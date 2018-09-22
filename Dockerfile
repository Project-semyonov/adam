FROM python:3-alpine
ADD example.py .
CMD [ "python3", "./example.py"]
