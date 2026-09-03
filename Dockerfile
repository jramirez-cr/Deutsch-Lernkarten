FROM python:3.14-slim
WORKDIR /app
RUN pip install --no-cache-dir pytest pytest-cov
COPY . .
CMD ["python", "deutsch-lernkarten.py"]