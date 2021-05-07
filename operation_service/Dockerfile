FROM python:3.7
COPY requirements.txt /operationapp/requirements.txt
WORKDIR /operationapp
RUN pip install -r requirements.txt
COPY . /operationapp
ENTRYPOINT ["python"]
CMD ["run.py"]