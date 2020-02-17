import os
import shutil

path = "/Users/AMNS/Downloads/"
names = os.listdir(path)
folder_name = ['images', 'texts', 'videos', 'docx', 'ppt', 'xlsx', 'pdf', 'exe', 'archive', 'music']
print("Sorting")

for x in range(0,10):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
for files in names:
    #upgrade this code later
    if ".pdf" in files and not os.path.exists(path+'pdf/'+files):
        shutil.move(path+files, path+'pdf/'+files)
    if ".docx" in files and not os.path.exists(path+'docx/'+files):
        shutil.move(path+files, path+'docx/'+files)
    if ".doc" in files and not os.path.exists(path+'docx/'+files):
        shutil.move(path+files, path+'docx/'+files)
    if ".pptx" in files and not os.path.exists(path+'ppt/'+files):
        shutil.move(path+files, path+'ppt/'+files)
    if ".ppt" in files and not os.path.exists(path+'ppt/'+files):
        shutil.move(path+files, path+'ppt/'+files)
    if ".xlsx" in files and not os.path.exists(path+'xlsx/'+files):
        shutil.move(path+files, path+'xlsx/'+files)
    if ".xls" in files and not os.path.exists(path+'xlsx/'+files):
        shutil.move(path+files, path+'xlsx/'+files)
    if ".txt" in files and not os.path.exists(path+'texts/'+files):
        shutil.move(path+files, path+'texts/'+files)
    if ".zip" in files and not os.path.exists(path+'archive/'+files):
        shutil.move(path+files, path+'archive/'+files)
    if ".rar" in files and not os.path.exists(path+'archive/'+files):
        shutil.move(path+files, path+'archive/'+files)
    if ".png" in files and not os.path.exists(path+'images/'+files):
        shutil.move(path+files, path+'images/'+files)
    if ".jpg" in files and not os.path.exists(path+'images/'+files):
        shutil.move(path+files, path+'images/'+files)
    if ".bmp" in files and not os.path.exists(path+'images/'+files):
        shutil.move(path+files, path+'images/'+files)
    if ".mkv" in files and not os.path.exists(path+'videos/'+files):
        shutil.move(path+files, path+'videos/'+files)
    if ".mp4" in files and not os.path.exists(path+'videos/'+files):
        shutil.move(path+files, path+'videos/'+files)
    if ".7z" in files and not os.path.exists(path+'archive/'+files):
        shutil.move(path+files, path+'archive/'+files)
    if ".JPG" in files and not os.path.exists(path+'images/'+files):
        shutil.move(path+files, path+'images/'+files)
    if ".mp3" in files and not os.path.exists(path+'music/'+files):
        shutil.move(path+files, path+'music/'+files)
        break
    
print("Sorting Complete")
    