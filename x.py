import os
path ="noteboo/research.ipynb"

dir,file=os.path.split(path)
os.makedirs(dir)

with open(path,"w")as f:
    pass