from nltk.tokenize import WordPunctTokenizer
from subword_nmt.learn_bpe import learn_bpe
from subword_nmt.apply_bpe import BPE

tokenizer = WordPunctTokenizer()


def tokenize(x):
    return ' '.join(tokenizer.tokenize(x.lower()))


# # сплит и токенизация данных
# with open('train.en', 'w', encoding='utf-8') as f_src, open('train.ru', 'w', encoding='utf-8') as f_dst:
#     for line in open('data.txt', encoding='utf-8'):
#         src_line, dst_line = line.strip().split('\t')
#         f_src.write(tokenize(src_line) + '\n')
#         f_dst.write(tokenize(dst_line) + '\n')

# создание BPE словаря и его применение к данным
bpe = {}
for lang in ['en', 'ru']:
    learn_bpe(open('./train.' + lang, encoding='utf-8'), open('bpe_rules.' + lang, 'w', encoding='utf-8'),
              num_symbols=8000)
    bpe[lang] = BPE(open('./bpe_rules.' + lang))

    with open('train.bpe.' + lang, 'w', encoding='utf-8') as f_out:
        for line in open('train.' + lang, encoding='utf-8'):
            f_out.write(bpe[lang].process_line(line.strip()) + '\n')
