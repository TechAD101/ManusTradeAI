
# Backend Stage
FROM python:3.9-slim as backend

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

# Frontend Stage
FROM node:16 as frontend

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY frontend/ .

RUN npm run build

# Final Stage
FROM python:3.9-slim

WORKDIR /app

COPY --from=backend /app .
COPY --from=frontend /app/build ./static

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]


