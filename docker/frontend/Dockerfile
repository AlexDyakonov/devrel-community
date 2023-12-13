FROM node:20

WORKDIR /frontend

RUN mkdir -p /opt/node_modules

COPY ./package.json .
COPY ./package-lock.json .

RUN npm ci

COPY . .

CMD ["npm", "run", "build"]