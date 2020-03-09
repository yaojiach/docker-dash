# Docker Dash (Plotly)

Dockerize a Python Dash app for quick prototyping.

## Switch debug mode in Dockerfile

```dockerfile
ENV DASH_DEBUG_MODE True # False
```

## Build and run

```sh
docker build -t dash . && docker run --rm -p 8050:8050 dash
```

## Access the page

Go to `http://0.0.0.0:8050/` in browser.
