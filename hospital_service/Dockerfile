FROM python:3.7
COPY requirements.txt /hospitalapp/requirements.txt
WORKDIR /hospitalapp
RUN pip install -r requirements.txt
COPY . /hospitalapp
ENTRYPOINT ["python"]
CMD ["run.py"]