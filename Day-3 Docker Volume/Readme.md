# MySQL with Docker & Persistent Storage on AWS EC2

This project demonstrates how to run a MySQL database inside a Docker container with persistent storage using Docker volumes, hosted on an AWS EC2 instance.

## 🧠 What I Learned

- **Problem with Containers**: By default, data inside a Docker container is lost once the container is stopped or removed.
- **Solution**: Docker Volumes help persist data by mounting a directory from the host to the container.
- **MySQL stores data in**: `/var/lib/mysql` — this is the critical path to mount volumes.

## 💻 Technologies Used

- AWS EC2 (Ubuntu instance)
- Docker
- MySQL (Docker image: `mysql:latest`)
- Docker Volumes

## 🔧 Commands Used

###  Create Docker Volume
```bash
1. docker volume create mysqlvolume

2. Run MySQL Container with Volume Mount

3. Connect to the Container
```

📂 MySQL Setup
```bash
CREATE DATABASE studentDB;
USE studentDB;
CREATE TABLE students (
  name VARCHAR(100),
  rollno INT PRIMARY KEY,
  subject VARCHAR(100)
);
INSERT INTO students (name, rollno, subject) VALUES
('Alice Johnson', 1, 'Math'),
('Bob Smith', 2, 'Science'),
('Charlie Brown', 3, 'English'),
('David Lee', 4, 'History'),
('Eva Green', 5, 'Biology'),
('Frank Wright', 6, 'Chemistry'),
('Grace Kim', 7, 'Physics'),
('Henry Zhao', 8, 'Geography'),
('Isla Moore', 9, 'Computer Science'),
('Jackie Chan', 10, 'Art');
SELECT * FROM students;
```

📂 Docker Volume Insights
```bash
docker volume inspect mysqlvolume
```

## 🧩 Key Takeaways
- Use Docker volumes to avoid data loss in containers.

- Always mount /var/lib/mysql for MySQL containers to persist data.

- Docker volumes are reusable, isolated storage resources managed by Docker.