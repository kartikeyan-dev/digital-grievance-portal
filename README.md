 Digital Public Grievance Portal (AI-Powered Full Stack System)

A production-style grievance management system that leverages Machine Learning to automatically classify complaints and assign priority levels. Built to simulate a real-world civic issue tracking platform with admin workflows, analytics, and SLA-based resolution tracking.
Designed for scalability, transparency, and intelligent automation of public grievance handling.

 Key Features

AI-Powered Complaint Classification
  - Automatically predicts complaint category (Water, Road, Electricity, etc.)
  - Assigns priority level (High / Medium / Low)

Complaint Management System
  - Unique complaint ID generation
  - Structured complaint submission workflow

Admin Control Panel
  - View, assign, and update complaint status
  - Workflow management: Pending → In Progress → Resolved

SLA-Based Tracking
  - Priority-based resolution timelines
  - Tracks overdue and pending cases

Notification System
  - Real-time updates stored in MongoDB
  - Status change alerts for users

Analytics Dashboard
  - Status distribution (Pie Chart)
  - Category distribution (Bar Chart)
  - Built using Chart.js

 AI & Technical Highlights

- Text classification model for complaint categorization
- Priority prediction logic based on complaint severity
- Lightweight ML pipeline integrated with Flask backend
- Structured data preprocessing for complaint text
- Scalable design for future model upgrades (NLP / LLM integration ready)


 Tech Stack

Backend
- Flask (Python)
- Jinja2 Templates

Database
- MongoDB (NoSQL document storage)

Frontend
- HTML5, CSS3
- Bootstrap (Responsive UI)
- Chart.js (Data Visualization)

AI/ML
- Python-based classification model (custom pipeline)


System Architecture

User
↓
Complaint Submission Form
↓
Flask Backend (API Layer)
↓
AI Model (Category + Priority Prediction)
↓
MongoDB Database Storage
↓
Admin Dashboard (Status Management)
↓
Notification Engine
↓
Analytics Dashboard (Chart.js)



 Project Structure
 Digital-Public-Grievance-Portal/
│
├── app.py
├── requirements.txt
├── config.py
│
├── /models
│ └── ai_classifier.pkl
│
├── /templates
│ ├── index.html
│ ├── submit_complaint.html
│ ├── admin_dashboard.html
│ ├── analytics.html
│
├── /static
│ ├── /css
│ ├── /js
│ └── /images
│
├── /utils
│ ├── prediction.py
│ ├── db.py
│
└── README.md

  Future Enhancements
Integration of LLMs for smarter complaint understanding
SMS / Email notification system
Role-based authentication (User / Admin / Officer)
Geo-tagging of complaints with map visualization
Microservices-based backend architecture
Mobile app support (React Native / Flutter)

Live Demo
https://digital-grievance-portal.onrender.com


Author
Kartikeyan Dev

GitHub: https://github.com/kartikeyan-dev
Project: Digital Public Grievance Portal

⭐ If you like this project
Give a star ⭐ on GitHub to support development.
