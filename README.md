# 📌 Job Application Tracker

A **Flask web app** + **RESTful API** that helps users keep track of job applications and manage them easily — all backed by **Supabase** for secure storage.  
Built for simplicity, speed, and deployment on **Vercel**.

---

## ✨ Features

- 🔐 **User Authentication** with Flask-Login
- 📝 Add, view, and delete job applications
- 🌐 RESTful API (GET, POST, PUT, DELETE)
- 📅 Track application date automatically
- 📱 Responsive UI with HTML, CSS, and JavaScript (no Bootstrap)
- ☁️ Hosted on **Vercel**
- 🗄 Supabase backend (PostgreSQL)

---

## 🚀 API Endpoints

| Method   | Endpoint    | Description              |
| -------- | ----------- | ------------------------ |
| `GET`    | `/job`      | Retrieve all job entries |
| `POST`   | `/job`      | Add a new job            |
| `PUT`    | `/job/<id>` | Update a job by ID       |
| `DELETE` | `/job/<id>` | Delete a job by ID       |

**Example Job JSON:**

```json
{
    "company": "Google",
    "position": "Software Engineer",
    "job_type": "Full-time",
    "location": "Remote"
}


🛠 Tech Stack
Backend: Flask, Flask-RESTful

Database: Supabase (PostgreSQL)

Frontend: HTML, CSS, JavaScript

Hosting: Vercel

Environment: Python 3.12+
```
