from python:3.11-slim

WORKDIR /app

COPY main.py /app/main.py
COPY tst.py /app/test.py

RUN pip install flask

EXPOSE 5000

CMD ["python", "main.py"]