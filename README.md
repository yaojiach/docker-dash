# Docker Dash (Plotly)

### Switch debug in mode in Dockerfile

```dockerfile
ENV DASH_DEBUG_MODE True # False
```

### Build and run

```sh
docker build -t dash . && docker run --rm -p 8050:8050 dash
```
