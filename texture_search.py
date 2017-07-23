#!/usr/bin/env python

# Blender script to remap image files.

import bpy
import os

def search_rec(root, file_name, depth = 0):
	if depth == 5:
		return None
	for f in os.listdir(root):
		path = os.path.join(root, f)
		if os.path.isdir(path):
			res = search_rec(path, file_name, depth + 1)
			if not res is None:
				return res
		else:
			if f == file_name:
				return path
	return None

cur = bpy.path.abspath("//")

for obj in bpy.data.images:
	print(obj.filepath)
	realpath = bpy.path.abspath(obj.filepath)
	basename = bpy.path.basename(obj.filepath)
	if os.path.isfile(realpath):
		print("ok")
		continue
	else:
		print("%s does not exist. Searching ..." % obj.filepath)
		res = search_rec(cur, basename)
		if res is not None:
			relpath = bpy.path.relpath(res)
			print("found %s" % relpath)
			obj.filepath = relpath
