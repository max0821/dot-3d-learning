from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
O=Path(__file__).resolve().parent
P=O/'history' if (O/'history').is_dir() else O.parent/'mass-layer-separation'
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',19)
b=Image.new('RGB',(2100,1510),'white');d=ImageDraw.Draw(b)
d.text((12,8),'Transverse-row taper | native Blender adaptation | actual orthographic renders, 200 px/unit',font=F,fill='black')
for i,(folder,n,label) in enumerate([(O,'A-regular-grid','A / new regular grid'),(O,'B-row-taper','B / row taper + tip weld'),(P,'B-native-pinch','HISTORY / Pinch, different topology')]):
 y=42+450*i
 for j,v in enumerate(['front','side','back','oblique','tip']):
  b.paste(Image.open(folder/f'{n}-{v}.png').convert('RGB'),(420*j,y));d.text((420*j+8,y+8),label,font=F,fill='white');d.text((420*j+8,y+36),v,font=F,fill='white')
for i,s in enumerate(['A -> B uses the same input grid; full rings shrink around their centers, length stays fixed; collapsed tip welded.', 'Historical Pinch has different topology / stroke / construction. This is NOT an isolated tool-performance comparison.', 'B is a rotational local control sample, NOT a finished hair clump, reference fit or character improvement.']):d.text((12,1400+i*31),s,font=F,fill='black')
b.save(O/'comparison-board.png')
b=Image.new('RGB',(1260,1040),'white');d=ImageDraw.Draw(b)
d.text((12,8),'Visible reference vs local control sample | qualitative only, no matched character fit',font=F,fill='black')
refpath=O/'reference.png' if (O/'reference.png').exists() else O.parents[1]/'images/reference/character-three-views.png'
ref=Image.open(refpath).convert('RGB').crop((245,0,455,210)).resize((420,420));b.paste(ref,(0,45))
d.text((8,470),'Reference crop: uniform 2x',font=F,fill='black')
for j,n in enumerate(['A-regular-grid','B-row-taper'],1):
 for v,y in [('front',45),('oblique',490)]:
  b.paste(Image.open(O/f'{n}-{v}.png').convert('RGB'),(420*j,y));d.text((420*j+8,y+8),n+' / '+v,font=F,fill='white')
for i,s in enumerate(['Reference has leaning,', 'asymmetric, layered spikes.', 'The symmetric sample', 'only tests circumferential', 'tip-volume control.', 'Root flow and silhouette', 'matching remain untested.', 'No hidden-depth claim.']):d.text((8,520+i*38),s,font=F,fill='black')
for i,s in enumerate(['B avoids a fin in this controlled sample, but is still generic and does not reproduce the visible hairstyle.', 'New learning: select full transverse rows; preserve flow/length; respect grid topology. Old taper principle reviewed.', 'No unknown addon executed. iteration04 unchanged.']):d.text((12,935+i*31),s,font=F,fill='black')
b.save(O/'reference-comparison.png')
