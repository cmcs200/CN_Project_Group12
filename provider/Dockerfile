FROM python:3
WORKDIR /app

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python","server.py"]
