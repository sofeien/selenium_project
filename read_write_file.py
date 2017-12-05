import os

dir_path = r'E:/selenium/'

for item in os.listdir(dir_path):
    if os.path.isfile(dir_path+item) and item.endswith(".txt") :
        for line in open(dir_path+item,'r',encoding="utf-8"):
            print(line.strip())
        
