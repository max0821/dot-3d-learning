import bpy,json
from pathlib import Path
O=Path(__file__).parent
P=O.parent/'mass-layer-separation'
def read(p):
 bpy.ops.wm.open_mainfile(filepath=str(p));o=bpy.data.objects['cylinder clump practice'];return [v.co.copy() for v in o.data.vertices]
a=read(P/'A-rounded-cylinder.blend');a2=read(O/'A-rounded-cylinder.blend');a3=read(O/'A-fixed-z-input.blend');old=read(P/'B-native-pinch.blend');b=read(O/'B-native-pinch.blend');c=read(O/'C-fixed-z-pinch.blend')
r={'input_same_max':max((x-y).length for x,y in zip(a,a2)), 'z_input_same_max':max((x-y).length for x,y in zip(a,a3)), 'area_replay_max':max((x-y).length for x,y in zip(old,b)), 'z_vs_area_max':max((x-y).length for x,y in zip(b,c)), 'z_root_max':max((x-y).length for x,y in zip(a,c) if x.z<.02)}
(O/'verify.json').write_text(json.dumps(r,indent=2));print(r)
