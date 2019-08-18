# Taiwan Indie Music Scraper
This is an on going project to analyse and create content related to Taiwan Indie Music

# Setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Database
Please start mongodb isntance before running the app on port 27017.
Configure aexternal database with the following .env file
```
MongoDB=SOME_Address
Mongo_UserName=SOME_UserName
Mongo_Password=SOME_Password
```