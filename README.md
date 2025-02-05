# Mapping the Valor

[View live project here on Heroku](https://mapping-the-valor-a17b7cc98edf.herokuapp.com/)

<br>


## CONTENTS

* [Concept](#concept)
* [Project Planning](#project-planning)
  * [Wireframes](#wireframes)
  * [Project Board](#project-board)
  * [Styling Choices](#styling-choices)
* [Features for MVP](features-for-mvp)
<p align="right"><a href="#mapping-the-valor">Back To Top</a></p>
<br>

## Project Directory Structure

```
your_project/
│
├── your_app/                   # Your Django app containing project logic
│   ├── migrations/             # Django migration files (auto-generated)
│   ├── models/                 # Directory for all model files
│   │   ├── __init__.py         # Imports all models for easy access
│   │   ├── institution.py      # Models related to institutions, religious orders, house types
│   │   ├── land.py             # Models for land holdings and land types
│   │   ├── role.py             # Models for roles, offices (monastic, cathedral, parish)
│   │   ├── county.py           # County model (for geographic records)
│   │   ├── monetary.py         # Models for monetary values (pounds, shillings, pence)
│   │   ├── valor_record.py     # Models for Valor record-related data (institution records, dates, etc.)
│   │   └── other_models.py     # Any other models not fitting into other categories
│   ├── admin.py                # Django admin configuration (register models for admin view)
│   ├── views.py                # Views for business logic (handling requests and rendering responses)
│   ├── urls.py                 # URL routes for your app
│   ├── forms.py                # Django forms (if applicable)
│   ├── tests.py                # Unit tests for models and views
│   ├── templates/              # Templates for rendering HTML views
│   │   ├── your_template.html  # Example HTML template
│   └── static/                 # Static files (CSS, JavaScript, images)
│       ├── your_app/           # App-specific static files (for modular organization)
│       │   ├── css/            # Stylesheets specific to your app
│       │   ├── js/             # JavaScript files for your app
│       │   └── images/         # Image files for your app
│       ├── css/                # Global static files (stylesheets shared across the project)
│       ├── js/                 # Global JavaScript files (shared libraries like jQuery)
│       └── images/             # Global images (logos, icons, etc.)
├── static/                     # Base-level static folder for global files
│   ├── css/                    # Global CSS styles
│   ├── js/                     # Global JS libraries (e.g., Leaflet, jQuery)
│   └── images/                 # Global images (icons, logos)
├── templates/                  # Global templates (for layout/base.html, etc.)
│   └── base.html               # Base template shared across all views
├── db.sqlite3                  # SQLite database file (if using SQLite for development)
├── manage.py                   # Django management command file
├── requirements.txt            # Python dependencies (generated via `pip freeze`)
├── .gitignore                  # Git ignore file (ignores unnecessary files from being tracked)
└── README.md                   # Project description and setup instructions
```

[🔼 Back to top](#mapping-the-valor)

---

## Concept

<br>

This project is to fulfil the requirements of the Capstone project with CodeInstitute.
The idea for the project is to provide a space for research and interaction for site users who have an interest in the history of England.
By selecting the monasteries as a defined list of items, and encouraging users to add information to the database, the project aims to achieve the CRUD features of this full stack web application.

[🔼 Back to top](#mapping-the-valor)

---

### What is the Valor?

The Valor, or to give it its full name, the 'Valor Ecclesiasticus' is a comprehensive record of all the church held lands in England and Wales on the eve of the Reformation. 
It is a document which gives a fascinating insight into land ownership, local and national economy, and the social geography of sixteenth century England and Wales.
It is, in a very real sense, a census document of value alongside that of the Domesday Book of 1086.

Although the texts are accessible to the public through the national libraries, they remain untranslated and thoroughly inaccessible to all but the most dedicated of historians.
Remaining untranslated from its 16th century Latin, and printed in the 19th century as a multi-volume tome of lists, the aim of this project is to generate interest in this work and make it accessible to contemporary viewers.



[🔼 Back to top](#mapping-the-valor)

---

<br>

## User Experience


## Technology Used

#### Languages, Frameworks, Editors & Version Control:

* HTML, CSS, JS & Python
* Django
* Bootstrap
* Leaflet.js
* Github
* Heroku

<p align="right"><a href="#mapping-the-valor">Back To Top</a></p>

#### Tools Used

* PostgreSQL
* WhiteNoise
* Google Chrome Dev Tools
* (Balsamiq)
* FontAwesome
* (Google Fonts)
* Google Sheets
* 
<p align="right"><a href="#mapping-the-valor">Back To Top</a></p>

## Database

#### Database Schema

## Features

#### Future Features

## Testing

#### Found Bugs & Fixes

## Deployment

## Credits








