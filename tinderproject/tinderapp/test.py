# nude.py and pynder stuff.
import operator
import argparse
import sys
import pynder
import urllib

#rake stuff
import re
import operator

sys.path.insert(0, 'src/')

from PIL import Image
from Pixel import * 
from Region import *
from utils import *


#nude.py functions
def contains_nudity(image_path):
    image = Image.open(image_path)
    imgPixels = image.load()
    width = image.size[0]
    height = image.size[1]
    pixels = [ [None]*height for i in range(width) ]

    for i in xrange(0, width):
        for j in xrange(0, height):
            pixels[i][j] = Pixel(i, j, imgPixels[i,j][0], imgPixels[i,j][1], imgPixels[i,j][2])
    
    skin_pixels = []
    skin_regions = []
    create_skin_regions(pixels, skin_pixels, skin_regions, width, height)

    if len(skin_regions) < 3:
        return 0.0
    skin_regions.sort(key = operator.attrgetter('size'), reverse=True)

    bounding_region = create_bounding_region(pixels, skin_regions, width, height)
    return analyze_regions(skin_pixels, skin_regions, bounding_region, width, height)


def color_skin(image_path):
    save_path = image_path[:-4] + "-skinified.jpg"
    color_skin_regions(image_path, save_path)

#################################################

# session = pynder.Session('chait9', 'CAAGm0PX4ZCpsBAGFJUUIVFWxpyzl4TEaXuCTFExnv0ldZBJXnwK9PRRKofMVGYROf0cTWGrhTpTB4gANZCji5eCdZCDdomID3obXY4k2YOcZArhGdcmFOso7toZAmQcw4ZCFsMEati0TdfRxUcjQRVn9HRZBxIao3w54W4i7ZCT1n8tVRyelCBUHZCZCOm3TlyjZC3yEdSAtjq9ZAllzvKV4fLjYb')
# total_users=session.nearby_users()
# print len(total_users)
count=0
image_name = 'photo' + str(count) + '.jpg'
photo_url = "http://i.huffpost.com/gen/1593698/thumbs/o-BLACK-MODELS-FASHION-CAMPAIGNS-570.jpg"
print photo_url
image=urllib.URLopener()
image.retrieve(photo_url,image_name)
count = count + 1

parser = argparse.ArgumentParser(description='Detect nudity in images.')
parser.add_argument(image_name, type=str, nargs=1)
parser.add_argument('-c', action='store_true')
args = parser.parse_args()

if args.c is True:
    color_skin(image_name)
    print "Skin regions covered in image saved at " + image_name[:-4] + "-skinified.jpeg"
    skin_percent = 100*contains_nudity(image_name)
    print "Skin region percentage = " + str(skin_percent)
else:
    nudity = contains_nudity(image_name)
    if nudity:
       print "Image contains nudity"
    else:
        print "Image doesn't contain nudity"