

from PIL import Image, ImageFont, ImageDraw,ImageFilter
from django.shortcuts import render     


def picture_image(request):
    my_image = Image.open('static/laptop2_adobespark.png')
    front_image=Image.open('static/laptop3.jpg')
    # backs_image=Image.open('static/work.jpg').
    backg_image=Image.open('static/IMG_20210214_145604_032.jpg')
    backg_image=backg_image.resize((230,130))
    backg_image.save('static/backg_image.jpg')



    title_font = ImageFont.truetype('mpesa_api/obelix_pro_26363/ObelixPro-cyr.ttf',14)
    title_text='My name is  mwashe\nA software developer \ninspired  to  create \nresponsive scalable \nand inspiring software'
    



    image_editable=ImageDraw.Draw(my_image)
    image_editable.text((140,90),title_text,(0,100,0),font=title_font)
    my_image.save('static/result.png')
    
   
    # paste method
    # front_image.paste(backg_image,(129,130))
    # front_image.save('static/laptop55.jpg',quality=95)




    # copy image
    # back_img=front_image.copy()
    # back_img.paste(backs_image,(200,145))



    # back_img.save('static/laptop5.jpg')



    # mask image
   


    # mask_im = Image.new("RGB", front_image.size, 0)
    # draw = ImageDraw.Draw(mask_im)
    # draw.ellipse((140, 50, 260, 170), fill=255)
    # mask_im.save('static/laptop5.jpg', quality=95)



    # back_im = front_image.copy()
    # back_im.paste(backs_image, (100, 100), mask_im)
    # back_im.save('data/dst/rocket_pillow_paste_mask_circle.jpg', quality=95)



    return render(request,'back.html')
