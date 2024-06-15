from collections import Counter
import numpy as np
import torch
import torch.nn.functional as F
from torch import nn, optim
from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pad_packed_sequence

class Dataset(torch.utils.data.Dataset):
    def __init__(
        self,
        lines,
    ):
        self.lines = lines
        self.pad_token = '<PAD>'
        self.bos_token = '<BOS>'
        self.eos_token = '<EOS>'
        self.uniq_words = [self.pad_token, self.bos_token, self.eos_token] + self.get_uniq_words()

        self.index_to_word = {index: word for index, word in enumerate(self.uniq_words)}
        self.word_to_index = {word: index for index, word in enumerate(self.uniq_words)}

        self.pad_token_id = self.word_to_index['<PAD>']
        self.bos_token_id = self.word_to_index['<BOS>']
        self.eos_token_id = self.word_to_index['<EOS>']

        self.tokenized = [[self.word_to_index[w] for w in line.split()] for line in self.lines]

    def get_uniq_words(self):
        word_counts = Counter(word for line in self.lines for word in line.split())
        return sorted(word_counts, key=word_counts.get, reverse=True)

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return (
            torch.LongTensor([self.bos_token_id] + self.tokenized[index]),
            torch.LongTensor(self.tokenized[index] + [self.eos_token_id]),
        )
    
def preprocess(line):
    return ' '.join(w.lower() for w in (''.join(ch for ch in word if ch.isalpha()) for word in line.split()) if w)    

def pad_collate(batch):
    (xx, yy) = zip(*batch)
    x_lens = [len(x) for x in xx]
    y_lens = [len(y) for y in yy]

    xx_pad = pad_sequence(xx, batch_first=True, padding_value=dataset.pad_token_id)
    yy_pad = pad_sequence(yy, batch_first=True, padding_value=dataset.pad_token_id)

    return xx_pad, yy_pad, x_lens, y_lens