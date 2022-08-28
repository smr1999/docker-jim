FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt ./
COPY ./run.py ./
RUN pip install -r requirements.txt
CMD ["python","run.py"]