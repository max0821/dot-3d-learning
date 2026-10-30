"""Diagnostic only: unchanged geometry, selected root-support gate. No new hair shape."""
import bpy,json,hashlib,math
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree
P=Path(__file__).resolve().parent
bpy.ops.wm.open_mainfile(filepath=str(P/'source-input/registered-context.blend'))
s=bpy.context.scene;target=bpy.data.objects['Head sculpt with orbital planes'];d=bpy.context.evaluated_depsgraph_get();e=target.evaluated_get(d);me=e.to_mesh();verts=[target.matrix_world@v.co for v in me.vertices];faces=[tuple(p.vertices) for p in me.polygons];bvh=BVHTree.FromPolygons(verts,faces);zmax=max(v.z for v in verts);e.to_mesh_clear()
root=[]
for i in range(5):
 u=i/4;px=388*(1-u)+374*u;py=123*(1-u)+142*u;root.append(Vector(((px-345)/153,-1,2.72+(333-py)/153)))
# Separate test fixture, root group only. These are projected image landmarks, not anatomical root coordinates.
other=[v+Vector((-.03,0,-.05)) for v in root]
m=bpy.data.meshes.new('Diagnostic selected boundary fixture');m.from_pydata(root+other,[],[(i,i+1,i+6,i+5) for i in range(4)]);m.update();o=bpy.data.objects.new('Projection gate fixture NOT hair model',m);s.collection.objects.link(o)
g=o.vertex_groups.new(name='ROOT_ONLY');g.add(list(range(5)),1,'REPLACE');before=[v.co.copy() for v in m.vertices]
sw=o.modifiers.new('Selected Y projection applicability test','SHRINKWRAP');sw.target=target;sw.vertex_group=g.name;sw.wrap_method='PROJECT';sw.use_project_x=False;sw.use_project_y=True;sw.use_project_z=False;sw.use_positive_direction=True;sw.use_negative_direction=False;sw.offset=.035
bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.modifier_apply(modifier=sw.name);after=[v.co.copy() for v in m.vertices];o.hide_render=True;o.hide_set(True)
results={'status':'NOT APPLICABLE at fixed image X/Z: root boundary lies entirely above historical head surface','new_hair_geometry':False,'input_sha256':hashlib.sha256((P/'source-input/registered-context.blend').read_bytes()).hexdigest(),'target':target.name,'target_max_z':zmax,'head_top_image_y':333-153*(zmax-2.72),'selected_root_source_pixels':[[388,123],[374,142]],'root_vertices_world':[list(v) for v in root],'root_z_min':min(v.z for v in root),'root_z_max':max(v.z for v in root),'minimum_vertical_gap':min(v.z for v in root)-zmax,'projection_direction':[0,1,0],'projection_hits':[bvh.ray_cast(v,Vector((0,1,0)))[0] is not None for v in root],'native_project_movement':[float((b-a).length) for a,b in zip(before,after)],'selection':'ROOT_ONLY vertices0..4; vertices5..9 excluded','assumptions':['selected historical visible-junction boundary is not proven anatomical root','04 head is preserved historical proxy, not ground truth hidden cranium','root Y=-1 for diagnostic ray origin only; no Y sweep','fixed X/Z correspondence derives from prior uniform registration; camera uncertainty persists'],'method_precondition':'UCBUGG starts nearly touching forehead; fixed high visible junction cannot directly be a forehead support patch','decision':'No extrusion or hair modification. Future connected support may require lower boundary plus explicit free transition, not root-point wrap at this height.'}
(P/'RESULTS.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
# Render diagnostic landmarks with existing model untouched, not new hair.
def line(name,points,color):
 c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.bevel_depth=.008;c.bevel_resolution=2;p=c.splines.new('POLY');p.points.add(len(points)-1)
 for a,b in zip(p.points,points):a.co=(*b,1)
 ob=bpy.data.objects.new(name,c);s.collection.objects.link(ob);mat=bpy.data.materials.new(name);mat.diffuse_color=(*color,1);c.materials.append(mat)
line('Orange diagnostic projected junction, NOT inferred root',root,(1,.15,.01));line('Cyan historical head maximum height',[(-.6,-.7,zmax),(.6,-.7,zmax)],(.01,.8,1))
s.render.resolution_x=s.render.resolution_y=480;s.render.resolution_percentage=100;s.cycles.samples=24;s.cycles.use_denoising=False
T=Vector((0,0,3.75));views={'front':(0,-9,3.75),'side':(9,0,3.75),'back':(0,9,3.75),'oblique':(6,-9,5.)}
for v,loc in views.items():
 s.camera.location=loc;s.camera.rotation_euler=(T-s.camera.location).to_track_quat('-Z','Y').to_euler();s.render.filepath=str(P/f'gate-{v}.png');bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(P/'support-gate-diagnostic.blend'))
