#DOCKER FILE FOR FRONTEND

FROM node:13
RUN mkdir /frontend/
WORKDIR /city/frontend

#install dependencies
COPY package*.json /city/frontend/

RUN npm install
#RUN npm install express

#add rst of client code
COPY . /frontend/
#CMD node index.js

#TODO PORT MAPPING!
#NOT LISTENING TO RIGHT PORT
EXPOSE 3000


CMD ["npm","start"]





