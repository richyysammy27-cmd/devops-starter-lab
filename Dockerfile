FROM alpine:3.20

RUN apk add --no-cache bash

WORKDIR /app

COPY scripts/system_check.sh .

RUN chmod +x system_check.sh

CMD ["./system_check.sh"]
