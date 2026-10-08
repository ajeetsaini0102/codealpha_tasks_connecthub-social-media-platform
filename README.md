# ConnectHub - Social Media Platform

ConnectHub is a Django-based social media platform developed as a learning project. It allows users to create accounts, manage profiles, share posts, comment, like posts, and follow other users.

 🌐 [Live Demo](https://connecthub-social-media-platform.onrender.com/login/?next=/)

## Features

* User Registration
* User Login and Logout
* User Profile
* Profile Image Upload
* Create Posts
* Home Feed
* Like / Unlike Posts
* Persistent Like Status
* Comments on Posts
* Follow / Unfollow Users
* Find People Page
* Followers and Following Count
* Django Admin Panel
* SQLite Database for local development
* Separate HTML, CSS and JavaScript files
* Responsive UI

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Django

### Database

* SQLite

### Other

* Git
* GitHub
* Django Static Files
* Django Media Files

## Project Structure

```text
ConnectHub/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── social/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── create_post.html
│   │   ├── users.html
│   │   └── navbar.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── Pipfile
└── .gitignore
```

## Database Models

The project contains the following main models:

### Profile

Stores additional information about users, including profile image and bio.

### Post

Stores posts created by users.

### Comment

Stores comments made on posts.

### Like

Stores likes given by users to posts.

### Follow

Stores follower and following relationships between users.

## Installation

Clone the repository:

```bash
git clone https://github.com/ajeetsaini0102/connecthub-social-media-platform.git
```

Move into the project folder:

```bash
cd connecthub-social-media-platform
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install django pillow
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Admin Panel

To create a Django superuser:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## How the Application Works

1. A new user registers an account.
2. The user logs in using their username and password.
3. After login, the user can view the home feed.
4. Users can create new posts.
5. Other users can like and comment on posts.
6. Users can find other registered users.
7. Users can follow or unfollow other users.
8. Users can open their profile and upload a profile image.
9. The application stores the data in the Django database.

## Learning Goals

This project was created to practice and understand:

* Django project and app structure
* Django models and database relationships
* Django authentication
* CRUD concepts
* Django templates
* Template inheritance/includes
* Static and media files
* HTML, CSS and JavaScript integration
* Git and GitHub
* Basic social media application architecture

## Future Improvements

Possible future enhancements include:

* Edit Profile
* Edit and Delete Posts
* Delete Comments
* Followers and Following Lists
* Notifications
* Search Users
* Better responsive design
* PostgreSQL database for production
* Cloud storage for uploaded media
* Deployment on Render

## Author

**Ajit Singh Saini**

This project was developed for learning and practice purposes.
