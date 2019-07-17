import os


def is_img(file):
	"""checks whether given file exists, and is an image file 
	of supported format
		Args:
			file (str): path to file which will be examined
		Returns:
			True or False whether file exists and has extention 
			equal to supported image file extentions
	"""
	return os.path.isfile(file) and \
	os.path.splitext(file)[1] in ['.jpg','.png', '.jpeg']


def sum_imgs(overlay, background, output_filename):
	""" Pastes overlay onto background image and saves resulting
	image file at output_filename
		Args:
			overlay (PIL.Image) : Image which will be pasted 
								on background
			background (PIL.Image) : Image to be used as background
			output_filename (str) : output file name with path
		Returns:
			saves output image as file at output_filename path
			returns None
	"""
	# resize overlay to fit on background
	overlay.thumbnail(background.size)

	# create new Image of size background.size
	transparent = Image.new('RGBA', background.size, (1, 1, 1, 1))

	# paste both images in order
	transparent.paste(background, (0, 0))
	transparent.paste(overlay, (0, 0), mask=overlay)

	# save resulting image
	transparent.save(output_filename)