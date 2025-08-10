from pregex.core import *
from pregex.core.operators import Either
from pregex.core.tokens import Space

any_cyrillic = Pregex('[а-яА-ЯёЁ]', False)
name_codex = ('([Нн]алогов|[Гг]ражданск|[Зз]емельн|[Тт]рудов|[Сс]емейн|[Жж]илищн|[Бб]юджетн|[Уу]головн|[Лл]есн|'
              '[Вв]оздушн|[Вв]одн|[Гг]радостроительн)[а-яА-ЯёЁ]{1,3}')

name_civile_process_codex = '([Гг]ражданск[а-яА-ЯёЁ]{1,3}\s+[Пп]роцессуальн[а-яА-ЯёЁ]{1,3}\s+[Кк]одекс)'
name_civile_process_codex_pre = Pregex(name_civile_process_codex, False)

name_arbitrage_process_codex = '([Аа]рбитражн[а-яА-ЯёЁ]{1,3}\s+[Пп]роцессуальн[а-яА-ЯёЁ]{1,3}\s+[Кк]одекс)'
name_arbitrage_process_codex_pre = Pregex(name_arbitrage_process_codex, False)

name_administrative_codex = '([Кк]одекс\s+об\s+[Аа]административн[а-яА-ЯёЁ]{1,3}\s+[Пп]равонарушен[а-яА-ЯёЁ]{1,3})'
name_administrative_codex_pre = Pregex(name_administrative_codex, False)

code_pre = Pregex("[Кк]одекс", False)
name_codex_pre = Pregex(name_codex, False)
codex = (Either(name_codex_pre.concat(Space().at_least(1)).concat(code_pre.concat(any_cyrillic.at_most(3))),
                name_civile_process_codex_pre,
                name_arbitrage_process_codex_pre))
c = codex.get_matches("Гражданского процессуального Кодекса")
c = codex.get_matches("арбитражного процессуального Кодекса")
print(codex.get_pattern())
