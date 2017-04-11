#!/usr/bin/env python
from PIL import Image
def roll(image,delta):
	"Roll an image sideways"
	xsize ,ysize=image.size
	delta = delta % xsize
	if delta == 0:
		return image
	part1 = image.crop((0,0,delta,ysize))
	part2 = image.crop((delta,0,xsize,ysize))
	image.paste(part2,(0,0,xsize-delta,ysize))
	image.paste(part1,(xsize - delta,0,xsize,ysize))
	return image
def fun(img,box):
	reg = img.crop(box)
	reg.show()
	reg = reg.transpose(Image.ROTATE_180)
	reg.show()
	img.paste(reg,box)
	img.show()

img = Image.open("1.jpg")
box = (100,100,200,200)
fun(img,box)
#roll(img,80).show()



