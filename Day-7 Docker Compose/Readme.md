

# 🐳 Docker Day 7 – Docker Compose: Node.js + Redis + NGINX

On Day 7 of my Docker journey, I explored **Docker Compose** using a real-world multi-container project from Docker’s official open-source repository.

📂 **Project Repo**:  
[awesome-compose/nginx-nodejs-redis](https://github.com/docker/awesome-compose/tree/master/nginx-nodejs-redis)

---

## 🧠 What is Docker Compose?

Docker Compose lets you **define and manage multi-container applications** using a single `docker-compose.yml` file.

It is especially useful for:

- **Development and testing environments**
- Spinning up **entire service stacks** with one command
- Abstracting container complexities for developers

---

## ⚙️ Services Used in This Project

The `docker-compose.yml` defines the following services:

| Service | Description |
|---------|-------------|
| `web1`  | Node.js app container |
| `web2`  | Another Node.js app container |
| `redis`| Redis key-value store to persist visit counters |
| `nginx`| Reverse proxy and load balancer to distribute requests between web1 and web2 |

---

## 🚀 How to Run

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/docker/awesome-compose.git
   cd awesome-compose/nginx-nodejs-redis

2. **Start the App Stack**:

   ```bash
   sudo docker compose up
   ```

> This will launch all 4 containers defined in the Compose file.

---

## 📊 Application Behavior

* The NGINX container **load balances** incoming requests between `web1` and `web2`.
* Each time you refresh the webpage, the **visit count increases**.
* Redis is used as a **persistent cache** to track the number of visits across containers.

---

## 🖥️ Running Containers

Expected containers upon running the app:

```
nginx-nodejs-redis-web1-1
nginx-nodejs-redis-web2-1
nginx-nodejs-redis-redis-1
nginx-nodejs-redis-nginx-1
```

You can verify them using:

```bash
sudo docker ps
```

---

## 🧠 Key Learnings

* Docker Compose simplifies multi-container orchestration with a single YAML file.
* Perfect for developers unfamiliar with Docker CLI — **write once, run many**.
* Services can communicate over a **default network**, and Compose handles **build context, ports, and volumes**.
* Redis is used to **persist data between containers**, preventing stateless resets.

---

## 📌 Connect

Follow my Docker DevOps journey on [LinkedIn](https://linkedin.com/in/manoranjan-sethi)

