# pull official python runtime image from docker as parent image
FROM python:3.6
ENV PYTHONUNBUFFERED 1


#
# backend will be its own volume
#

#adding backend directory to make absolute filepaths
RUN mkdir /backend/
WORKDIR /city/backend

#install python dependencies for backend
ADD requirements.txt /city/backend/
RUN pip install --upgrade pip && pip install -r requirements.txt

# add rest of code
ADD . /city/backend

# evtl make port available for app
#EXPOSE 8000

#CMD python3 manage.py runserver 0.0.0.0:8000

