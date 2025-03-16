## Context
This is a flask based web-application for manging patient records at a hospital, it allows staff to
    -Add patients to the database
    -View patients in the database
    -Delete patients in the database

## Features
The flask framework handles web routing and db connections. SQLite is used for storing patient records.
Records are stored in database.db and persist between different sessions. Users are able to navigate between pages
with a drop down bar.

## Orginization
The app.py file can be found in the HW3 folder, and is where all connections and functions are defined. Inside
of the templates folder are three html files. Index.html is the landing page of the website, and contains
code for a dropdown menu that will lead to either of the other two html files. Input.html is the form for adding
a new patient. It requires a first and last name to add a patient and displays a table with all the patient
information. Delete.html is the last page that has the opposite function of input.html, but otherwise behaves the
same. Structure is as follows
│-- app.py          # Main Flask application
│-- database.db     # SQLite database (automatically created)
│-- README.md       # This README file
│-- templates/
│   ├── index.html  # Main page with dropdown navigation
│   ├── input.html  # Add patient form
│   ├── delete.html # Delete patient form

## Instructions
To run the code, navigate to the app.py file, and run the file from any IDE or terminal.
A console will pop up with a URL, click it to access the website.