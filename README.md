# Project 1: Movie Trailer Website
### by Fabio Derendinger

Movie trailer website project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Demo

For a demo, check out <https://fabioderendinger.github.io/movie-website/>

## What it is and does

Server-side python script to store a list of my favorite movies, including box art imagery, movie trailer URL and additional metadata. This data is served as a webpages (index.html) dynamically generetated by the python script.

## Required Libraries and Dependencies

- Python 2.x is required to run this project

## Project contents

In it's core, the project consists of the following files:

* generate_movie_page.py - main Python script to run
* media.py - contains the definition of the class Movie (used to create instances of movies)
* fresh_tomatoes.py - creates the HTML file for the website
* css folder - contains materialize framework files and a custom css file (style.css)
* js folder - contains materialize framework files and a custom js file (functions.css)

## How to Run Project

Download the project zip file to you computer and unzip the file. Or clone this
repository to your desktop.

Run the Python file "generate_movie_page.py".

Your default browser should launch a new tab displaying the movie trailer website.

## Extra Credit Description

The following features were implemented to gain an extra credit from Udacity:

* Added storyline and additional metadata of the movie to the website
* Complete re-design of the frontend to achieve a modern, neat touch
* Carousel-like component to select a movie, preview of movie info

## Miscellaneous

This README document is based on a template suggested by PhilipCoach in this
Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).
