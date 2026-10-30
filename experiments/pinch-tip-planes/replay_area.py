import bpy,math,json,traceback
from pathlib import Path
from mathutils import Vector,Quaternion
from bpy_extras.view3d_utils import location_3d_to_region_2d
O=Path(__file__).resolve().parent
area=bpy.context.area
if bpy.context.object and bpy.context.object.mode!='OBJECT':bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=.30,depth=1.5,location=(0,0,0))
ob=bpy.context.object;ob.name='cylinder clump practice'
b=ob.modifiers.new('Common rounded ends preparation','BEVEL');b.width=.08;b.segments=4
bpy.ops.object.modifier_apply(modifier=b.name)
ob.data.remesh_voxel_size=.018;bpy.ops.object.voxel_remesh()
for p in ob.data.polygons:p.use_smooth=True
baseline=[v.co.copy() for v in ob.data.vertices]
mask=ob.data.attributes.new('.sculpt_mask','FLOAT','POINT')
for i,co in enumerate(baseline):mask.data[i].value=max(0,min(1,(.20-co.z)/.18))
area.type='VIEW_3D';rv=area.spaces.active.region_3d
rv.view_rotation=Quaternion((1,0,0,0));rv.view_distance=2.8;rv.view_location=(0,0,.60);rv.view_perspective='ORTHO'
sc=bpy.context.scene
for a in 'xyz':setattr(sc.tool_settings.sculpt,'use_symmetry_'+a,False)
bpy.ops.object.mode_set(mode='SCULPT')
br=bpy.data.brushes.new('Native Pinch end taper review',mode='SCULPT');br.sculpt_tool='PINCH';br.strength=.7;br.size=110;br.use_frontface=False;br.asset_mark()
bpy.ops.brush.asset_activate(asset_library_type='LOCAL',relative_asset_identifier='Brush/'+br.name)
sc.tool_settings.unified_paint_settings.size=110
bpy.ops.wm.save_as_mainfile(filepath=str(O/'A-rounded-cylinder.blend'))
def run():
 try:
  region=next(r for r in area.regions if r.type=='WINDOW');rv=area.spaces.active.region_3d
  stroke=[]
  for i in range(41):
   t=i/40;loc=Vector((.012*math.cos(t*2*math.pi),.012*math.sin(t*2*math.pi),.75));p=location_3d_to_region_2d(region,rv,loc)
   stroke.append(dict(name='Native Pinch tip',location=loc,mouse=p,mouse_event=p,pressure=1,size=110,time=t,is_start=i==0,pen_flip=False,x_tilt=0,y_tilt=0))
  with bpy.context.temp_override(area=area,region=region):result=bpy.ops.sculpt.brush_stroke(stroke=stroke)
  bpy.ops.object.mode_set(mode='OBJECT');dis=[(v.co-co).length for v,co in zip(ob.data.vertices,baseline)]
  report={'native_operator_result':list(result),'tool':br.sculpt_tool,'blender':bpy.app.version_string,'vertices':len(dis),'changed_vertices':sum(d>1e-7 for d in dis),'max_displacement':max(dis),'root_below_z002_max':max(d for d,c in zip(dis,baseline) if c.z<.02),'strength':br.strength,'size_px':110,'events':41,'region':[region.width,region.height],'frontface_only':False,'assumption':'tip viewed axially; our brush path/settings, not reconstruction of author strokes','baseline':{'minz':min(c.z for c in baseline),'maxz':max(c.z for c in baseline)}}
  bpy.ops.wm.save_as_mainfile(filepath=str(O/'B-native-pinch.blend'));(O/'report.json').write_text(json.dumps(report,indent=2))
 except Exception:(O/'error.txt').write_text(traceback.format_exc())
 return None
bpy.app.timers.register(run,first_interval=1)
