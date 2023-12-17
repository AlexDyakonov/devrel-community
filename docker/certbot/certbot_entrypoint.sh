#!/bin/sh

trap exit TERM

# DOMAIN=$(echo $ALLOWED_HOST | cut -d ',' -f1) # Если ALLOWED_HOST содержит несколько доменов, разделенных запятой, берем первый

certbot certonly --webroot --webroot-path=/var/www/certbot --register-unsafely-without-email --agree-tos -d shampiniony.ru --quiet

while :; do 
  certbot renew --webroot --webroot-path=/var/www/certbot --quiet
  sleep 12h & wait $${!}
done