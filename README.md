# 🗳️ JanVote Portal – Secure Online Voting System

A full-stack secure online voting platform built using Flask, MySQL, HTML, CSS, JavaScript, and Bootstrap.

This project simulates a real-world government election management and voter verification workflow system with multi-department approval architecture.

---

# 🚀 Features

## 👤 Public Module
- Home page
- About page
- Notices
- FAQ
- Contact page
- Election results
- Public voter registration

---

## 🪪 Voter Registration Workflow
- New voter registration form
- Document upload system
- Identity proof upload
- Photo upload
- Workflow-based application processing

---

## 🏢 Multi-Department Verification Workflow

### Workflow Architecture

```text
Public User
    ↓
Administration Department
    ↓
Verification Department
    ↓
Approval / Rejection
    ↓
Voter ID Generation
```

### Features
- Administration review queue
- Verification department queue
- Application forwarding
- Workflow stages
- Department-based processing

---

## 🔐 Authentication System
- User registration
- Login/logout
- Password hashing
- Session management
- Flask-Login integration
- OTP verification system

---

## 🗳️ Election Management
- Create elections
- Manage candidates
- Election scheduling
- Candidate assignment
- Voting engine

---

## 📊 Voting System
- Secure vote casting
- Duplicate vote prevention
- OTP vote verification
- Real-time result counting

---

## 📈 Results Dashboard
- Election analytics
- Winner calculation
- Vote percentages
- Chart.js integration

---

# 🧱 Tech Stack

## Backend
- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-Mail

## Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## Database
- MySQL

## Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
secure_online_voting_system/
│
├── app/
│   ├── admin/
│   ├── auth/
│   ├── department/
│   ├── models/
│   ├── public/
│   ├── voter/
│   ├── static/
│   └── templates/
│
├── migrations/
├── venv/
├── .env
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

# 🗄️ Database Architecture

## Main Tables
- users
- voter_applications
- department_officers
- elections
- candidates
- votes

---

# 🔄 Workflow Management

The system uses a multi-stage workflow architecture.

## Workflow Stages
- Submitted
- Admin Review
- Forwarded To Verification
- Verification In Progress
- Approved
- Rejected
- Voter ID Generated

---

# 🔒 Security Features

- Password hashing
- Session authentication
- OTP verification
- Role-based access control
- Duplicate vote prevention
- Protected routes
- Secure file uploads

---

# 🧩 Flask Architecture

The application uses:
- Flask Blueprints
- Template Inheritance
- Modular Structure
- App Factory Pattern

---

# 🎨 Frontend Architecture

## Template Hierarchy

```text
base.html
    ↓
public_base.html
admin_base.html
voter_base.html
    ↓
individual pages
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/secure_online_voting_system.git
```

---

## 2️⃣ Navigate to Project

```bash
cd secure_online_voting_system
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Configure Environment Variables

Create `.env`

```env
SECRET_KEY=your_secret_key

DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=janvote_db

MAIL_USERNAME=your_email
MAIL_PASSWORD=your_email_password
```

---

## 7️⃣ Create Database

Inside MySQL:

```sql
CREATE DATABASE janvote_db;
```

---

## 8️⃣ Run Database Migrations

```bash
flask db init

flask db migrate -m "Initial migration"

flask db upgrade
```

---

## 9️⃣ Run Application

```bash
flask run
```

---

# 📌 Future Improvements

- Biometric verification
- Aadhaar integration
- Face recognition
- Blockchain vote ledger
- Docker deployment
- REST APIs
- Real-time notifications
- Audit logging system
- Constituency-based election filtering

---

# 📷 Screenshots

## Public Homepage
(Add Screenshot)

## Voter Registration
(Add Screenshot)

## Admin Dashboard
(Add Screenshot)

## Voting Dashboard
(Add Screenshot)

---

# 👨‍💻 Developer

**Jaswanth Krishna**

Computer Science Undergraduate  
Passionate about:
- Full Stack Development
- Cybersecurity
- Workflow Systems
- Data Science
- Cloud Technologies

---

# 📜 License

This project is developed for educational and portfolio purposes.
