FROM python:3.12.6-alpine
WORKDIR /app

COPY requirements.txt .

RUN apk update
RUN apk add --no-cache shadow && rm -rf /var/lib/apt/lists/*
RUN PIP_ROOT_USER_ACTION=ignore pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r appgroup && useradd -r -g appgroup appuser
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8001

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8001"]
