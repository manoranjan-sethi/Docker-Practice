
# 🐳 Docker Networking Practice

This project explores **Docker networking** by experimenting with bridge, host, and none network modes, along with custom bridge networks to solve container communication issues.

---

## 🔧 Docker Networking Types Covered

### 1️⃣ Default Bridge Network

- Pulled the latest NGINX image:
```bash
  docker pull nginx:latest
```

* Ran NGINX with port forwarding:

  ```bash
  docker run -d --name nginx-container -p 8000:80 nginx:latest
  ```

* Verified container and network:

  ```bash
  docker ps
  docker network ls
  docker inspect nginx-container
  ```

* Created two more containers:

  ```bash
  docker run -d --name first-nginx-container nginx:latest
  docker run -d --name second-nginx-container nginx:latest
  ```

* Tried pinging `first-nginx-container` from inside `second-nginx-container`:

  ```bash
  docker exec -it second-nginx-container bash
  ping <IP-of-first-nginx-container>
  ```

🛑 **Problem:** Containers can't talk using names in default bridge network.

---

### 2️⃣ Custom Bridge Network (🔗 Solution)

* Created a custom bridge:

  ```bash
  docker network create --driver bridge nginx-network
  ```

* Created 3 containers in the same network:

  ```bash
  docker run -d --name third-nginx-container --network nginx-network nginx:latest
  docker run -d --name forth-nginx-container --network nginx-network nginx:latest
  docker run -d --name fifth-nginx-container --network nginx-network nginx:latest
  ```

✅ **Now containers can ping each other using both**:

* IP address
* **Container name**

---

### 3️⃣ Host Network

* Ran a container with host network:

  ```bash
  docker run -d --name sixth-nginx-container --network host nginx:latest
  ```

📝 The container shares **host’s IP**, which means:

* Only one container at a time
* No name-based isolation

---

### 4️⃣ None Network

* Ran container with no network:

  ```bash
  docker run -d --name seven-nginx-container --network none nginx:latest
  docker exec -it seven-nginx-container bash
  ```

🛑 **Result**: No internet access
`apt update` fails due to no DNS or external connectivity:

```
Temporary failure resolving 'deb.debian.org'
```

---

## 📸 Screenshots

> These demonstrate custom bridge networking and container communication tests:

| Custom Network Inspect                                     | Ping with IP and Name                                |
| ---------------------------------------------------------- | ---------------------------------------------------- |
| ![Network Inspect](./Screenshot%202025-06-15%20211659.png) | ![Ping Test](./Screenshot%202025-06-15%20214958.png) |

| No Network Issues                                       |
| ------------------------------------------------------- |
| ![None Network](./Screenshot%202025-06-16%20005502.png) |

---

## 📚 Key Learnings

* Use `docker exec -it <container> bash` to enter container
* Create named custom bridge networks to allow DNS resolution between containers
* Inspect networks with `docker inspect <container/network>`
* Use `--network <name>` to assign a network to containers
* Containers in `none` mode are completely isolated
* `host` network shares IP with the host machine

---

## 🧽 Cleanup

```bash
# Remove container
docker rm -f <container_name>

# Remove network
docker network rm <network_name>
```
---

> 🔗 *This lab helped me understand practical Docker networking with real container-to-container communication scenarios and debugging.*

