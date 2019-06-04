from PIL import Image,ImageOps
from io import BytesIO
import json


def get_name():
    with open('../data/exampleName.json', 'r') as f:
        data = json.load(f)
        names = data['names']
        for i in range(len(names)):
            names[i] = names[i].split('.')[0]
    return names


def remove_transparency(im, bg_colour=(255, 255, 255)):

    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im

def crop_margin(im, padding=(0, 0, 0, 0)):
    #with BytesIO('') as output_bf:
    image = im.convert('RGB')
    ivt_image = ImageOps.invert(image)
    bbox = ivt_image.getbbox()
    left = bbox[0] - padding[0]
    top = bbox[1] - padding[1]
    right = bbox[2] + padding[2]
    bottom = bbox[3] + padding[3]
    cropped_image = image.crop([left, top, right, bottom])
    #cropped_image.save(output_bf, format='PNG')
    #ret = output_bf.getvalue()
    return cropped_image

'''
image = Image.open('./image/3d-cone.png')
new_image = remove_transparency(image)
new_image = crop_margin(new_image)
new_image.save('./image/test3.png','png')
'''
def crop():

    names = get_name()

    for name in names:
        print(name)
        image = Image.open('./image/'+name+'.png')
        new_image = remove_transparency(image)
        try:
            new_image = crop_margin(new_image)
        except:
            pass
        new_image.save('./cropped_image/'+name+'.png','png')

def refine():
    names = get_name()

    for name in names:
        print(name)
        image = Image.open('./cropped_image/'+name+'.png')
        new_image = remove_transparency(image)
        #try:
        #    new_image = crop_margin(new_image)
        #except:
        #    pass
        new_image.save('./cropped_image/'+name+'.png','png')

refine()
