FROM node:latest AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
ENV NODE_ENV=production
RUN npm run build
RUN cp dist/index.html dist/404.html