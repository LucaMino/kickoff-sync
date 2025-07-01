FROM python:3.9-slim

# define Supercronic download URL and checksum
ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.2.34/supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=e8631edc1775000d119b70fd40339a7238eece14 \
    SUPERCRONIC=supercronic-linux-amd64

# install curl and ca-certificates, download and install Supercronic
RUN apt-get update && apt-get install -y curl ca-certificates \
    && curl -fsSLO "$SUPERCRONIC_URL" \
    && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
    && chmod +x "$SUPERCRONIC" \
    && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
    && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

# set work dir
WORKDIR /app

# copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy source code and crontab file
COPY src/ /app/src/
COPY crontab /app/crontab

# use Supercronic to run the scheduled tasks defined in crontab
CMD ["supercronic", "/app/crontab"]