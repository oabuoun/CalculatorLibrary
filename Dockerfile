FROM python:alpine3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD python ./calculator.py

#COPY requirements.txt /app/requirements.txt
#ENTRYPOINT ["python", "./calculator.py"]
