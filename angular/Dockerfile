FROM node:16.16.0-alpine as builder

RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY angular-app/package.json angular-app/package-lock.json /app/angular-app/

# Install app dependencies.
RUN npm install --prefix angular-app

# Copy app files.
COPY . /app

# Build app
RUN npm run build --prefix angular-app -- --output-path=./dist/out

### Stage 2: delivery ###

FROM nginx:1.23.1-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/

# Copy output directory from builder to nginx image.
COPY --from=builder /app/angular-app/dist/out /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf