# SenpaiLog

SenpaiLog is a full-stack web application that allows users to explore, track, and manage anime, manga, and manhwa in one place. Users can log what they are watching or reading, track progress, and interact with an AI-powered chatbot for information and recommendations.

SenpaiLog is built using a production-ready backend stack with Django, PostgreSQL, Docker, and Gunicorn.

---

# Features

## Content Browsing

* Browse Anime, Manga, and Manhwa
* View detailed information including:

  * Title
  * Description
  * Rating
  * Release Year
  * Episodes / Chapters
  * Cover Image
* Sorted from latest to oldest
* Pagination support for performance

---

## User Authentication

* User registration
* Secure login and logout
* User-specific tracking system

---

## Tracking System

Users can log content with status:

* Watching
* Completed
* Plan to Watch / Read

Each user has a personal dashboard showing their tracked content.

---

## User Dashboard

Dashboard allows users to:

* View Watching list
* View Completed list
* View Planned list
* Manage tracked content

---

## AI Chatbot (Planned Feature)

Integrated chatbot to answer questions such as:

* "What is Naruto about?"
* "Suggest anime like Death Note"
* "Is Attack on Titan completed?"

Future versions will include AI-powered recommendations.

---

# Tech Stack

## Backend

* Python
* Django
* Django REST Framework
* PostgreSQL
* Gunicorn

## Frontend

* HTML
* CSS
* Bootstrap
* Django Templates

## DevOps

* Docker
* Docker Compose

## AI Integration (Planned)

* OpenAI API

---

# Project Structure

```
senpailog/

├── docker/
├── config/
│
├── apps/
│   ├── users/
│   ├── anime/
│   ├── manga/
│   ├── manhwa/
│   ├── chatbot/
│
├── templates/
├── static/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
```

---

# Installation

## Clone the repository

```
git clone https://github.com/yourusername/senpailog.git
cd senpailog
```

## Run using Docker

```
docker-compose up --build
```

---

# Future Improvements

* AI-powered recommendation system
* Advanced search and filters
* React frontend
* Cloud deployment
* User profile customization

---

# Goals of This Project

SenpaiLog is built to:

* Practice backend engineering with Django
* Work with PostgreSQL database design
* Learn Docker and production deployment
* Implement real-world authentication systems
* Integrate AI features into web applications
* Build a production-level portfolio project

---

# Author

Rikim Rana

Backend Developer | AI Enthusiast
