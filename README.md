# StatusDV 
StatusDV is a flask powered webapp which allows users to create custom wordcloud from anyone's twitter timeline, raw text inputs or facebook statuses (not allowed after facebook policy changes but user can use dummy status generator instead). 
[Try Here!!](https://statusdv.herokuapp.com/)

### About
 This repo contains different custom packages which were used in the webapp. You can use these packages independently from this project to retrieve anyone's tweets or to load facebook statuses. This repo also contains some utils functions (each file is well-documented)
 
 Because of security reasons and privacy policies, source code for webapp cannot be made public. 
 
 ### How to Use

***1. [Custom_wordcloud_generator](custom_wordcloud_generator.ipynb)***  
It is a jupyter notebook which contains examples of how webapp generates some of its custom wordclouds

**2. facebook_api** 
Retrieve user statues by giving user token 
```
>>> from facebook_api.feed import Feed
>>> feed = Feed() # init object with default settings
>>> status_lst = feed.load(token="YOUR_USER_TOKEN") # returns user statuses
```
Use get_user from facebook_api.utils to check user token's validity and get user's name, id
```
>>> from facebook_api.utils import get_user
>>> get_user(token="YOUR_USER_TOKEN") # returns name & id if valid, else None
```

**3. twiiter_api**
Retrieve user tweets easily. It's a flask wrapper for tweepy. Your app.config should contain following twitter keys
- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET,
- TWITTER_ACCESS_TOKEN
- TWITTER_ACCESS_TOKEN_SECRET

Once you have your flask app ready, you can easily use it with twitter_api as following
```
>>> from twitter_api.user import Timeline
>>> tm = Timeline()   # you can give app=flask_app
>>> tm.init_app(app=your_flask_app)
>>>tweets = tm.get_tweets(handle='YOUR_TWITTER_USER_NAME') 
# returns list of tweets
```

**4. utils**
utils contains various functions to generate [dummy word-frequency dict](utils/status_utils.py#L6), [filter function](utils/status_utils.py#L27) to remove non-ascii chars from text and [file utils](utils/file_utils.py#L4) to check custom file constraints. Image utils contains functions to [merge two images](utils/img_utils.py#L17) and to check whether given image file is of a [supported type](utils/img_utils.py#L4).

### Structure
[Repo Structure](static/structure.png)

### Dependencies
- python 3.6
- certifi==2019.6.16
- chardet==3.0.4
- cycler==0.10.0
- idna==2.8
- kiwisolver==1.1.0
- matplotlib==3.1.1
- numpy==1.16.4
- oauthlib==3.0.2
- pillow==6.1.0
- pyparsing==2.4.0
- PySocks==1.7.0
- python-dateutil==2.8.0
- requests==2.22.0
- requests-oauthlib==1.2.0
- six==1.12.0
- tweepy==3.8.0
- urllib3==1.25.3
- wordcloud==1.5.0