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

    save_images_from_page(page_layout) #save the images on this first page.
    #once they're saved. get the list.
    img_list = os.listdir('imgs')
    images_we_loop_now = len(img_list)-last_img-1

    for i in range(last_img,images_we_loop_now):
        if i % 3 == 0:
            dog_name = pytesseract.image_to_string(Image.open('imgs/img'+str(i)+'.bmp')).rstrip()
            # print(dog_name)
    last_img=images_we_loop_now # change the loop so you can start from the new page.
    # each img starts around this y position 
    # 713,685,677,631,603,595,549,521,513,467,439,431,385,357,349,303,275,267,213,185,177,123,95,87
    #so first dog is defined between the confines of 713 and 685.

    for element in page_layout:
        print(element)
        if isinstance(element, LTTextContainer):
            # print(vars(element))
            print('farmer')
            # print(element.get_text())
            # print(element.y1)
        elif isinstance(element, LTFigure):
            for e in element:
                if isinstance(e, LTChar):
                    print('this is the ltchar!!!!!!!!\n\n')
                    text = element.get_text()
                    print(text)
