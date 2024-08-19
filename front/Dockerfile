FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /front
WORKDIR /front
COPY ./requirements.txt /front/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /front/
