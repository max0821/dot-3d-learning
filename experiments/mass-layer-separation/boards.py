from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
O=Path(__file__).parent
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
names=['A-rounded-cylinder','B-native-pinch'];views=['front','side','back','oblique','tip']
b=Image.new('RGB',(2100,1060),'white');d=ImageDraw.Draw(b)
d.text((12,8),'Native Pinch review | actual Blender renders | A/B identical orthographic scale 200 px/unit',font=F,fill='black')
for i,n in enumerate(names):
 y=42+i*450
 for j,v in enumerate(views):
  b.paste(Image.open(O/f'{n}-{v}.png').convert('RGB'),(j*420,y));d.text((j*420+10,y+8),n+' / '+v,font=F,fill='white')
for i,s in enumerate(['RESULT: front silhouette narrows, but oblique / tip reveal a ridge-fin, not a clean all-around point.', 'Review of Soni Kumari steps 29-30, isolating Pinch only. Our brush settings/path are an adaptation.', 'Root masked. No Snake Hook, Smooth finishing, clump layering or root seam claim. B rejected for integration.']):d.text((12,955+i*31),s,font=F,fill='black')
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
for i,s in enumerate(['Visible reference spikes', 'have directional shapes;', 'this straight cylinder is', 'only a tool-control sample.', 'No hidden-root inference.', 'No quantitative fit claim.', 'A/B use same dimensions', 'and fixed cameras.']):d.text((8,520+i*38),s,font=F,fill='black')
for i,s in enumerate(['FAILURE: a sharper front outline concealed an undesirable fin in depth.', 'Next gap: control brush plane / stroke direction to taper the volume, not merely one projection.', 'No AI image editing. Original proportion preserved. iteration04 unchanged.']):d.text((12,935+i*31),s,font=F,fill='black')
b.save(O/'reference-comparison.png')
