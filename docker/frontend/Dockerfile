FROM node:20

WORKDIR /frontend

COPY ./package.json .

RUN npm install

COPY . .

CMD ["npm", "run", "build"]