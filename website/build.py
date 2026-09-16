from pathlib import Path
import shutil
root=Path(__file__).parent
out=root/'dist'
if out.exists(): shutil.rmtree(out)
out.mkdir()
for p in root.iterdir():
 if p.suffix in ('.html','.css','.js','.txt','.xml','.webmanifest'): shutil.copy2(p,out/p.name)
shutil.copytree(root/'assets',out/'assets')
print('Built static Cake Club website in dist/')
