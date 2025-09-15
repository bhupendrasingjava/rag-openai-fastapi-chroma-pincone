# Use a slim Python base image
FROM python:3.11-slim

# Prevents Python from writing .pyc files and buffers logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (gcc etc. only if needed)
COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev curl \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . .

# Render will provide PORT at runtime (default 10000)
ENV PORT=10000
EXPOSE 10000

# Run with Gunicorn + Uvicorn worker
# IMPORTANT: sh -c ensures $PORT is expanded correctly
#CMD ["sh", "-c", "gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:$PORT"]
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:10000"]
