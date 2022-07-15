import os

def __init__():
    pass

def get_data(path = '../src/data'):
    os.system('kaggle competitions download -c spaceship-titanic')
    os.system(f'move spaceship-titanic.zip {path}')