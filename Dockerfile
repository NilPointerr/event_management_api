FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /app/venv

COPY requirements.txt .
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

ENV PATH="/app/venv/bin:$PATH"

CMD ["/bin/sh", "-c", "source /app/venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
