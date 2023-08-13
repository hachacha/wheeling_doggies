#https://www.trackinfo.com/trakdocs/hound/WD/RPAGES/WHEELING-Jun11-Sunday-Afternoon-Program.pdf
import pytesseract
import os
import pdfminer
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTFigure, LTChar
from pdfminer.image import ImageWriter
from PIL import Image




last_img = 0  # last image that we cycled through when extracting multiple pages.
dog = {}
#receive images from layout object
def get_image(layout_object):
    if isinstance(layout_object, pdfminer.layout.LTImage):
        return layout_object
    if isinstance(layout_object, pdfminer.layout.LTContainer):
        for child in layout_object:
            return get_image(child)
    else:
        return None


def save_images_from_page(page: pdfminer.layout.LTPage):
    images = list(filter(bool, map(get_image, page)))
    iw = ImageWriter('imgs')
    for image in images:
        # print(vars(image))
        iw.export_image(image)

# extract the pages in the pdf and loop on through each page
for page_layout in extract_pages("WHEELING-Apr05-Wednesday-Afternoon-Program.pdf"):
    print("i'm a new page \n\n\n\n\n")
    # is page layout the same as list of pages?
    # print(page_layout.__dict__)
    # print(vars(page_layout))
    # print(page_layout.pageid)

    # only way to do this is to get all the images on the page at once.
    print("getting the images\n")
    save_images_from_page(page_layout) #save the images on this first page.
    #once they're saved. get the list.
    img_list = os.listdir('imgs')
    images_we_loop_now = len(img_list)-last_img-1

    # 8 dogs per page


    for i in range(last_img,images_we_loop_now):
        if i % 3 == 0:
            dog_name = pytesseract.image_to_string(Image.open('imgs/img'+str(i)+'.bmp')).rstrip()
            # print(dog_name)
    last_img=images_we_loop_now # change the loop so you can start from the new page.
    # each img starts around this y position 
    # 713,685,677,631,603,595,549,521,513,467,439,431,385,357,349,303,275,267,213,185,177,123,95,87
    #so first dog is defined between the confines of 713 and 685.
# i don't think i want to loop through here. i'd rather go by number if it's all the same. 
# and do that for each page. will b frustrating.
    print("going through page layout")
    for element in page_layout:
        # print(element)
        if isinstance(element, LTTextContainer):
            # print(vars(element))
            print([element.y0, element.x0])
            print(element.get_text())
            # print(element.y1)
    
"""
[726.8025, 18.0] race title & distance 
[719.6375, 140.33] # Race, date (Wednesday Afternoon April 05, 2023), bets (WPS, QUINIELA, $3 PERFECTA, TRIFECTA, & .10 SUPER ($2 MIN BET))

ok the positions are not reliable.
just go in order then?

race(wheeling), #yards

#race, date(Wednesday Afternoon April 05, 2023),bet,whateverthisis(FIRST HALF LUCKY NORTH TWIN TRI(FORCE OUT EVERY FRIDAY))

wheeling, Grade

firstdog weight (csr ##), dog info: (birth, parents, breeder)

track info and something (not relevant), same

next

next

next

race history dog1:firstrace no date, second race no date(both in imgs), data up until weight for five races :)

positions in lines all the way own

far turn positions

finish positions-- first digit and then then split on second and third to get lengths lost by 49
38
33
612
210
37

ART, speed figure, odds, grade of race

dog 2 CSR

track info WD, same

next

next

next

second dog info breeder and so on

AFTER the 7th dog's finish position then we get the right side box for dog 1
kennel, top row of unecessarything, bottom row of unecessary thing, trainer, weight and low and hi grade and best time, order of showing of first3 grayhounds(probably useless)

chart writers comments on racing efforts for each race

THEN that same info for all 7 dogs

and then the dog 8's birthday
might be a little weird 
"""