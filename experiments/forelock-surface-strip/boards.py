from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,math
P=Path(__file__).resolve().parent
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20);sm=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17)
b=Image.new('RGB',(1920,1150),'white');d=ImageDraw.Draw(b)
d.text((15,12),'SINGLE-TIP SURFACE STRIP / failed closest-surface adaptation / no baseline promotion',font=f,fill='black')
for row,label in enumerate(['A-old-double-tip','B-conformed-single-tip']):
 y=55+530*row;d.text((15,y),['A: current registered three-lock context; depth Y0 remains unverified. Actual rerender.','B: new open-root strip, whole-strip closest projection to 04 head. Silhouette collapsed; failed.'][row],font=f,fill='black')
 for j,v in enumerate(['front','side','back','oblique']):
  b.paste(Image.open(P/f'{label}-{v}.png'),(j*480,y+30));d.text((j*480+12,y+38),v,font=f,fill='white')
d.text((15,1120),'The author starts NEAR the forehead. Our distant workplane + whole-strip projection did not satisfy this condition.',font=f,fill='black');b.save(P/'comparison-board.png')
r=json.loads((P/'source-input/registration-metrics.json').read_text());ref=Image.open(P/'source-input/reference.png').convert('RGB');box=r['front_render_source_window'];pad=Image.new('RGB',(ref.width+200,ref.height+200),'white');pad.paste(ref,(100,100));crop=pad.transform((480,480),Image.Transform.EXTENT,[v+100 for v in box],Image.Resampling.BICUBIC)
b=Image.new('RGB',(1440,680),'white');d=ImageDraw.Draw(b)
for i,(im,label) in enumerate([(crop,'SOURCE / historic uniform scale'),(Image.open(P/'A-old-double-tip-front.png'),'A / old double-ended forelock'),(Image.open(P/'B-conformed-single-tip-front.png'),'B / failed surface conformation')]):
 d.text((i*480+8,12),label,font=sm,fill='black');b.paste(im,(i*480,45))
 for py,c in [(333,(60,150,200)),(123,(210,100,40)),(215,(100,150,80))]:
  y=45+round((py-box[1])*480/382.5);d.line((480*i,y,480*(i+1)-1,y),fill=c,width=1)
for i,t in enumerate(['Same square source window and equal X/Y scale; no reference stretch.', 'Orange: historic root-image level; green: distal tip-image level; blue: chin. These do NOT constrain depth.', 'B loses the visible front arc and does not meet the cap. Open root topology alone is not hair-root design.', 'Do not repeat this whole-strip projection. Support region must be identified before free silhouette extension.']):d.text((12,545+30*i),t,font=sm,fill='black')
b.save(P/'reference-comparison.png')
r=json.loads((P/'RESULTS.json').read_text());outer=[(388,123),(353,96),(316,98),(281,119),(266,160)];inner=[(374,142),(356,116),(325,139),(303,168),(286,197)];coords=[]
for l,rr in zip(outer,inner):
 for k in range(5):
  u=k/4;px=l[0]*(1-u)+rr[0]*u;py=l[1]*(1-u)+rr[1]*u;coords.append(((px-345)/153,-1,2.72+(333-py)/153))
coords.append(((280-345)/153,-1,2.72+(333-215)/153))
r['pre_projection_cage_xyz']=coords;r['max_xz_displacement']=max(math.hypot(a[0]-b[0],a[2]-b[2]) for a,b in zip(coords,r['projected_cage_xyz']));r['root_length_before']=math.hypot(14,19)/153;r['root_length_after']=r['root_edge_length'];r['status']='FAILED: distant seed plane and whole-strip closest mapping violate near-surface prerequisite; free silhouette lost';(P/'RESULTS.json').write_text(json.dumps(r,indent=2))
print(r['max_xz_displacement'],r['root_length_before'],r['root_length_after'])
