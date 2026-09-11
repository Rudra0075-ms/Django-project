# 🎓 Student Management System

### 🌐 [Live Demo](https://student-management-app-2026.netlify.app/)

A full-stack **Student Management System** built with **Python and Django** for managing student records through a clean web interface.

The application provides authentication, CRUD operations, search, sorting, pagination, validation, and a dashboard for managing student information efficiently.

---

## 🚀 Features

### 🔐 Authentication

* User Signup
* User Login
* User Logout
* Authentication-protected pages
* Session-based user management

### 👨‍🎓 Student Management

* Add new students
* View student records
* Edit existing student details
* Delete students
* Search students
* Sort student records
* Paginate large student lists

### 📊 Dashboard

* Student overview
* Quick access to student records
* Organized management interface
* User-friendly navigation

### 🛡️ Validation & Security

* Server-side form validation
* CSRF protection using Django
* Authentication checks
* Secure form handling
* Django's built-in security features

---

## 🛠️ Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| 🐍 Python  | Backend programming  |
| 🌐 Django  | Web framework        |
| HTML5      | Page structure       |
| CSS3       | Styling              |
| SQLite     | Database             |
| Git        | Version control      |
| GitHub     | Source code hosting  |
| Netlify    | Deployment / hosting |

---

## 🏗️ Application Architecture

```text
User
 │
 ▼
Django Templates
 │
 ▼
Django Views
 │
 ├── Authentication
 ├── Student CRUD
 ├── Search & Sorting
 ├── Pagination
 └── Dashboard
 │
 ▼
Django Models
 │
 ▼
SQLite Database
```

The project follows Django's **MVT (Model–View–Template)** architecture.

---

## 📂 Project Structure

```text
Student_Management_System/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── requirements.txt
├── db.sqlite3
└── README.md
```

> The exact folder structure may differ depending on the current project implementation.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rudra0075-ms/Student_Management_System.git
```

### 2. Navigate to the project

```bash
cd Student_Management_System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create an admin account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🗄️ Database

The project currently uses **SQLite** for data storage.

Student information is managed through Django models and Django's ORM, allowing the application to perform:

* Create
* Read
* Update
* Delete
* Search
* Sort
* Filter

operations without writing raw SQL for normal database operations.

---

## 🔎 Student Search & Management

The system allows users to quickly find and manage student records.

Example workflow:

```text
Dashboard
   ↓
Student List
   ↓
Search / Sort
   ↓
View Student
   ├── Edit
   └── Delete
```

Pagination keeps the student list manageable when the number of records increases.

---

## 📊 Dashboard

The dashboard acts as the central management page where users can access student information and navigate between the major features of the application.

---

## 🔐 Security

The project takes advantage of Django's built-in security mechanisms, including:

* CSRF protection
* Authentication middleware
* Password hashing
* Session management
* Form validation
* Django ORM protection against common SQL injection patterns

For production deployment, sensitive configuration such as `SECRET_KEY`, database credentials, and API keys should be stored using **environment variables** rather than committed to GitHub.

---

## 🚀 Deployment

The project is deployed online and can be accessed here:

### 🌐 [Open Student Management System](https://student-management-app-2026.netlify.app/)

> **Note:** Django is primarily a server-side framework. A production Django application normally requires a Python-capable backend host such as Render, Railway, PythonAnywhere, AWS, etc. Netlify is primarily designed for static sites/serverless workloads, so Django deployment on Netlify requires an appropriate serverless/backend configuration.

---

## 🧪 Future Improvements

The current system can be extended with more production-level functionality:

* 📸 Student profile pictures
* 📧 Email notifications
* 📄 Export students to CSV/PDF
* 📊 Advanced analytics
* 🔍 Advanced filtering
* 👥 Role-based access control
* 👨‍🏫 Teacher management
* 📚 Course management
* 🎓 Attendance management
* 📝 Marks and grade management
* 🔔 Notification system
* 🌐 REST API using Django REST Framework
* 🐘 PostgreSQL for production database
* 🐳 Docker support
* 🔄 CI/CD with GitHub Actions
* ☁️ Production deployment

---

## 📌 Learning Outcomes

Through this project, I practiced:

* Django MVT architecture
* CRUD operations
* Django models and ORM
* Forms and validation
* User authentication
* URL routing
* Templates
* Static files
* Database migrations
* Search and sorting
* Pagination
* Git & GitHub
* Web application deployment

---

## 👨‍💻 Author

**Madhab**

B.Tech CSE — AI & ML

Interested in **Python, Django, Backend Development, AI/ML, Automation and Real-World Projects.**

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📜 License

This project is created for **educational and learning purposes**.
