#!/usr/bin/python3
import sys
import os
import codecs

args = sys.argv

def readData(filename):
	fileObj = open(filename)
	data = fileObj.read()
	return data

def writeData(filename, data):
	fileObj = open(filename, "w")
	fileObj.write(data)
	fileObj.close()

def run():
	option = args[1].lower()
	filename = args[2]
	if os.path.exists(filename):
		data = readData(filename)
		if option == "encrypt":
			writeData(filename, codecs.encode(data, "rot_13"))
		elif option == "decrypt":
			writeData(filename, codecs.decode(data, "rot_13"))
		else:
			print("USAGE: ./... encrypt(decrypt) filename")
	else:
		print("FILE NOT FOUND")

if __name__ == "__main__":
	run()
