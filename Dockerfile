FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn requests
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]