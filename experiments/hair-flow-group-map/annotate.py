"""Reference analysis only. No generated anatomy, no model or new render."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math,json
P=Path(__file__).resolve().parent
SRC=P.parent.parent/'images'/'reference'/'character-three-views.png'
src=Image.open(SRC).convert('RGB'); crop=(225,0,430,250); scale=2
im=src.crop(crop).resize((410,500),Image.Resampling.LANCZOS)
out=Image.new('RGB',(900,690),'#f3f3ef');out.paste(im,(25,75));out.paste(im,(465,75));d=ImageDraw.Draw(out)
f=ImageFont.truetype('DejaVuSans.ttf',18);small=ImageFont.truetype('DejaVuSans.ttf',15)
d.text((25,15),'Visible flow groups - reference analysis, NOT a new 3D render',font=f,fill='black')
d.text((25,47),'Unmarked reference (uniform 2x crop)',font=small,fill='black');d.text((465,47),'Directional design map (not root positions)',font=small,fill='black')
def xy(p):return (465+2*(p[0]-crop[0]),75+2*(p[1]-crop[1]))
def arrow(points,color):
 pp=[xy(p) for p in points];d.line(pp,fill=color,width=4,joint='curve');a,b=pp[-2:];v=(a[0]-b[0],a[1]-b[1]);L=math.hypot(*v);v=(v[0]/L,v[1]/L);n=(-v[1],v[0]);d.polygon([b,(b[0]+12*v[0]+6*n[0],b[1]+12*v[1]+6*n[1]),(b[0]+12*v[0]-6*n[0],b[1]+12*v[1]-6*n[1])],fill=color)
# The first endpoint is a visible sample, never an asserted root.
flows={'U1':[(388,112),(382,84),(367,57),(343,34)],'U2':[(312,97),(296,79),(275,62)],'F':[(370,122),(348,111),(324,116),(301,136),(281,167),(276,189)]}
for n,ps in flows.items():arrow(ps,'#16b6d9' if n.startswith('U') else '#ffbe25');d.text((xy(ps[1])[0]+8,xy(ps[1])[1]-10),n,font=f,fill='white',stroke_width=2,stroke_fill='black')
# Previously used selected edge. Only image locus is known.
a=xy((388,123));b=xy((374,142));d.line([a,b],fill='#ec4ea2',width=4);d.text((b[0]+8,b[1]+10),'J',font=f,fill='#ec4ea2',stroke_width=1,stroke_fill='black')
for y,t in [(590,'U1/U2: visible upward flow group. F: visible front/downward flow group.'),(614,'J: old selected boundary; NOT an observed shared root or required weld.'),(638,'Test priority: independent group guides + preserved overlap; hidden support remains unknown.'),(662,'Arrows summarize visible bands. They do not prove growth direction or hidden continuation.')]:d.text((25,y),t,font=small,fill='black')
out.save(P.parent.parent/'images'/'hair-flow-group-map'/'reference-flow-groups.png')
(P/'annotation-data.json').write_text(json.dumps({'crop':crop,'uniform_scale':2,'flow_samples':flows,'J_old_selected_edge':[[388,123],[374,142]],'classification':'reference analysis only','caution':'Flow is graphic direction, not proven anatomical growth direction. Hidden connectivity unknown.'},indent=2))
