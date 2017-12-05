import os

lists=os.listdir('./')
lists.sort(key=lambda f:os.path.getmtime(f))
print(lists[-1])
