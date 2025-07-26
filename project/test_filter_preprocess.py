import re
from unittest import TestCase

from tools.regexp import spaced_word_regex


class Test(TestCase):
    def test_spaced_word_regex(self):
        pattern = spaced_word_regex("установил")

        # Список входных строк, в которых должно быть совпадение
        should_match = [
            "Рассмотрев материалы дела и дополнительно представленные документы, суд установил.",
            "установил:",
            "установил.",
            "установил",
            "у с т а н о в и л",
            "у с т а н о в и л:",
            "у с т а н о в и л.",
            "У С Т А Н О В И Л",
            "у с Т А н О в И л",
            "суд установил решение",
            "установил:",
            "установил.",
            "он    у   с  т а  н о в и л   факт",
            "рассмотрев, суд у с т а н о в и л следующее"
        ]

        # Строки, где совпадения быть не должно
        should_not_match = [
            "переустановил",  # лишние буквы
            "установ",  # неполное
            "не установлен",  # другое слово
            "уста н о в и л",  # разрыв слова
            "установи",  # укороченное
        ]

        for text in should_match:
            assert re.search(pattern, text), f"Не найдено совпадение в: {text}"

        for text in should_not_match:
            assert not re.search(pattern, text), f"Ложно найдено совпадение в: {text}"

        print("Все тесты прошли успешно.")