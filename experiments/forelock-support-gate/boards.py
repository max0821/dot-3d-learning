from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
P=Path(__file__).resolve().parent;f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20);sm=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17)
b=Image.new('RGB',(1920,1170),'white');d=ImageDraw.Draw(b)
d.text((15,10),'SUPPORT APPLICABILITY / Diagnostic rerender of unchanged old hair, NOT a new hair model',font=f,fill='black')
for row in range(2):
 y=50+530*row;d.text((15,y),['PRIOR F26 FAILURE: whole-strip Closest collapsed the silhouette. Previous render, not a new result.','CURRENT GATE: original context preserved. Orange = selected visible junction; cyan = head maximum height.'][row],font=f,fill='black')
 for j,v in enumerate(['front','side','back','oblique']):
  p=P/f'gate-{v}.png' if row else P/'source-input'/f'B-conformed-single-tip-{v}.png'
  b.paste(Image.open(p),(j*480,y+30));d.text((j*480+12,y+38),v,font=f,fill='white')
d.text((15,1120),'Root-only Y projection: 0/5 hits, unchanged vertices. This junction is above the entire preserved head surface.',font=f,fill='black');d.text((15,1146),'Do not move it down with Closest or enlarge the hidden head to force success. Direct wrap is not applicable here.',font=sm,fill='black');b.save(P/'comparison-board.png')
r=json.loads((P/'source-input/registration-metrics.json').read_text());box=r['front_render_source_window'];ref=Image.open(P/'source-input/reference.png').convert('RGB');pad=Image.new('RGB',(ref.width+200,ref.height+200),'white');pad.paste(ref,(100,100));crop=pad.transform((480,480),Image.Transform.EXTENT,[v+100 for v in box],Image.Resampling.BICUBIC)
b=Image.new('RGB',(1440,720),'white');d=ImageDraw.Draw(b)
for i,(im,label) in enumerate([(crop,'SOURCE / junction is not proven root'),(Image.open(P/'source-input/B-conformed-single-tip-front.png'),'PRIOR F26 / collapsed strip'),(Image.open(P/'gate-front.png'),'CURRENT / unchanged hair + markers')]):
 d.text((i*480+8,12),label,font=sm,fill='black');b.paste(im,(i*480,45))
 for py,c in [(123,(240,90,30)),(142,(240,90,30)),(157.1773,(0,170,210))]:
  y=45+round((py-box[1])*480/382.5);d.line((480*i,y,480*(i+1)-1,y),fill=c,width=1)
for i,t in enumerate(['Same uniform reference scale and camera framing; source image was not stretched.', 'Orange band: historical visible junction y123-142; cyan: maximum head height projected at y157.18.', 'These guide levels demonstrate this direct support mismatch, NOT the hidden scalp or anatomical hair root.', 'Next question: can a lower surface support connect to the visible junction through a separate free transition?', 'No new hair shape, no baseline promotion; the prior root interpretation remains a design hypothesis.']):d.text((12,545+30*i),t,font=sm,fill='black')
b.save(P/'reference-comparison.png')
