import os

cwd = os.getcwd()
d = 'wek'
def create_dirs():
    for i in range(1,6):
            os.mkdir(f"wek{i}")
    for i in range(1,6):
        for j in range(1,3):
            os.mkdir(os.path.join(cwd,f'wek{i}\\day{j}'))
            os.mkdir(os.path.join(cwd,f'wek{i}\\day{j}\\lesson'))
            os.mkdir(os.path.join(cwd,f'wek{i}\\day{j}\\homework'))

create_dirs()

print(os.path.join(cwd,))