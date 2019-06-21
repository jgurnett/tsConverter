#  Joel Gurnett
#  Converts ts files to mp4
#  June 21, 2019

#!/usr/bin/python
import subprocess
import os
from ffmpy import FFmpeg

# gets all ts files that are in given path
#
# dirPath = string of path given
def getFiles(dirPath):
	videoFiles = []
	files = os.listdir(dirPath)
	# go through all files in directory
	for index, file in enumerate(files):
		filename, file_extension = os.path.splitext(file)

		# if the file is a directory then iterate through that
		if(os.path.isdir(dirPath + file)):
			# don't look at hidden files
			if(file[0] != "."):
				inner = os.listdir(dirPath + file)
				for tmp in inner:
					tmpname, tmp_extension = os.path.splitext(tmp)
					if tmp_extension == ".ts":
						videoFiles.append(dirPath + file + "/" + tmp)


		if file_extension == ".ts":
			videoFiles.append(dirPath + file)

	if len(videoFiles) > 0:
		return videoFiles
	return None


# execute program
def main():
	# main path to start on 
	dirPath = "/Users/joelgurnett/Downloads/show/"
	# get list of ts files
	vids = getFiles(dirPath)

	# iterate through the list
	if vids != None:
		for index, video in enumerate(vids):
			filename, file_extension = os.path.splitext(video)
			infile = video
			outfile = filename + ".mp4"

			# display all ts files
			# for file in vids:
			# 	print(file)

			# convert ts to mp4
			p = subprocess.call(["ffmpeg", "-i", infile, outfile])
			# rmove ts file
			os.remove(infile)
	else:
		print("no files")

main()