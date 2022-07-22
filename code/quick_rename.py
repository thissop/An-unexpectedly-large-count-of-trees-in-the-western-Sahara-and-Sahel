import os 
import shutil
def quick_rename(new_number, old_dir:str='/mnt/c/Users/Research/Documents/GitHub/africa-trees/data/first_mosaic/annotations/ready/temp_output/'): 
    
    new_dir = old_dir.replace('temp_output', 'output')
    for file in os.listdir(old_dir):
        old_path = old_dir+file
        new_path = new_dir+file.replace('_0', '_'+str(new_number))
        shutil.copyfile(old_path,new_path)
        os.remove(old_path)
quick_rename(9)