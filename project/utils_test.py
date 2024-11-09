import unittest

from project.utils import extract_joint_stock, clean_name_sides

cases = {
    'open_stock_company_«': 'Как следует из материалов дела, открытое акционерное общество «Российские железные дороги» в качестве перевозчика осуществляло доставку вагона по вышеуказанным транспортным железнодорожным накладным.',
    'open_stock_company_«_ya': '11.11.1993 специализированное государственное территориально-производственное предприятие было преобразовано путем приватизации в акционерное общество открытого типа «Владимироблгаз», которое в 2001 году переименовано в открытое акционерное общество «Владимироблгаз». 30.09.2013 общество переименовано в открытое акционерное общество «Газпром газораспределение Владимир», 20.07.2015 – в акционерное общество «Газпром газораспределение Владимир».',
    'open_stock_company_""': 'Как следует из материалов дела, открытое акционерное общество ""Российские железные дороги"" в качестве перевозчика осуществляло доставку вагона по вышеуказанным транспортным железнодорожным накладным.',
    'open_stock_company_""_ya': 'В соответствии с подпунктом ""а"" пункта 1 Распоряжения № 3203-р публичное акционерное общество ""Ростелеком"" определено единственным исполнителем закупок работ (услуг) по подключению цифрового',
    'short_public_stock_company_«': 'Исковые требования ПАО СК «Росгосстрах» основаны на положениях подпункта «к» пункта 1 статьи 14 Закона об ОСАГО,',
    'short_open_stock_company_«': 'перед кредиторами ООО МФК «Мани Мен», ОАО «Альфа Банк», АО «Тинькофф Банк», ОАО «АльфаСтрахование», МИФНС России № 6',
    'empty_name_sides': 'Здесь нет наименований сторон процесса'
}

truth_name_sides = {
    'open_stock_company_«': 'Как следует из материалов дела, открытое акционерное общество в качестве перевозчика осуществляло доставку вагона по вышеуказанным транспортным железнодорожным накладным.',
    'open_stock_company_""_ya': 'В соответствии с подпунктом ""а"" пункта 1 Распоряжения № 3203-р публичное акционерное общество определено единственным исполнителем закупок работ (услуг) по подключению цифрового',
    'open_stock_company_«_ya': '11.11.1993 специализированное государственное территориально-производственное предприятие было преобразовано путем приватизации в акционерное общество открытого типа, которое в 2001 году переименовано в открытое акционерное общество. 30.09.2013 общество переименовано в открытое акционерное общество, 20.07.2015 – в акционерное общество.',
    'short_public_stock_company_«': 'Исковые требования ПАО СК основаны на положениях подпункта «к» пункта 1 статьи 14 Закона об ОСАГО,',
    'short_open_stock_company_«': 'перед кредиторами ООО МФК «Мани Мен», ОАО, АО, ОАО, МИФНС России № 6',
}


class TestUtils(unittest.TestCase):
    def test_extract_joint_stock(self):
        res = extract_joint_stock(cases['open_stock_company_«'])
        self.assertEqual(['открытое акционерное общество «Российские железные дороги»'], res)

        res = extract_joint_stock(cases['open_stock_company_""'])
        self.assertEqual(['открытое акционерное общество ""Российские железные дороги""'], res)

    def test_clean_name_sides(self):
        res = clean_name_sides(cases['open_stock_company_«'])
        self.assertEqual(truth_name_sides['open_stock_company_«'], res)

        res = clean_name_sides(cases['open_stock_company_""_ya'])
        self.assertEqual(truth_name_sides['open_stock_company_""_ya'], res)

        res = clean_name_sides(cases['open_stock_company_«_ya'])
        self.assertEqual(truth_name_sides['open_stock_company_«_ya'], res)

        res = clean_name_sides(cases['short_public_stock_company_«'])
        self.assertEqual(truth_name_sides['short_public_stock_company_«'], res)

        res = clean_name_sides(cases['short_open_stock_company_«'])
        self.assertEqual(truth_name_sides['short_open_stock_company_«'], res)

        res = clean_name_sides(cases['empty_name_sides'])
        self.assertEqual(cases['empty_name_sides'], res)

if __name__ == '__main__':
    unittest.main()
