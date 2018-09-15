FROM python:3-alpine
ADD Test.py .
CMD [ "python3", "./Test.py"]
