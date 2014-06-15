FROM dockerfile/python
MAINTAINER Tech For Elissa <techforelissa@gmail.com>

ENV PYTHONIOENCODING utf-8

ADD requirements.txt /src/requirements.txt
WORKDIR /src
RUN ["pip", "install", "-r", "requirements.txt"]
ADD . /src

ENV FROM_DATE 01/01/2014
ENV TO_DATE 06/01/9999
ENV REPORT_TYPE con

CMD ["python", "scrape.py"]
