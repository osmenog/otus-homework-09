FROM python:3.7.10-alpine as base

FROM base as builder
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PATH=/build/bin/:$PATH

WORKDIR /build

RUN apk update && apk upgrade && \
    apk add --no-cache --virtual build-deps \
        python3-dev \
        gcc \
        libffi-dev \
        musl-dev \
        postgresql-dev

COPY requirements.txt /build/requirements.txt
RUN python3 -m pip install -U pip && CFLAGS="-O0" pip3 install --prefix=/build -r /build/requirements.txt
RUN apk del build-deps

FROM base as main
# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app
RUN apk update && apk upgrade && apk add --no-cache postgresql-dev

COPY --from=builder /build /usr/local
COPY ./src /app

CMD ["gunicorn", "--config", "gunicorn.conf.py", "user_service.wsgi"]

