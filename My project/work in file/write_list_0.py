text = "Первая строка"



import gzip            
with gzip.open(r"My project\work in file\list.gz", "wt") as f:
    f.write(text)
    


import bz2         
with bz2.open(r"My project\work in file\list.bz2", "wt") as f:
    f.write(text)
    
    

with gzip.open(r"My project\work in file\list.gz", "rt") as f:
    text = f.read()
    



with bz2.open(r"My project\work in file\list.bz2", "rt") as f:
    text = f.read()