import unittest
from unittest import TestCase


class Test(TestCase):
    def test_remove_named_entities(self):
        from ner import remove_named_entities  # ← замени на имя файла, если нужно

        text = "В 2022 году судья Иванов А.А. рассматривал дело против ООО Ромашка в Москве."
        result = remove_named_entities(text)

        # Проверяем, что сущности удалены
        self.assertNotIn("Иванов", result)
        self.assertNotIn("ООО", result)
        self.assertNotIn("Москва", result)
        self.assertNotIn("2022", result)

        # Проверяем, что остался контекст
        self.assertIn("дело", result)
        self.assertIn("рассматривал", result)


if __name__ == '__main__':
    unittest.main()
