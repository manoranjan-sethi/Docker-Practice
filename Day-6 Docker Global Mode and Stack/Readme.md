
# 🐳 Docker Day 6 – Global Mode & Stack Deployment

This project documents my learning and practice of deploying services in **Docker Swarm** using both **global mode** and a **Docker Stack YAML file** to manage multiple services efficiently.

---

## 🌍 Global Mode Deployment

Global mode ensures that **one container runs on each node** in the Swarm.

### ✅ Command Used:
```bash
sudo docker service create --name nginx-service --mode global -p 80:80 nginx:latest
````

### 🧠 Why use Global Mode?

* Useful for services that need to run on **every node** (e.g., log collectors, monitoring agents).
* Automatically scales based on the number of nodes in the cluster.

---

## 📦 Docker Stack File Deployment

Instead of manually creating services one by one, I defined them in a **YAML configuration file** to streamline deployment.

### 📄 Stack File: `firststack.yaml`

```yaml
version: '3.8'

services:
  mysql-service:
    image: mysql:latest
    container_name: mysql-container
    environment:
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
    deploy:
      replicas: 3

  ngnix-service:
    image: nginx:latest
    container_name: nginx-container
    ports:
      - "8080:80"
```

### 🚀 Deploy the Stack

```bash
sudo docker stack deploy -c firststack.yaml mystack
```

> `mystack` is the name of the stack. Docker creates an overlay network and deploys services accordingly.

### 🔍 View Running Tasks

```bash
sudo docker stack ps mystack
```

---

## 📸 Screenshots

* **Stack file creation & push to GitHub**

![Stack File in VSCode](./Screenshot%202025-07-16%20234134.png)

* **Stack deployment output**

![Stack Deploy Output](./Screenshot%202025-07-16%20234022.png)

* **Service distribution across Swarm nodes**

![Stack Services Running](./Screenshot%202025-07-16%20233641.png)

---

## 🧠 Key Learnings

* **Global Mode** ensures that exactly one container is scheduled per node.
* **Stack files** allow you to manage multiple services declaratively.
* Using `stack deploy` simplifies **multi-service orchestration** in Swarm.
* All configuration is **centralized**, **version-controlled**, and **reusable**.

---

## 🚀 Next Steps

* Add volumes and configs to stack files
* Integrate health checks for services
* Explore inter-service networking with stack-level networks

---

## 📌 Connect

Follow my DevOps journey on [LinkedIn](https://linkedin.com/in/manoranjan-sethi)

\#Docker #SwarmMode #DockerStack #DevOps #GlobalMode #Yaml #AWS #Cloud #Linux #100DaysOfDevOps #ContainerOrchestration

