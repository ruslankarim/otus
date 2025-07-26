import csv
import json
import re
import nltk
from nltk.tokenize.punkt import PunktParameters
from nltk.data import load

csv.field_size_limit(500000)

# === Подготовка NLTK ===
try:
    nltk.download('punkt')
    tokenizer = load('tokenizers/punkt/russian.pickle')
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    tokenizer._params.abbrev_types.update(punkt_param.abbrev_types)
    use_nltk = True
    print("Используем NLTK токенайзер для русского языка")
except:
    use_nltk = False
    print("NLTK недоступен, используем простое разбиение на предложения")

# === Функция fallback-токенизации ===
def simple_sent_tokenize(text):
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]

# === Параметры ===
max_rows = 500  # 0 = без ограничения, >0 = обрабатывать только первые N строк
output_file = 'sentences_output_test.jsonl'

# === Обработка CSV и сохранение JSONL ===
processed_rows = 0
total_sentences = 0

with open('solution.csv', 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)

    for i, row in enumerate(reader):
        if max_rows > 0 and i >= max_rows:
            break

        text = row.get('text_sol', '')

        if text and text.strip():
            if use_nltk:
                raw_sentences = tokenizer.tokenize(text.strip())
            else:
                raw_sentences = simple_sent_tokenize(text.strip())

            # Разбиваем по строкам (вдруг внутри предложения есть переносы)
            new_sentences = [part.strip()
                             for sentence in raw_sentences
                             for part in sentence.split('\n')
                             if part.strip()]

            # Пишем каждую строку как JSON-массив в формате JSONL
            json.dump(new_sentences, outfile, ensure_ascii=False)
            outfile.write('\n')

            processed_rows += 1
            total_sentences += len(new_sentences)

print(f"Обработано строк: {processed_rows}")
print(f"Всего предложений: {total_sentences}")
print(f"Результат сохранен в файл '{output_file}' в формате JSONL")
