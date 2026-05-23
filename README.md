# 🏟️ Sports Complex Booking System (SCBS)

A full-stack web-based booking and management system for sports facilities built using Flask and SQLite. The system supports user reservations, admin management, email notifications, and activity tracking.

---

## ✨ Features

### 👤 User Features
- User registration and login (authentication system)
- Profile management
- Facility browsing and booking
- Reservation tracking
- Inquiry submission
- Chatbot support (AI/FAQ assistant)
- Password-secured sessions

---

### 🧑‍💼 Admin Features
- Admin login authentication
- Dashboard overview
- Manage users
- Manage categories (sports/facilities)
- Manage facilities
- Manage reservations
- Manage inquiries
- View transaction logs
- System settings management
- History log tracking (activity monitoring)

---

### 📩 System Features
- SMTP Email Notifications:
  - Booking confirmations
  - Reservation updates
  - User-related notifications
- Real-time data handling using SQLite
- Logging system for user/admin actions
- Modular backend structure (fetch & service-based files)

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Flask (Python)  
- Database: SQLite (`database.db`)  
- Email Service: SMTP (`email_notifications.py`)  
- Templating Engine: Jinja2  

---

## 📁 Project Structure
SCBS-Flask/
│
├── app.py
├── config.py
├── chatbot.py
├── database.db
├── insert_dummy.py
│
├── create_reservation.py
├── email_notifications.py
├── history_logger.py
│
├── fetch_users.py
├── fetch_reservations.py
├── fetch_facility.py
├── fetch_categories.py
├── fetch_inquiries.py
│
├── static/
│ ├── images/
│ ├── uploads/
│
├── templates/
│
│ ├── index.html
│ ├── profile.html
│ │
│ ├── auth/
│ │ ├── login.html
│ │ ├── admin-login.html
│ │
│ ├── admin/
│ │ ├── dashboard.html
│ │ ├── users.html
│ │ ├── categories.html
│ │ ├── facilities.html
│ │ ├── reservations.html
│ │ ├── inquiries.html
│ │ ├── settings.html
│ │ ├── history-log.html
│ │ ├── transaction-log.html
│
└── README.md
