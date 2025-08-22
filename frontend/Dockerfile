FROM node:20-alpine
WORKDIR /app
COPY frontend/package.json ./package.json
COPY frontend/package-lock.json ./package-lock.json
RUN npm install
COPY frontend/src ./src
COPY frontend/public ./public
EXPOSE 3000
CMD ["npm", "start"]
