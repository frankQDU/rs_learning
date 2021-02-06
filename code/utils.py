import os
import numpy as np
import pandas as pd

from tqdm import tqdm
from os.path import join,getsize

def get_file_info(path):
    import os
    from os.path import join,getsize
    for root, _, files in os.walk(path):
        for file in files:
            path_ = join(root, file).replace('\\','/')
            print(f'the size of {path_} is {round(getsize(path_)/(1024 ** 2) , 5)} M')