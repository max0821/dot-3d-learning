from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
O=Path(__file__).parent
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
names=['B-native-pinch','C-fixed-z-pinch'];views=['front','side','back','oblique','tip']
b=Image.new('RGB',(2100,1060),'white');d=ImageDraw.Draw(b)
d.text((12,8),'Pinch plane control | B: AREA / C: fixed Z | actual renders, same cameras 200 px/unit',font=F,fill='black')
for i,n in enumerate(names):
 y=42+i*450
 for j,v in enumerate(views):
  b.paste(Image.open(O/f'{n}-{v}.png').convert('RGB'),(j*420,y));d.text((j*420+10,y+8),n+' / '+v,font=F,fill='white')
for i,s in enumerate(['RESULT: fixing the brush normal to Z did NOT remove the ridge-fin. Both trials fail as clean hair tips.', 'Same input, mask, 41-event path, strength and radius. Only sculpt_plane changed from AREA to Z.', 'AREA replay equals the previous result. This does not identify stroke direction as the sole cause. No integration.']):d.text((12,955+i*31),s,font=F,fill='black')
b.save(O/'comparison-board.png')
b=Image.new('RGB',(1260,1040),'white');d=ImageDraw.Draw(b)
d.text((12,8),'Reference vs isolated tool trial: qualitative shape check, NOT a matched character fit.',font=F,fill='black')
p=O/'reference.png'
if not p.exists():p=O.parents[1]/'images/reference/character-three-views.png'
ref=Image.open(p).convert('RGB').crop((245,0,455,210)).resize((420,420));b.paste(ref,(0,45))
d.text((8,470),'Reference crop: uniform 2x',font=F,fill='black')
for j,n in enumerate(names,1):
 b.paste(Image.open(O/f'{n}-front.png').convert('RGB'),(j*420,45));d.text((j*420+8,52),n+' / front',font=F,fill='white')
 b.paste(Image.open(O/f'{n}-oblique.png').convert('RGB'),(j*420,490));d.text((j*420+8,498),n+' / oblique',font=F,fill='white')
for i,s in enumerate(['Visible reference spikes', 'have directional shapes;', 'this straight cylinder is', 'only a tool-control sample.', 'No hidden-root inference.', 'No quantitative fit claim.', 'B/C use same dimensions', 'and fixed cameras.']):d.text((8,520+i*38),s,font=F,fill='black')
for i,s in enumerate(['NEGATIVE RESULT: a fixed normal alone does not turn this circular Pinch stroke into a clean point.', 'Next gap: an author-demonstrated stroke pattern, not another plane / strength sweep.', 'No AI image editing. Original proportion preserved. iteration04 unchanged.']):d.text((12,935+i*31),s,font=F,fill='black')
b.save(O/'reference-comparison.png')
