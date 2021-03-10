FROM python:3.9.1

WORKDIR /app/
COPY dev-requirements.txt requirements.txt /app/
RUN pip install -r dev-requirements.txt
ADD app test /app/
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
