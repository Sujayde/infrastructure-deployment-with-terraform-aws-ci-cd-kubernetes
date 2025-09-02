# Stage 1: Build stage
FROM python:3.11-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .

# Stage 2: Production stage
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]
