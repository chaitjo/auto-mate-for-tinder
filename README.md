![logo](https://raw.githubusercontent.com/chaitjo/Auto-Mate-for-Tinder/master/logo.png)

# Overview
Auto Mate uses existing research in **Natural Language Processing** and **Computer Vision** to rank Tinder profiles and automatically swipes right on all those which pass the 'promiscuity test'.

**Read more and check out some examples in the blog post here: [chaitjo.github.io/automate](https://chaitjo.github.io/automate/).**

# Tech
* The unofficial <a href="https://gist.github.com/rtt/10403467">Tinder API documentation</a> and <a href="https://github.com/charliewolf/pynder">Pynder</a> (A Python client for the API) to interact with Tinder.
* A modified version of <a href="https://github.com/ParthGandhi/nude.py">nude.py</a> to analyse images for nudity/semi-nudity and assign scores based on skin pixel percentage. (Which is funny, because this algorithm is actually used in pornography blocking software.) 
* A <a href="https://github.com/aneesha/RAKE">Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm</a> to perform simple sentiment analysis. Keywords extracted from the bio using the algorithm are matched with a custom dictionary of keywords to obtain a score for the text.
* <a href="https://howhot.io/">Howhot.io</a> to rate images on a general level of attractiveness. (To-do)
* Django framework to deploy the webapp.

# Authors
* <a href="https://github.com/chaitjo">Chaitanya Joshi</a>
* <a href="https://github.com/bbbranjan">Bobby Ranjan</a>

# Disclaimer
We do not personally endorse or condemn using Tinder for hooking up, nor can we speak for the results obtained by using our application. The idea came about as a joke when we were having a deep conversation about how society and dating had changed for the worse, and was meant to be a parody of how young people use Tinder: brainlessly swiping right to bounce from one meaningless fling to another. 
