# Usage
1. Download/clone this repository locally.
2. Install the following third-party libraries- <a href="https://github.com/charliewolf/pynder">pynder</a> and <a href="http://effbot.org/imagingbook/image.htm">Image</a>.
3. Get a facebook authentication token by loging in <a href="https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token">here</a>. It'll be in the url.
4. Put your facebook id and token into `test.py` and run the script using-
```
python test.py
```

# To-do
* [ ] Expand the keyword dictionary used for bio analysis.
* [ ] Incorporate <a href="https://howhot.io/">howhot.io</a>, possibly using <a href="https://pypi.python.org/pypi/mechanize/">mechanize</a> or <a href="https://pypi.python.org/pypi/selenium">selinium</a>.
* [ ] Make fetching facebook authentication token automatic.
