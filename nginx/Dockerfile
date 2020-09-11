FROM nginx:1.19.2
RUN rm /etc/nginx/conf.d/default.conf
#COPY ./default.conf /etc/nginx/default.conf
#RUN mv /etc/nginx/default.conf /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
COPY /etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./ssl/privkey.pem /etc/ssl/privkey.pem
COPY ./ssl/cert.pem /etc/ssl/cert.pem
