import bpy,json
from pathlib import Path
O=Path(__file__).resolve().parent
coords=[]
for n in ['A-regular-grid','B-row-taper']:
 bpy.ops.wm.open_mainfile(filepath=str(O/(n+'.blend')))
 ob=bpy.data.objects['local taper control sample'];coords.append([tuple(v.co) for v in ob.data.vertices])
a,b=coords
ra=sorted(p for p in a if p[2]<=.150001);rb=sorted(p for p in b if p[2]<=.150001)
r={'root_and_lower_rows_exactly_equal':ra==rb,'z_extent_A':[min(p[2] for p in a),max(p[2] for p in a)],'z_extent_B':[min(p[2] for p in b),max(p[2] for p in b)],'tip_vertex_count_after_weld':sum(p[2]>.749999 for p in b),'reopened_saved_files':True}
(O/'verify.json').write_text(json.dumps(r,indent=2))
