# Docker Dash (Plotly)

Dockerize a Python Dash app for quick prototyping.

## Build and run

```sh
docker build -t docker-dash-example .

docker run -p 8050:8050 -v "$(pwd)"/app:/app --rm docker-dash-example
```

## Access the page

Go to `http://localhost:8050` in browser.

## Switch debug mode in Dockerfile

```dockerfile
ENV DASH_DEBUG_MODE True # False
```

## Development

Install the app requirements for development to get better editor support.

```sh
poetry install
```

Optional: clean initialization of `poetry`:

```sh
poetry init
cat app/requirements.txt | xargs poetry add
```
