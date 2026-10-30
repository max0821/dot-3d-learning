"""Self-authored native mesh adaptation of documented row-taper constraints.
Not MOTOMODEL code or a reproduction/test of the MT Hair Taper addon.
Run with installed Blender: blender -b --python build.py
"""
import bpy,bmesh,math,json
from pathlib import Path
from mathutils import Vector
O=Path(__file__).resolve().parent
stats={}
for name,taper in [('A-regular-grid',False),('B-row-taper',True)]:
 bpy.ops.wm.read_factory_settings(use_empty=True)
 vs=[];fs=[];rows=[];N=64;K=26
 for i in range(K):
  z=-.75+1.5*i/(K-1);t=max(0,min(1,(z-.15)/.60));s=1-t*t if taper else 1
  rows.append({'z':z,'scale':s,'width':.60*s,'depth':.60*s})
  for j in range(N):
   a=2*math.pi*j/N;vs.append((.30*s*math.cos(a),.30*s*math.sin(a),z))
 for i in range(K-1):
  for j in range(N):fs.append((i*N+j,i*N+(j+1)%N,(i+1)*N+(j+1)%N,(i+1)*N+j))
 fs.extend([tuple(reversed(range(N))),tuple((K-1)*N+j for j in range(N))])
 me=bpy.data.meshes.new('regular transverse rows');me.from_pydata(vs,[],fs);me.update()
 bm=bmesh.new();bm.from_mesh(me)
 if taper:bmesh.ops.remove_doubles(bm,verts=[v for v in bm.verts if v.co.z>.749],dist=1e-6)
 bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bm.to_mesh(me);bm.free();me.update()
 ob=bpy.data.objects.new('local taper control sample',me);bpy.context.collection.objects.link(ob)
 for p in me.polygons:p.use_smooth=True
 ma=bpy.data.materials.new('neutral clay');ma.diffuse_color=(.32,.48,.62,1);ob.data.materials.append(ma)
 bm=bmesh.new();bm.from_mesh(me);stats[name]={'rows_before_tip_merge':rows,'vertices':len(me.vertices),'nonmanifold_edges':sum(not e.is_manifold for e in bm.edges),'zero_area_faces':sum(f.calc_area()<1e-10 for f in bm.faces),'volume':bm.calc_volume(signed=False),'note':'quadratic falloff and row count are our adaptation, not author parameters'};bm.free()
 sc=bpy.context.scene;sc.render.engine='CYCLES';sc.cycles.samples=24;sc.cycles.use_denoising=False;sc.render.resolution_x=420;sc.render.resolution_y=420;sc.render.resolution_percentage=100
 sc.world=bpy.data.worlds.new('World');sc.world.color=(.12,.12,.12)
 bpy.ops.object.camera_add(location=(0,-7,0));cam=bpy.context.object;sc.camera=cam;cam.data.type='ORTHO';cam.data.ortho_scale=2.1
 for loc,pow,size in [((3,-4,5),550,4),((-4,-2,1),250,3),((0,4,3),400,3)]:
  bpy.ops.object.light_add(type='AREA',location=loc);li=bpy.context.object;li.data.energy=pow;li.data.shape='DISK';li.data.size=size;li.rotation_euler=(-li.location).to_track_quat('-Z','Y').to_euler()
 for view,loc in [('front',(0,-7,0)),('side',(7,0,0)),('back',(0,7,0)),('oblique',(4,-6,3)),('tip',(0,0,7))]:
  cam.location=loc;cam.rotation_euler=(-cam.location).to_track_quat('-Z','Y').to_euler();sc.render.filepath=str(O/f'{name}-{view}.png');bpy.ops.render.render(write_still=True)
 bpy.ops.wm.save_as_mainfile(filepath=str(O/(name+'.blend')))
(O/'report.json').write_text(json.dumps(stats,indent=2))
