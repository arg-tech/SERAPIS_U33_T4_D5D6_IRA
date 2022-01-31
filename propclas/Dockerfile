FROM python:3.8

RUN pip install --upgrade pip

RUN pip install numpy
RUN pip install pandas
RUN pip install transformers==4.9.2
RUN pip install torch
RUN pip install sklearn
RUN pip install CherryPy
RUN pip install pickle-mixin

COPY lr_0.76_BERT_15-03-21.pkl .
COPY pproc.py .
COPY ws.py .

EXPOSE 8199
ENTRYPOINT ["python", "ws.py"]
