import operator
import argparse

import Image
from nude_res.Pixel import * 
from nude_res.Region import *
from nude_res.utils import *

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

if __name__ == "__main__":
    # Can be used to test individual images
    print "Skin pixel score= "+str(contains_nudity('test.jpg')*100)
    color_skin('test.jpg')