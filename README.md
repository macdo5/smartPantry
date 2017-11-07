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
5. Open your web browser (Chrome, Firefox or Edge are recommended) and navigate to `localhost:8000` or `127.0.0.1:8000`. The pantry image should load after a few seconds.