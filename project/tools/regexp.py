import re
from pregex.core.classes import AnyDigit
from pregex.core.pre import Pregex
from pregex.core.tokens import Space

point = 'пункт[а-яА-ЯёЁ]{,3}' #пункт/пунктом ...
point_short = 'п\.|п' #п.
sub_point = 'подпункт[а-яА-ЯёЁ]{,3}' #подпункт/подпунктом ...
sub_point_short = 'п\.п\.|пп.|пп' #п.п./пп./пп
article = 'стат[а-яА-ЯёЁ]{1,3}' #статья/статьи ...
article_short = 'ст\.|ст' #ст.
paragraph = 'абзац[а-яА-ЯёЁ]{,3}' #абзац/абзаца ...
digits = r'[1-9]+' #123
digits_point = r'(\.[1-9][0-9]*)+' # .1 или .123...
num_words = '(перв|втор|трет|четверт|пят|шест|седьм|восьм|девят|десят|одиннадцат|двенадцат)[а-яА-ЯёЁ]{1,3}'
comma = ','
and_word = 'и'

any_cyrillic = Pregex('[а-яА-ЯёЁ]', False)
paragraph_pre = Pregex(paragraph, False)
point_pre = Pregex(point_short, False)
point_short_pre = Pregex(point, False)
sub_point_pre = Pregex(sub_point, False)
sub_point_short_pre = Pregex(sub_point_short, False)
article_pre = Pregex(article, False)
article_short_pre = Pregex(article_short, False)

and_word_pre = Pregex(and_word, False)
num_words_pre = Pregex(num_words, False)
and_pre = Pregex(and_word, False)
hyphen_pre = Pregex('[-–—]', False)
comma_pre = Pregex(',', False)

test = any_cyrillic.concat(num_words_pre)
print("")

paragraph_num_word_comma_and_num_word_pre = paragraph_pre.concat(Space().at_least(1)).concat(num_words_pre).concat(
    (comma_pre.concat(Space().at_least(1)).concat(num_words_pre)).at_least(1))

patterns_paragraph = {
    "абзац число прописью, число прописью (более одного) и число прописью - число прописью":
        paragraph_num_word_comma_and_num_word_pre
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(num_words_pre)
        .concat(Space().at_least(1)).concat(hyphen_pre).concat(Space().at_least(1))
        .concat(num_words_pre),

    "абзац число, число (более одного) и число - число":
        paragraph_pre
        .concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1))
        .concat((comma_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1))).at_least(1))
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1))
        .concat(Space().at_least(1)).concat(hyphen_pre).concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1)),

    "абзац число прописью, число прописью (более одного) и число прописью":
        paragraph_num_word_comma_and_num_word_pre
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(num_words_pre),

    "абзац число, число (более одного) и число":
        paragraph_pre
        .concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1))
        .concat((comma_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1))).at_least(1))
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1)),

    "абзац число прописью и число прописью - число прописью":
        paragraph_pre
        .concat(Space().at_least(1))
        .concat(num_words_pre)
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(num_words_pre)
        .concat(Space().at_least(1)).concat(hyphen_pre).concat(Space().at_least(1))
        .concat(num_words_pre),

    "абзац число и число - число":
        paragraph_pre
        .concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1))
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1))
        .concat(Space().at_least(1)).concat(hyphen_pre).concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1)),

    "абзац число прописью и число прописью": paragraph_pre.concat(Space().at_least(1))
        .concat(num_words_pre).concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1)).concat(num_words_pre),

    "абзац число и число":
        paragraph_pre
        .concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1))
        .concat(Space().at_least(1)).concat(and_pre).concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1)),

    "абзац число прописью":
        paragraph_pre.concat(Space().at_least(1))
        .concat(num_words_pre),

    "абзац число":
        paragraph_pre.concat(Space().at_least(1))
        .concat(AnyDigit().at_least(1)),
}

patterns_sub_point = {
    "подпункт число": sub_point_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1)),
    "п.п./пп./пп число": sub_point_short_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1)),
}


patterns_point = {
    "пункт число": point_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1)),
    "п./п число": point_short_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1)),
}

patterns_article = {
    "статья число": point_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1)),
    "ст./ст число": point_short_pre.concat(Space().at_least(1)).concat(AnyDigit().at_least(1)),
}


def find(text, patterns):
    """
    Ищет первый паттерн абзаца в куске текста.
    Возвращает capture, если найдено, иначе None.
    """
    for key, pattern in patterns.items():
        capture = pattern.get_matches(text)
        if capture:
            return capture, pattern
    return None, None

def get_address_norm_in_act(text):
    """
    Находит в тексте абзацы и обрабатывает их по patterns_paragraph.
    При нахождении capture сразу переходит к следующему chunk.
    """
    # Находим все вхождения "абзац[...]" и получаем индексы
    matches = list(re.finditer(paragraph_pre.get_pattern(), text))
    indexes = [m.start() for m in matches] + [len(text)]

    # Формируем список кусков между индексами
    chunks = [
        text[indexes[i]:indexes[i + 1]].strip()
        for i in range(len(indexes) - 1)
    ]

    # Перебираем chunks и ищем паттерны абзаца
    for chunk in chunks:
        capture, pattern_paragraph = find(chunk, patterns_paragraph)
        if capture:
            # переходим к следующему chunk
            # print(f"{capture} {pattern_paragraph}")
            if sub_point_pre.get_matches(chunk):
                followed_sub_point_pre = {}
                for key, pattern_sub_point in patterns_sub_point.items():
                    followed_sub_point_pre[key] = pattern_paragraph.concat(Space().at_least(1)).concat(pattern_sub_point)
                capture, pattern_paragraph_sub_point = find(chunk, followed_sub_point_pre)
                if capture:
                    if point_pre.get_matches(chunk):
                        followed_point_pre = {}
                        for key, pattern_point in patterns_point.items():
                            followed_point_pre[key] = pattern_paragraph_sub_point.concat(Space().at_least(1)).concat(pattern_point)
                        capture, pattern_paragraph_point = find(chunk, followed_point_pre)
                        if capture:
                            print(f"{capture} {pattern_paragraph_point}")
                            continue
            elif point_pre.get_matches(chunk):
                followed_point_pre = {}
                for key, pattern_point in patterns_point.items():
                    followed_point_pre[key] = pattern_paragraph.concat(Space().at_least(1)).concat(pattern_point)
                capture, pattern_paragraph_point = find(chunk, followed_point_pre)
                if capture:
                    print(f"{capture} {pattern_paragraph_point}")
                    continue
                continue