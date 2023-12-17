FROM node:alpine as build-stage
WORKDIR /frontend
COPY package*.json ./
RUN npm install
COPY . .

CMD ["npm", "run", "build", "--verbose"]