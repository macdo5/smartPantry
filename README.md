# Smart Pantry Web App  
This tutorial will show you how to get the Smart Pantry Web App working on your server. Before you get started, make sure you have rudimentary knowledge of [Git](https://try.github.io/levels/1/challenges/1 "Git Tutorial"), [Python](https://www.python.org/about/gettingstarted/ "Getting started with Python"), and [Django](https://tutorial.djangogirls.org/en/ "Django Girls tutorial"). Django Girls have a wonderful tutorial that covers Python, Git and Django and other things in their website.
1. First, clone this repository to your machine.
3. Now to activate the virtual environment. On the command line, go to smartPantry/pantryWebVenv/bin. If you are using Windows, enter `activate`. If you are using Linux/OS type `source activate`.
4. Go back to smartPantry/ and enter `python manage.py runserver`. If everything goes well, you should see this:
```
Performing system checks...

System check identified no issues (0 silenced).
November 06, 2017 - 15:38:31
Django version 1.11.5, using settings 'smartPantry.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
5. Open your web browser (Chrome, Firefox or Edge are recommended) and navigate to `localhost:8000` or `127.0.0.1:8000`. There is currently a default pantry already in the datatbase called myPantry. It has 1 row and 10 columns. The Django views and templates are built to display this single pantry only. In future development this will change so that every user will be able to view their own pantry. The pantry image should load after a few seconds.

The reason why it takes so long to load is because it is constructing a single .jpg out of multiple images. There are 10 pictures that the web app needs to stitch together, so the more columns and rows in a pantry and the higher the resolution of the pictures, the longer it takes for the web app to stitch them all together.
