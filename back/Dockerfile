FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /back
WORKDIR /back
COPY ./requirements.txt /back/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /back/