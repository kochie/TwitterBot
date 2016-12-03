# TwitterBot
AI that simulates someone using their tweets

# Outline
- [ ] Create Django App
- [ ] Obtain Twitter API access
- [ ] Obtain TensorFlow API access
- [ ] Build database in Django (create Schema)
- [ ] Connect database to twitter API

# MVP Concepts
- Create simple Twitter app that grabs a users tweets and adds them to a database.
- Build TensorFlow App and connect that to TwitterBot.

# Aim
To create an MVP app that uses the Twitter API to 'clone' a person via their tweets and build a chatbot using TensorFlow based on their persona.

# Materials
- Django
- React
- Twitter API
- TensorFlow API

# Method
1. So the first step is to create a Django webserver on the local machine, since this is slightly different in each operating system the rest of this document will assume that we are using a Mac with macOSX Sierra installed.
  - Following the instructions on the [Django Website](https://docs.djangoproject.com/en/1.10/topics/install/#installing-official-release).
  - It is highly recommended to install Django with [virtualenv](https://virtualenv.pypa.io/en/stable/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) if it is compatable with the local machine.
  - This installation guide will assume that the current installed python version is Python 3.5

2. One advantage to Django is that it's super easy to make microframeworks so using this stratery we can make several smaller applications that do specific things.
  - One server can handle the Twitter API and add tweets to a centralized data

# Brief
## TensorFlow
http://lauragelston.ghost.io/


