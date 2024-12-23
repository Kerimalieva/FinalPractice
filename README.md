# Notes Project

## Overview
The Notes project is a web application built to provide users with an intuitive and secure platform for creating, managing, and organizing notes. Users can add, edit, and delete notes with photos, making it a practical tool for both personal and professional use.

## Features

### 1. User Functionality
- **User Authentication**:
  - Register and log in securely using JWT (JSON Web Tokens).
  - Password reset functionality with confirmation via a secure link.
- **Note Management**:
  - Add, edit, and delete notes.
  - Upload and manage photos related to notes.

### 2. Deployment
- The application is deployed on a remote server, making it accessible online.
- Configured to ensure high availability and cross-device compatibility.

### 3. Security
- **Authentication**:
  - Implemented secure login and JWT-based authentication.
- **Data Protection**:
  - Password encryption.
  - Protection of user-uploaded content (e.g., photos).

### 4. Performance Optimization
- Optimized application speed and load times.
- Ensured responsiveness for seamless performance across various devices.

## Technical Stack

### Backend
- **Framework**: Django 5.1.4
- **REST API**: Django REST Framework (DRF), Djoser for authentication.
- **Database**: SQLite (default setup, easily replaceable for production).

### Frontend
(Not included in this example, assuming API-focused backend development.)

### Deployment
- Deployed on a remote server.
- Configured for scalability and security.

#### Deployment Details
- **Website URL**: [185.39.79.88:8080](http://185.39.79.88:8080)
- **Admin Credentials**:
  - **Username**: `admin`
  - **Password**: `admin`

#### API Endpoints

##### Authentication
- `POST /api/auth/users/`: Register a new user.
- `POST /api/token/`: Obtain a JWT token.
- `POST /api/token/refresh/`: Refresh a JWT token.
- `POST /api/token/password_reset/`: Reset the user password.

##### Notes
- `GET /api/posts/`: List all notes.
- `GET /api/posts/<id>/`: Retrieve a specific note.
- `POST /api/posts/create/`: Create a new note.
- `PUT /api/posts/<id>/update/`: Update a note.
- `DELETE /api/posts/<id>/delete/`: Delete a note.

