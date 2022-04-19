FROM mongo
COPY import.sh .
RUN chmod +x import.sh
EXPOSE 80
CMD ["bin/bash", "import.sh"]

