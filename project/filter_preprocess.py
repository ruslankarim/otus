import json
import re


# === Параметр: сколько строк читать из файла (0 — без ограничений) ===
max_rows = 0  # Например, 10 — прочитать только 10 строк; 0 — все строки

def spaced_word_regex(word):
    return r'\s*'.join(f"[{c.lower()}{c.upper()}]" for c in word)
# === Регулярки начала и конца ===
start_pattern = spaced_word_regex("установил")
end_pattern = spaced_word_regex("решил")

# === Категориальные ключевые слова ===
category_keywords = {
    'civile': r'гражданское',
    'bankruptcy': r'банкротное',
    'administrative': r'административное',
}

# === Файлы для записи ===
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
    'no_match': 0,
    'start_missing': 0,
    'categories': {key: 0 for key in category_keywords},
    'index_solution_no_match_common': [],
    'index_solution_no_match_civile': [],
    'index_solution_no_match_bankruptcy': [],
    'index_solution_no_match_administrative': [],
    'index_solution_not_start_common': [],
    'index_solution_not_start_civile': [],
    'index_solution_not_start_bankruptcy': [],
    'index_solution_not_start_administrative': [],
    'index_solution_not_end_common': [],
    'index_solution_not_end_civile': [],
    'index_solution_not_end_bankruptcy': [],
    'index_solution_not_end_administrative': [],
}
is_category = None
# индекс решения
count_solution_common = 0
count_solution_civile = 0
count_solution_bankruptcy =  0
count_solution_administrative = 0

# === Основной цикл ===
with open('sentences_output_test.jsonl', 'r', encoding='utf-8') as infile:
    for line in infile:
        if 0 < max_rows <= stats['total_lines']:
            break

        stats['total_lines'] += 1
        is_category = True
        try:
            items = json.loads(line.strip())

            if not isinstance(items, list):
                continue
        except json.JSONDecodeError:
            continue

        matched_category = None
        for category, keyword in category_keywords.items():
            if keyword.lower() in items[0].lower():
                matched_category = category
                break

        if matched_category is None:
            count_solution_common += 1
        else:
            if matched_category == 'civile':
                count_solution_civile += 1
            elif matched_category == 'bankruptcy':
                count_solution_bankruptcy += 1
            elif matched_category == 'administrative':
                count_solution_administrative += 1

        # Поиск начала и конца в любом месте строки (не только с начала)
        start_idx = next((i for i, s in enumerate(items) if re.search(start_pattern, s)), None)
        end_idx = next((i for i in range(len(items) - 1, -1, -1) if re.search(end_pattern, items[i])), None)
        if end_idx is not None:
            end_idx -= 1

        if end_idx is not None and start_idx is not None:
            result = items[start_idx + 1:end_idx]
            stats['both_matches'] += 1
        elif start_idx is not None and end_idx is None:
            result = items[start_idx + 1 : len(items)-1]
            stats['start_missing'] += 1
            if matched_category == 'civile':
                stats['index_solution_not_end_civile'].append(count_solution_civile)
            elif matched_category == 'bankruptcy':
                stats['index_solution_not_end_bankruptcy'].append(count_solution_bankruptcy)
                print(result)
            elif matched_category == 'administrative':
                stats['index_solution_not_end_administrative'].append(count_solution_administrative)
            elif matched_category is None:
                stats['index_solution_not_end_common'].append(count_solution_common)
        elif start_idx is None and end_idx is not None:
            result = items[0 :end_idx]
            stats['end_missing'] += 1
            if matched_category == 'civile':
                stats['index_solution_not_start_civile'].append(count_solution_civile)
            elif matched_category == 'bankruptcy':
                stats['index_solution_not_start_bankruptcy'].append(count_solution_bankruptcy)
            elif matched_category == 'administrative':
                stats['index_solution_not_start_administrative'].append(count_solution_administrative)
            elif matched_category is None:
                stats['index_solution_not_start_common'].append(count_solution_common)
        else:
            stats['no_match'] += 1


        if result:
            if matched_category:
                json.dump(result, files[matched_category], ensure_ascii=False)
                files[matched_category].write('\n')
                stats['categories'][matched_category] += 1
            else:
                json.dump(result, files['filtered'], ensure_ascii=False)
                files['filtered'].write('\n')

# Закрываем файлы
for f in files.values():
    f.close()

# Итоги
print(f"Обработано строк: {stats['total_lines']}")
for cat, count in stats['categories'].items():
    print(f"{cat}: {count} строк (категория)")
print(f"Фильтрация — оба совпадения: {stats['both_matches']}")
print(f"Фильтрация — только start (без end): {stats['end_missing']}")
print(f"Фильтрация — только end (нет start): {stats['start_missing']}")
print(f"Фильтрация — пустые после обрезки: {stats['no_match']}")
print(f"Индексы решений, где не было обоих маркеров (без категории): {stats['index_solution_no_match_common']}")
print(f"Индексы решений, где не было обоих маркеров (гражданские): {stats['index_solution_no_match_civile']}")
print(f"Индексы решений, где не было обоих маркеров (банкротные): {stats['index_solution_no_match_bankruptcy']}")
print(f"Индексы решений, где не было обоих маркеров (административные): {stats['index_solution_no_match_administrative']}")
print(f"Индексы решений, где не было маркера начала (без категории): {stats['index_solution_not_start_common']}")
print(f"Индексы решений, где не было маркера начала (гражданские): {stats['index_solution_not_start_civile']}")
print(f"Индексы решений, где не было маркера начала (банкротные): {stats['index_solution_not_start_bankruptcy']}")
print(f"Индексы решений, где не было маркера начала (административные): {stats['index_solution_not_start_administrative']}")
print(f"Индексы решений, где не было маркера конца (без категории): {stats['index_solution_not_end_common']}")
print(f"Индексы решений, где не было маркера конца (гражданские): {stats['index_solution_not_start_civile']}")
print(f"Индексы решений, где не было маркера конца (банкротные): {stats['index_solution_not_end_bankruptcy']}")
print(f"Индексы решений, где не было маркера конца (административные): {stats['index_solution_not_end_administrative']}")

print("Результаты записаны в: civile.jsonl, bankruptcy.jsonl, administrative.jsonl, filtered_output.jsonl")
