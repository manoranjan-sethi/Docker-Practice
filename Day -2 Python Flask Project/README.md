# Day -2 — Python Flask Project 🚀

Simple Flask application used for Docker practice. The app exposes two routes and runs on port `5000`.

---

## Quick start

### Run locally (venv)

1. Create & activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies and start the app:

```bash
pip install -r requirements.txt
python app.py
```

3. Open in browser or curl:

- http://localhost:5000/info
- http://localhost:5000/login

Example:

```bash
curl http://localhost:5000/info
# => <h1>Good Morining from Docker!</h1>
```

---

### Run with Docker

Build the image and run a container:

```bash
docker build -t day2-flask .
docker run --rm -p 5000:5000 day2-flask
```

Then visit `http://localhost:5000/info` or `http://localhost:5000/login`.

---

## What this repository contains

- `app.py` — minimal Flask application
- `requirements.txt` — Python dependencies (`flask`)
- `Dockerfile` — Docker image definition

---

## Endpoints

- `GET /info` — returns `<h1>Good Morining from Docker!</h1>`
- `GET /login` — returns `<h1>Login Page of Docker!</h1>`

---

## Dockerfile (summary)

- Base image: `python:3.14.0a7-slim`
- Copies app files into `/flaskapp`
- Installs `requirements.txt`
- Runs `python app.py`

Tip: if `python:3.14.0a7-slim` is not available on your system, replace with a stable tag such as `python:3.11-slim`.

---

## Troubleshooting & tips 💡

- If port `5000` is in use, change the published port in `docker run -p <host_port>:5000`.
- To enable auto-reload during development consider running with `flask run` and `FLASK_ENV=development` or use a tool such as `watchdog`.

---

## License

Open for learning and experimentation.
