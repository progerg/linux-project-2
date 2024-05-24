FROM python:3.9-slim
WORKDIR /app
COPY data_processor.py /app
RUN pip install requests
CMD ["python", "data_processor.py"]
