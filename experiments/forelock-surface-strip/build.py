import bpy, math, json, hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parent
bpy.ops.wm.open_mainfile(filepath=str(P/'source-input/registered-context.blend'))
s=bpy.context.scene;s.cycles.samples=24;s.cycles.use_denoising=False
old=bpy.data.objects['Fixed historical context C front arc'];target=bpy.data.objects['Head sculpt with orbital planes']
# Small new editable strip. These are old visible outline landmarks, not reused failed B mesh.
outer=[(388,123),(353,96),(316,98),(281,119),(266,160)]
inner=[(374,142),(356,116),(325,139),(303,168),(286,197)]
vs=[];fs=[];cols=5
for j,(l,r) in enumerate(zip(outer,inner)):
 for k in range(cols):
  u=k/(cols-1);px=l[0]*(1-u)+r[0]*u;py=l[1]*(1-u)+r[1]*u
  vs.append(((px-345)/153,-1.0,2.72+(333-py)/153))
for j in range(4):
 for k in range(cols-1):
  a=j*cols+k;fs.append((a,a+1,a+cols+1,a+cols))
vs.append(((280-345)/153,-1,2.72+(333-215)/153))
for k in range(cols-1):fs.append((20+k,21+k,25))
me=bpy.data.meshes.new('Single distal tip continuous plane');me.from_pydata(vs,[],fs);me.update()
o=bpy.data.objects.new('Study single-tip surface strip',me);s.collection.objects.link(o);o.data.materials.append(old.data.materials[0]);o.hide_render=True
counts={}
for p in me.polygons:
 for key in p.edge_keys: counts[tuple(sorted(key))]=counts.get(tuple(sorted(key)),0)+1
boundary=[list(k) for k,v in counts.items() if v==1]
report={'input_sha256':hashlib.sha256((P/'source-input/registered-context.blend').read_bytes()).hexdigest(),'baseline04_sha256':hashlib.sha256((P/'source-input/iteration04.blend').read_bytes()).hexdigest(),'new_mesh_vertices':len(vs),'new_mesh_faces':len(fs),'boundary_edges':boundary,'root_boundary_vertices':[0,1,2,3,4],'distal_single_tip_vertex':25,'target':target.name,'target_status':'Historical 04 geometry; hidden shape NOT reference ground truth','tools_order':['new 5-column quad strip with single distal fan','native Shrinkwrap NEAREST_SURFACEPOINT ON_SURFACE offset .035 on whole strip to 04 head','apply Shrinkwrap; preserve projected cage','Subdivision level2','Solidify .02 tapered to zero at distal tip'],'assumptions':['front workplane Y=-1 selects nearest front head surface','whole head is preserved historical design proxy, not verified scalp','offset .035 and thickness .02 are design assumptions, not measured','no B/C failed mesh reused; same visible landmark list used only to set plane X/Z']}
(P/'INPUT_GATE.json').write_text(json.dumps(report,indent=2))
bpy.ops.wm.save_as_mainfile(filepath=str(P/'pre-shrinkwrap-cage.blend'))
# New methodological evidence vs old B/C: head-conforming deformer BEFORE thickness, not guessed root-back bend.
bpy.context.view_layer.objects.active=o;o.select_set(True)
sw=o.modifiers.new('Author-method closest surface adaptation','SHRINKWRAP');sw.target=target;sw.wrap_method='NEAREST_SURFACEPOINT';sw.wrap_mode='ON_SURFACE';sw.offset=.035
bpy.ops.object.modifier_apply(modifier=sw.name)
report['projected_cage_xyz']=[list(v.co) for v in me.vertices]
report['root_edge_length']=sum((me.vertices[i+1].co-me.vertices[i].co).length for i in range(4))
for p in me.polygons:p.use_smooth=True
sub=o.modifiers.new('preview subdivision','SUBSURF');sub.levels=sub.render_levels=2
vg=o.vertex_groups.new(name='Thickness taper');vg.add(list(range(20)),1,'REPLACE');vg.add(list(range(20,25)),.5,'REPLACE');vg.add([25],0,'REPLACE')
sol=o.modifiers.new('thin shell after conformation','SOLIDIFY');sol.thickness=.02;sol.offset=0;sol.vertex_group=vg.name;sol.thickness_vertex_group=0
T=Vector((0,0,3.75));views={'front':(0,-9,3.75),'side':(9,0,3.75),'back':(0,9,3.75),'oblique':(6,-9,5.0)}
for label in ['A-old-double-tip','B-conformed-single-tip']:
 old.hide_render=label.startswith('B');o.hide_render=label.startswith('A')
 for v,loc in views.items():
  s.camera.location=loc;s.camera.rotation_euler=(T-s.camera.location).to_track_quat('-Z','Y').to_euler();s.render.filepath=str(P/f'{label}-{v}.png');bpy.ops.render.render(write_still=True)
 if label.startswith('B'):bpy.ops.wm.save_as_mainfile(filepath=str(P/'B-conformed-single-tip.blend'))
(P/'RESULTS.json').write_text(json.dumps(report,indent=2))
