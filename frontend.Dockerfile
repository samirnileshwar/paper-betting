# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install app dependencies
COPY frontend/package.json ./
COPY frontend/package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
RUN npm install react-router-dom --save
RUN npm install bootstrap
RUN npm install axios
RUN npm install react-bootstrap-validation --save
RUN npm install react-bootstrap bootstrap

# add app
COPY ./frontend ./

# start app
CMD ["npm", "start"]