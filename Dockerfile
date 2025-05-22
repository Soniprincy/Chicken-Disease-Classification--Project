FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN  pip install --no-cache-dir -r requirements.txt

RUN echo "Reached end of Dockerfile"

CMD ["python", "app.py"]