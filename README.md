# Commodity Food Prices
This project attempts to gather commodity food prices data from each distribution node, e.g. production (farmers), distributors (marketing agent), merchant in market, etc. through SMS based app. The collected data is then further processed to create daily visualization/trends and predict future prices using our defined prediction model.

* The project is developed in hackathon for 70th birthday of Indonesia: http://hackathonmerdeka.id/

# Installation

You should have [Heroku Toolbelt](https://toolbelt.heroku.com/) installed beforehand. In Mac OS X you can install it via `brew install heroku-toolbelt`. Then, make sure that [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is installed in your Python environment. No clue? [GTFO](http://www.urbandictionary.com/define.php?term=GTFO).

Do the following to install the dependencies:
```
make clean
make install
```

# Running Locally
```
make serve
```

Or, if you prefer to use the Heroku Toolbelt:
```
make heroku-toolbelt
```

# Deploying to Heroku
Make sure you have logged in to Heroku in Heroku Toolbelt.
```
heroku login
```

We have to get a place to push to from Heroku. You just need to do this once.
```
heroku create
```

Then, commit your changes to your local git repo.
```
git add .
git commit -m "Your commit message"
```

Push!
```
git push heroku master
```

Open the newly deployed app.
```
heroku open
```
