from utils import Dataset, preprocess, pad_collate
from torch.utils.data import DataLoader


with open('poslo1.txt', encoding='utf-8') as f:
    lines = f.readlines()

dataset = Dataset([preprocess(line) for line in lines])


dataloader = DataLoader(dataset, batch_size=512, collate_fn=pad_collate, shuffle=True)

print()


