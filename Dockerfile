FROM python:3.9-slim
WORKDIR /app
RUN echo 'CI/CD Pipeline Application is Running' > index.html
EXPOSE 8080
CMD ["python", "-m", "http.server", "8080"]
