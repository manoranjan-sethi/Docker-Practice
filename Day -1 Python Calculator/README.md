# 🐳 Day 1 - Dockerized Terminal Calculator App

This repository contains a simple terminal-based calculator app written in Python and containerized using Docker. It marks Day 1 of my "Learning Docker in Public" journey.

## 🧮 App Functionality

The calculator supports the following operations:

- Addition
- Subtraction
- Multiplication
- Division (with zero-division check)

All interactions happen through the terminal, making it a perfect use case to explore Docker's interactive container capabilities.

## 📁 Files

- `calculator.py` – Python CLI calculator script
- `Dockerfile` – Instructions to build a Docker image for the app

## 🐳 Docker Instructions

### 🔨 Build the Docker Image

```bash
docker build -t terminal-calculator .
```

### 🔨 Run the Container (with interactive terminal)

```bash
docker run -it terminal-calculator
```

### 🐳 Want to pull image from docker Hub

```bash
docker pull spartan0007/calculator:1.0
```
