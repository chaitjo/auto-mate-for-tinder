import pynder
import urllib

from nude import *
from rake import *

if __name__ == "__main__":
    facebook_id = ''
    facebook_auth_token = ''
    user_limit = 1
    image_limit = 1

    session = pynder.Session(facebook_id, facebook_auth_token)
    total_users = session.nearby_users()
    if len(total_users) > user_limit:
        users = total_users[:user_limit]
    else:
        users = total_users
    
    user_number = 1
    for user in users:
        print("\n----------\n\nRunning the algorithm for " + user.name + ', ' + str(user.age))
        total_skin_percent = 0.0
        bio_score = 0.0
        final_percent = 0.0

        # Image nudity analysis
        try:
            for i in range(image_limit):
                image_name = str(user_number) + '_' + str(i+1) + '.jpg'
                photo_url = str(user.get_photos(width='640')[i])
                print('\nPhoto '+ str(i) + ':\n' + photo_url)
                image = urllib.URLopener()
                image.retrieve(photo_url, image_name)

                skin_percent = 100*contains_nudity(image_name)
                color_skin(image_name)
                print('Skin region percentage = ' + str(skin_percent))
                total_skin_percent += skin_percent
        except IndexError:
                print('')

        total_skin_percent /= image_limit
        print('\nAverage skin region percentage = ' + str(total_skin_percent))
        
        # Bio text analysis
        try:
            text = user.bio.lower().replace('\n','. ')
            rake = Rake("rake_res/SmartStoplist.txt")
            keywords = rake.run(text.lower())          

            word_list = {'hook up':-10, 'hookup':-10, 'single':-5, 'booty':-9, 'fuck':-10, 'sex':-7, 'swipe':-3, 'conversation':5, 'stories':7, 'right':-5, 'shag':-10, 'fit':-5, 'call':-2, 'personality':4, 'body':-6, 'cuddle':-3, 'mature':-1, 'smile':3, 'exchange':-8, 'temp':-8, 'sleep':-9}
            
            #keywords -> list of tuples. Each element- (word, wordscore)
            for element in keywords: 
                for word in word_list.keys():
                    if (element[0] in word) or (word in element[0]):
                        bio_score += -1.0*word_list[word]*element[1]
        except: pass
        
        if bio_score > 100 : bio_score = 100
        
        print('\nBio: ' + text)
        print(keywords)
        print('Bio score = ' + str(bio_score))

        final_percent = (total_skin_percent + bio_score)/2
        print('\nFinal Score = ' + str(final_percent))

        user.like()
        user_number += 1