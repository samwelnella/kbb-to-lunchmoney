# Usage:
#   docker build -t kbb-to-lunchmoney .
#   docker run --env-file .env -it kbb-to-lunchmoney
#   docker run --env-file .env -it kbb-to-lunchmoney bash

FROM python:3.9.6

# clean eliminates the need to manually `rm -rf` the cache
RUN set -eux; \
  \
  apt-get update; \
  apt-get install -y --no-install-recommends \
    bash \
    nano less \
    chromium chromium-driver \
    cron; \
  apt-get clean;

# TODO this will not work once the cryptography package is updated
#      we must install python3-dev when it's package version is updated to 3.9.6
# https://stackoverflow.com/questions/66118337/how-to-get-rid-of-cryptography-build-error
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN set -eux; \
  # lock to specific version to avoid rust compilation
  pip3 install cryptography==3.4.8;

# run every hour by default, use `SCHEDULE=NONE` to run directly
ENV SCHEDULE "0 * * * *"

WORKDIR /app
COPY . ./

# run after copying source to chache the earlier steps
RUN pip install -r requirements.txt

CMD ["bash", "cron.sh"]
