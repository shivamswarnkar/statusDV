import os


def is_file(file, extn):
	"""checks if given file exists, and has extention equal 
	to extn
		Args:
			file (str): path to file which will be examined
			extn (str): extension name which will be used for 
			testing 
		Returns:
			True or False whether file exists and has extention 
			equal to extn
	"""
	return os.path.isfile(file) and \
	os.path.splitext(file)[1].lower() == extn.lower()