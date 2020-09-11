     export NGINX_HOST=easytovote.org
     export NGINX_PORT=80
     export SSL_PRIVKEY_FILE=/etc/ssl/privkey.pem
     export SSL_CERTIFICATE_FILE=/etc/ssl/cert.pem
     export WEB=web
     export ADDXFORWARDEDFOR=$$proxy_add_x_forwarded_for
     export REALIP=\$\$remote_addr
     export HTTPUPGRADE=\$\$http_upgrade
