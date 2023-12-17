FROM certbot/certbot

RUN mkdir -p /etc/letsencrypt && mkdir -p /var/www/certbot

COPY certbot_entrypoint.sh /certbot_entrypoint.sh
RUN chmod +x /certbot_entrypoint.sh

ENTRYPOINT ["/certbot_entrypoint.sh"]