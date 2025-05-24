FROM python:3.10-slim

COPY app.py /app/app.py
WORKDIR /app

RUN echo "Reached end of Dockerfile"

CMD ["python", "app.py"]