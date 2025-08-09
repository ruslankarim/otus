# отсекаю решения в которых нет хотя бы одного маркера -> судя по всему это решения не первой инстанции
import csv
import json
import re

# === Параметр: сколько строк читать из файла (0 — без ограничений) ===
max_rows = 0

def spaced_word_regex(word):
    return r'\s*'.join(f"[{c.lower()}{c.upper()}]" for c in word)

# === Регулярки начала и конца ===
start_pattern = re.compile(spaced_word_regex("установил"), re.IGNORECASE)
end_pattern = re.compile(spaced_word_regex("решил"), re.IGNORECASE)

# === Категориальные ключевые слова ===
category_keywords = {
    'civile': re.compile(r'гражданск', re.IGNORECASE),
    'bankruptcy': re.compile(r'банкрот', re.IGNORECASE),
    'administrative': re.compile(r'административ', re.IGNORECASE),
}

# Подготовим файлы заранее (вместо JSON файлов)
files = {
    'civile': open('civile.jsonl', 'w', encoding='utf-8'),
    'bankruptcy': open('bankruptcy.jsonl', 'w', encoding='utf-8'),
    'administrative': open('administrative.jsonl', 'w', encoding='utf-8'),
    'filtered': open('filtered_output.jsonl', 'w', encoding='utf-8'),
}

# === Статистика ===
stats = {
    'total_lines': 0,
    'both_matches': 0,
    'end_missing': 0,
    'start_missing': 0,
    'categories': {key: 0 for key in category_keywords},
    'without_category': 0,
    'index_solution_no_match_category_common': [],
    'index_solution_no_match_category_civile': [],
    'index_solution_no_match_category_bankruptcy': [],
    'index_solution_no_match_category_administrative': [],
    'index_solution_not_start_common': [],
    'index_solution_not_start_civile': [],
    'index_solution_not_start_bankruptcy': [],
    'index_solution_not_start_administrative': [],
    'index_solution_not_end_common': [],
    'index_solution_not_end_civile': [],
    'index_solution_not_end_bankruptcy': [],
    'index_solution_not_end_administrative': [],
}

count_solution_common = 0
count_solution_civile = 0
count_solution_bankruptcy = 0
count_solution_administrative = 0

with open('sentences_output_test.jsonl', 'r', encoding='utf-8') as infile:
    for line in infile:
        if 0 < max_rows <= stats['total_lines']:
            break

        stats['total_lines'] += 1
        try:
            items = json.loads(line.strip())
            if not isinstance(items, list):
                continue
        except json.JSONDecodeError:
            continue

        # Определение категории
        matched_category = None
        for category, pattern in category_keywords.items():
            if pattern.search(items[0]):
                matched_category = category
                break

        if matched_category is None:
            count_solution_common += 1
        elif matched_category == 'civile':
            count_solution_civile += 1
        elif matched_category == 'bankruptcy':
            count_solution_bankruptcy += 1
        elif matched_category == 'administrative':
            count_solution_administrative += 1

        # Поиск начала и конца
        start_idx = next((i for i, s in enumerate(items) if start_pattern.search(s)), None)
        end_idx = next((i for i in range(len(items) - 1, -1, -1) if end_pattern.search(items[i])), None)
        if end_idx is not None:
            end_idx -= 1

        result = []
        if start_idx is not None and end_idx is not None and start_idx < end_idx:
            result = items[start_idx + 1:end_idx]
            stats['both_matches'] += 1
        elif start_idx is not None and end_idx is None:
            result = False
            stats['start_missing'] += 1
            key = f"index_solution_not_end_{matched_category or 'common'}"
            stats[key].append(eval(f"count_solution_{matched_category or 'common'}"))
        elif start_idx is None and end_idx is not None:
            result = False
            stats['end_missing'] += 1
            key = f"index_solution_not_start_{matched_category or 'common'}"
            stats[key].append(eval(f"count_solution_{matched_category or 'common'}"))
        elif start_idx is None and end_idx is None:
            key = f"index_solution_no_match_category_{matched_category or 'common'}"
            stats[key].append(eval(f"count_solution_{matched_category or 'common'}"))

        if result:
            out_file = files[matched_category] if matched_category else files['filtered']
            json.dump(result, out_file, ensure_ascii=False)
            out_file.write('\n')
            if matched_category:
                stats['categories'][matched_category] += 1

# Закрытие файлов
for f in files.values():
    f.close()

# === Статистика ===
print(f"Обработано строк: {stats['total_lines']}")
for cat, count in stats['categories'].items():
    print(f"{cat}: {count} строк (категория)")
print(f"Без категории: {stats['without_category']}")
print(f"Решений принятых в датасет: {stats['both_matches']}")
print(f"Решения не принятых в датасет, причина: нет второго маркера: {stats['end_missing']}")
print(f"Решения не принятых в датасет, причина: нет первого маркера: {stats['start_missing']}")
print(f"Решения не принятых в датасет, всего: {stats['start_missing'] + stats['end_missing']}")
print(f"Индексы решений, где не было обоих маркеров (без категории): {stats['index_solution_no_match_category_common']}")
print(f"Индексы решений, где не было обоих маркеров (гражданские): {stats['index_solution_no_match_category_civile']}")
print(f"Индексы решений, где не было обоих маркеров (банкротные): {stats['index_solution_no_match_category_bankruptcy']}")
print(f"Индексы решений, где не было обоих маркеров (административные): {stats['index_solution_no_match_category_administrative']}")
print(f"Индексы решений, где не было маркера начала (без категории): {stats['index_solution_not_start_common']}")
print(f"Индексы решений, где не было маркера начала (гражданские): {stats['index_solution_not_start_civile']}")
print(f"Индексы решений, где не было маркера начала (банкротные): {stats['index_solution_not_start_bankruptcy']}")
print(f"Индексы решений, где не было маркера начала (административные): {stats['index_solution_not_start_administrative']}")
print(f"Индексы решений, где не было маркера конца (без категории): {stats['index_solution_not_end_common']}")
print(f"Индексы решений, где не было маркера конца (гражданские): {stats['index_solution_not_end_civile']}")
print(f"Индексы решений, где не было маркера конца (банкротные): {stats['index_solution_not_end_bankruptcy']}")
print(f"Индексы решений, где не было маркера конца (административные): {stats['index_solution_not_end_administrative']}")
print("Результаты записаны в: civile.jsonl, bankruptcy.jsonl, administrative.jsonl, filtered_output.jsonl")
