FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /chemist
WORKDIR /chemist
COPY requirements.txt /chemist/
COPY entrypoint.sh /chemist/
RUN pip install -r requirements.txt
COPY . /chemist/