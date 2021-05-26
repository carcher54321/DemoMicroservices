FROM python:3.7
COPY requirements.txt /hospitalapp/requirements.txt
WORKDIR /hospitalapp
RUN pip install -r requirements.txt
COPY . /hospitalapp
CMD ["flask db init"]
CMD ["flask db migrate"]
CMD ["flask db upgrade"]
ENTRYPOINT ["python"]
CMD ["run.py"]
