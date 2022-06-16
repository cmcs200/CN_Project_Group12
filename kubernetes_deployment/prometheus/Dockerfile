FROM python:3.10.4-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN chmod u+x main.py
ENTRYPOINT ["python"]
CMD ["main.py"]
