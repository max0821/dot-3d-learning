import bpy, math
from pathlib import Path
from mathutils import Vector
O=Path(__file__).parent
for n in ['B-native-pinch','C-fixed-z-pinch']:
 bpy.ops.wm.open_mainfile(filepath=str(O/(n+'.blend')))
 if bpy.context.object and bpy.context.object.mode!='OBJECT':bpy.ops.object.mode_set(mode='OBJECT')
 sc=bpy.context.scene;sc.render.engine='CYCLES';sc.cycles.samples=24;sc.cycles.use_denoising=False
 sc.render.resolution_x=420;sc.render.resolution_y=420;sc.render.resolution_percentage=100
 sc.world.color=(.12,.12,.12)
 ob=bpy.data.objects.get('cylinder clump practice')
 ma=bpy.data.materials.new('neutral clay');ma.diffuse_color=(.32,.48,.62,1);ob.data.materials.clear();ob.data.materials.append(ma)
 bpy.ops.object.camera_add(location=(0,-7,0));cam=bpy.context.object;sc.camera=cam;cam.data.type='ORTHO';cam.data.ortho_scale=2.1
 for loc,pow,size in [((3,-4,5),550,4),((-4,-2,1),250,3),((0,4,3),400,3)]:
  bpy.ops.object.light_add(type='AREA',location=loc);li=bpy.context.object;li.data.energy=pow;li.data.shape='DISK';li.data.size=size;li.rotation_euler=(-li.location).to_track_quat('-Z','Y').to_euler()
 for view,loc in [('front',(0,-7,0)),('side',(7,0,0)),('back',(0,7,0)),('oblique',(4,-6,3)),('tip',(0,0,7))]:
  cam.location=loc;cam.rotation_euler=(-cam.location).to_track_quat('-Z','Y').to_euler();sc.render.filepath=str(O/f'{n}-{view}.png');bpy.ops.render.render(write_still=True)
 bpy.ops.wm.save_as_mainfile(filepath=str(O/(n+'-render-scene.blend')))
