#!/usr/bin/env python

# Do https://dskjal.com/blender/rigify279-to-unity.html

import bpy
import os

rig = bpy.context.object

if rig.type != 'ARMATURE':
	print('This is not armature.')
else:
	print('Modifying...')
	bpy.ops.object.mode_set(mode='EDIT')
	rig.data.edit_bones['DEF-breast.L'].use_deform = False
	rig.data.edit_bones['DEF-breast.R'].use_deform = False
	rig.data.edit_bones['DEF-palm.01.L'].use_deform = False
	rig.data.edit_bones['DEF-palm.01.R'].use_deform = False
	rig.data.edit_bones['DEF-palm.02.L'].use_deform = False
	rig.data.edit_bones['DEF-palm.02.R'].use_deform = False
	rig.data.edit_bones['DEF-palm.03.L'].use_deform = False
	rig.data.edit_bones['DEF-palm.03.R'].use_deform = False
	rig.data.edit_bones['DEF-palm.04.L'].use_deform = False
	rig.data.edit_bones['DEF-palm.04.R'].use_deform = False
	rig.data.edit_bones['DEF-pelvis.L'].use_deform = False
	rig.data.edit_bones['DEF-pelvis.R'].use_deform = False
	rig.data.edit_bones['DEF-upper_arm.L'].parent = rig.data.edit_bones['DEF-shoulder.L']
	rig.data.edit_bones['DEF-upper_arm.R'].parent = rig.data.edit_bones['DEF-shoulder.R']
	rig.data.edit_bones['DEF-shoulder.L'].parent = rig.data.edit_bones['DEF-spine.003']
	rig.data.edit_bones['DEF-shoulder.R'].parent = rig.data.edit_bones['DEF-spine.003']
	rig.data.edit_bones['DEF-thigh.L'].parent = rig.data.edit_bones['DEF-spine']
	rig.data.edit_bones['DEF-thigh.R'].parent = rig.data.edit_bones['DEF-spine']
	rig.data.edit_bones['DEF-f_index.01.L'].parent = rig.data.edit_bones['DEF-hand.L']
	rig.data.edit_bones['DEF-f_index.01.R'].parent = rig.data.edit_bones['DEF-hand.R']
	rig.data.edit_bones['DEF-f_middle.01.L'].parent = rig.data.edit_bones['DEF-hand.L']
	rig.data.edit_bones['DEF-f_middle.01.R'].parent = rig.data.edit_bones['DEF-hand.R']
	rig.data.edit_bones['DEF-f_ring.01.L'].parent = rig.data.edit_bones['DEF-hand.L']
	rig.data.edit_bones['DEF-f_ring.01.R'].parent = rig.data.edit_bones['DEF-hand.R']
	rig.data.edit_bones['DEF-f_pinky.01.L'].parent = rig.data.edit_bones['DEF-hand.L']
	rig.data.edit_bones['DEF-f_pinky.01.R'].parent = rig.data.edit_bones['DEF-hand.R']
