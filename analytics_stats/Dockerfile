FROM python:3
WORKDIR /analytics_stats
COPY requirements.txt /analytics_stats
RUN pip install -r requirements.txt
COPY . /analytics_stats
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]

