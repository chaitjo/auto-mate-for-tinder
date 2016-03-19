![logo](https://raw.githubusercontent.com/ckjoshi9/Auto-Mate-for-Tinder/master/logo.png)

# Overview
Auto Mate uses cutting edge research in **Natural Language Processing** and **Feature Extraction** to rank Tinder profiles and automatically swipes right on all those which pass the 'promiscuity test'.

# Tech
* The unofficial <a href="https://gist.github.com/rtt/10403467">Tinder API documentation</a> and <a href="https://github.com/charliewolf/pynder">Pynder</a> (A Python client for the API) to interact with Tinder.
* A modified version of <a href="https://github.com/ParthGandhi/nude.py">nude.py</a> to analyse images for nudity/semi-nudity and assign scores based on skin pixel percentage. (Which is funny, because this algorithm is actually used in pornography blocking software.) 
* A <a href="https://github.com/aneesha/RAKE">Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm</a> to perform simple sentiment analysis. Keywords extracted from the bio are matched with a custom dictionary of keywords to obtain a score for the text.
* <a href="https://howhot.io/">Howhot.io</a> to rate images on a general level of attractiveness. (To-do)
* Django framework to deploy the webapp.

# Authors
* <a href="https://github.com/bbbranjan">Bobby Ranjan</a>
* <a href="https://github.com/ckjoshi9">Chaitanya Joshi</a>

# Disclaimer
No! We do not personally endorse using Tinder to hookup.
