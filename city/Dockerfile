# pull official python runtime image from docker as parent image
FROM python:3.6
ENV PYTHONUNBUFFERED 1

#
# backend will be its own volume
#

#adding backend directory to make absolute filepaths
RUN mkdir /city/
WORKDIR /city/

#install python dependencies for backend
ADD requirements.txt /city/
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# add rest of code
ADD . /city/

# evtl make port available for app
#EXPOSE 8000 0.0.0.0:8000

#CMD python manage.py runserver 0.0.0.0:8000

