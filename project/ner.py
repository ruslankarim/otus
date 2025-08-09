from natasha import (
    Segmenter, MorphVocab,
    NewsEmbedding, NewsNERTagger,
    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
ner_tagger = NewsNERTagger(emb)

def remove_named_entities(text):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)
    tokens_to_remove = set()

    for span in doc.spans:
        span.normalize(morph_vocab)
        tokens_to_remove.add(span.text)

    for token in tokens_to_remove:
        text = text.replace(token, '')

    return ' '.join(text.split())
