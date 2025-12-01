FROM python:3.14.0-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY app .

FROM builder AS test

WORKDIR /app

ENV PYTHONPATH=/install/lib/python3.14/site-packages:/app
ENV PATH=/install/bin:$PATH

RUN pytest tests -q --disable-warnings --maxfail=1

FROM builder AS final

WORKDIR /app

COPY --from=builder /install /usr/local

COPY --from=builder /app .

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "src/app.py"]
