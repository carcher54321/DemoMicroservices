FROM python:3.7
COPY requirements.txt /surgeryapp/requirements.txt
WORKDIR /surgeryapp
RUN pip install -r requirements.txt
COPY . /surgeryapp
ENTRYPOINT ["python"]
CMD ["run.py"]