import os
import shutil

path = "A:/Users/Naveen/Downloads/C102_assets-main"
print("before coping file")
print(os.listdir(path))

src = "A:/Users/Naveen/Downloads/C102_assets-main/C102_assets-main/feather.jfif"
dest = "A:/Users/Naveen/Downloads/C102_assets-main/capyfeather.jfif"
destination = shutil.copy(src,dest)
print("after coping file")
print(os.listdir(path))