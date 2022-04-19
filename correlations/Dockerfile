FROM python:3
WORKDIR /correlations
COPY requirements.txt /correlations
RUN pip install -r requirements.txt
COPY . /correlations
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]
