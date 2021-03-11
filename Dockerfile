FROM python:3.9.1

WORKDIR /core
COPY dev-requirements.txt requirements.txt /core/
RUN pip install -r dev-requirements.txt
ADD app /core/app


EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
