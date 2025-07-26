import numpy as np
import torch
torch.set_printoptions(edgeitems=2, threshold=50)

with open('1342-0.txt', encoding='utf8') as f:
    text = f.read()

lines = text.split('\n')
line = lines[200]

print(line)