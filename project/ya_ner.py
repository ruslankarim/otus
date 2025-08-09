from natasha import (
    Segmenter, NewsEmbedding, NewsNERTagger, Doc
)

segmenter = Segmenter()
emb = NewsEmbedding()
ner_tagger = NewsNERTagger(emb)

text = "В 2020 году судья Иванов А.А. рассматривал дело против ООО Ромашка в Москве."
doc = Doc(text)

doc.segment(segmenter)
doc.tag_ner(ner_tagger)

for span in doc.spans:
    print(span.text, '→', span.type)
