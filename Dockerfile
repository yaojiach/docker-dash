FROM python:3.7

ENV DASH_DEBUG_MODE True

RUN set -ex && \
    pip install dash dash-daq dash-bootstrap-components

EXPOSE 8050

COPY ./app /app

WORKDIR /app

CMD ["python", "app.py"]
