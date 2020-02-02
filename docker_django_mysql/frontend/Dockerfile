#DOCKER FILE FOR FRONTEND

FROM node:13
RUN mkdir /city/frontend/
WORKDIR /city/frontend

#install dependencies
COPY package*.json /city/frontend/

RUN npm install
#RUN npm install express

#add rst of client code
COPY . /city/frontend/
#CMD node index.js

EXPOSE 3000


CMD ["npm","start"]





