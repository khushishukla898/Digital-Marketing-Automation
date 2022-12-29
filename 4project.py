
#!/usr/bin/env python
# coding: utf-8

# In[9]:


import urllib.request
from bs4 import BeautifulSoup as bs
from PIL import Image , ImageDraw, ImageFont
import urllib.request
import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize
import time


# In[10]:


item_name= 'Data Science Training Program'
tagline= """Apply Now Offer Price Rs. 899 only.
USE COUPEN CODE = intern899"""
tagline1 = """Data Science and Python Training Program for Everyone
                     (AGE:10 yrs to 70 yrs)"""

url='https://isteam.wsimg.com/ip/a8efe83b-6857-477d-9d0f-f13ca0229a20/ols/3923_original/:/rs=w:600,h:600'
logo_url='https://isteam.wsimg.com/ip/a8efe83b-6857-477d-9d0f-f13ca0229a20/ols/3908_original/:/rs=w:400,h:400'
image=urllib.request.urlretrieve(url,"img.png")
logo_image=urllib.request.urlretrieve(logo_url,"logo.png")


# In[12]:


img=Image.open("img.png")
logo=Image.open("logo.png").convert('RGBA')
img=img.resize((400,400))
bg = Image.open('bg.jpg')
bg=bg.resize((1000,800))
bg.paste(img,(50,230),mask=img)
bg.paste(logo,(550,20),mask=logo)
bg.save('final.png')
banner=Image.open('final.png')
font_type=ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',30)
font_type1=ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',35)
draw=ImageDraw.Draw(banner)
draw.text(xy=(500,170),text=tagline1,fill='Black',font=font_type1,anchor='ms',spacing=10)
draw.text(xy=(700,350),text="New Price= Rs 999.00",fill='Brown',font=font_type,anchor='ms',spacing=5,allign='right')
draw.text(xy=(700,400),text="Old Price= Rs 25000.00",fill='brown',font=font_type,anchor='ms',spacing=5,allign='right')
draw.text(xy=(530,700),text=tagline,fill='Green',font=font_type1,anchor='ms',spacing=10)
banner.save('final.png')
banner.show()

# In[13]:



 

def generate_video():
    image_folder = 'banner' # make sure to use your folder
    v = 'mygeneratedvideo.mp4'
    os.chdir("project-4")
      
    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")]
     
    # Array images should only consider
    # the image files ignoring others if any
    print(images) 
  
    frame = cv2.imread(os.path.join(image_folder, images[0]))
  
    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape  
  
    video = cv2.VideoWriter(v,0,1,24,(width, height)) 
  
    # Appending the images to the video one by one
    for image in images:
        for i in range(480):
            video.write(cv2.imread(os.path.join(image_folder, image))) 
      
    # Deallocating memories taken for window creation
    cv2.destroyAllWindows() 
    video.release()  
#generate_video()


# In[18]:



clip = VideoFileClip("mygeneratedvideo.mp4")

clip = clip.subclip(0,20)

#loading audio file
audioclip = AudioFileClip("audio.mpeg").subclip(0,20)

#adding audio to video
videoclip = clip.set_audio(audioclip)

#showing video clip
videoclip.ipython_display()
time.sleep(5)


# In[ ]:




