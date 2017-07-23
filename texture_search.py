#!/usr/bin/env python

# Blender script to remap image files.

bl_info = {
	"name": "Image Reassigner",
	"description": "Search and reassign image file of image object of missing file.",
	"author": "Takahiro Poly Horikawa",
	"version": (0, 0, 1),
	"blender": (2, 78, 0),
	"location": "3D View > Object",
	"warning": "",
	"wiki_url": "",
	"category": "3D View"
}

import bpy
import os

MAX_DEPTH = 5

class ImageReassigner(bpy.types.Operator):
	"""Search and reassign image file of image object of missing file."""	  # blender will use this as a tooltip for menu items and buttons.
	bl_idname = "object.image_reassigner"		# unique identifier for buttons and menu items to reference.
	bl_label = "Reassign Images"		 # display name in the interface.
	bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

	def execute(self, context):

		# The original script
		# scene = context.scene
		# for obj in scene.objects:
		# 	obj.location.x += 1.0

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

		return {'FINISHED'}			# this lets blender know the operator finished successfully.

def menu_func(self, context):
	self.layout.operator("object.image_reassigner")	 # 登録したいクラスの「bl_idname」を指定

def register():
	bpy.utils.register_class(ImageReassigner)
	bpy.types.VIEW3D_MT_object.prepend(menu_func)

def unregister():
	bpy.utils.unregister_class(ImageReassigner)
	bpy.types.VIEW3D_MT_object.remove(menu_func)

def search_rec(root, file_name, depth = 0):
	if depth >= MAX_DEPTH:
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

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
	register()
