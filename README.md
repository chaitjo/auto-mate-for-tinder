![logo](https://raw.githubusercontent.com/chaitjo/Auto-Mate-for-Tinder/master/logo.png)

# Overview
Auto Mate uses existing research in **Natural Language Processing** and **Computer Vision** to rank Tinder profiles and automatically swipes right on all those which pass the 'promiscuity test'.

# Tech
* The unofficial <a href="https://gist.github.com/rtt/10403467">Tinder API documentation</a> and <a href="https://github.com/charliewolf/pynder">Pynder</a> (A Python client for the API) to interact with Tinder.
* A modified version of <a href="https://github.com/ParthGandhi/nude.py">nude.py</a> to analyse images for nudity/semi-nudity and assign scores based on skin pixel percentage. (Which is funny, because this algorithm is actually used in pornography blocking software.) 
* A <a href="https://github.com/aneesha/RAKE">Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm</a> to perform simple sentiment analysis. Keywords extracted from the bio using the algorithm are matched with a custom dictionary of keywords to obtain a score for the text.
* <a href="https://howhot.io/">Howhot.io</a> to rate images on a general level of attractiveness. (To-do)
* Django framework to deploy the webapp.

# Examples
Different parts of the algorithm in action.

### Image analysis
![Image](https://raw.githubusercontent.com/chaitjo/Auto-Mate-for-Tinder/master/Examples/image.jpg)

The image analysis algorithm detects skin pixels and returns the total percentage of skin pixels in the image as the score. The higher the score, the greater the promiscuity.

Though not perfect, the skin pixel patterns identified by the algorithm can be seen below.

![Emily Ratajkowski](https://raw.githubusercontent.com/chaitjo/Auto-Mate-for-Tinder/master/Examples/emily.jpg)
![Bradley Cooper](https://raw.githubusercontent.com/chaitjo/Auto-Mate-for-Tinder/master/Examples/cooper.jpg)

Hollywood superstars Emily Ratajkowski and Bradley Cooper got scores of 12.1% and 28.6% respectively, though that might have something to do with Cooper being shirtless.

### Bio analysis
![Bio](https://raw.githubusercontent.com/chaitjo/Auto-Mate-for-Tinder/master/Examples/bio.jpg)

The RAKE algorithm extracts keywords from a bio, which are then matched with a custom dictionary of keywords to obtain a score for the text. The higher the rating, the greater the promiscuity, as seen in the example above. 

Jane Doe's friendly bio receives a negative score while John Doe gets a very high positive score for his flirty bio.

# Authors
* <a href="https://github.com/chaitjo">Chaitanya Joshi</a>
* <a href="https://github.com/bbbranjan">Bobby Ranjan</a>

# Disclaimer
No! We do not personally endorse using Tinder to hookup.
