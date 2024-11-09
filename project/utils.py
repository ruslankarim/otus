import logging
import re

mark_description = r' *у *с *т *а *н *о *в\w*\W*'
mark_justification = r'как следует из материалов дела' \
                     r'|изучив материалы дела' \
                     r'|исследовав материалы дела' \
                     r'|исследовав представленные в дело материалы' \
                     r'|ознакомившись с представленными по делу документами' \
                     r'|проанализировав имеющиеся в материалах дела' \
                     r'|рассмотрев материалы дела' \
                     r'|проанализировав доводы' \
                     r'|проанализировав представленные в материалы дела документы' \
                     r'|заслушав объяснения представителей сторон' \
                     r'|из представленных в материалы дела документов' \
                     r'|ознакомившись с представленными в материалы дела документами' \
                     r'|изучив представленные в материалы дела' \
                     r'|исследовав представленные в материалы дела' \
                     r'|на основании исследования представленных в дело' \
                     r'|исследовав представленные в материалы дела' \
                     r'|исследовав представленные по делу доказательства' \
                     r'|изучив имеющиеся материалы дела' \
                     r'|изучив представленные материалы дела' \
                     r'|оценив представленные доказательства' \
                     r'|суд, исследовав и оценив обстоятельства' \
                     r'|заслушав\w*|\W*изучив' \
                     r'|исследовав представленные в матералы дела доказательства' \
                     r'|исследовав\w*|\W*доказательства'
mark_resolution = r'руководствуясь\w*|\W*р *е *ш *и *л'

#todo сделать алиасы для ключей:
mark_joint_stock = {
    'open': r'(открыт[ого|ому|ое|ым|ом]+ +акционерн[ое|ый|ого|ому|ый|ым|ом]+ +обществ[о|а|у|е] +[\w+ +]*«\w+[ +\w+]*»)',
    'open_quotes': '(открыт[ого|ому|ое|ым|ом]+ +акционерн[ое|ый|ого|ому|ый|ым|ом]+ +обществ[о|а|у|е] +[\w+ +]*\"+\w+[ +\w+]*\"+)',

    'public': r'(публичн[ого|ому|ое|ым|ом]+ +акционерн[ое|ый|ого|ому|ый|ым|ом]+ +обществ[о|а|у|е] +[\w+ +]*«\w+[ +\w+]*»)',
    'public_quotes': '(публичн[ого|ому|ое|ым|ом]+ +акционерн[ое|ый|ого|ому|ый|ым|ом]+ +обществ[о|а|у|е] +[\w+ +]*\"+\w+[ +\w+]*\"+)',

    'closed': r'(акционерн[ое|ый|ого|ому|ый|ым|ом]+ +обществ[о|а|у|е] +[\w+ +]*«\w+[ +\w+]*»)',

    'short_open': r'(оао +[\w+ +]*«\w+[ +\w+]*»)',
    'short_open_quotes': r'(оао +[\w+ +]*«\w+[ +\w+]*»)',

    'short_public': r'(пао +[\w+ +]*«\w+[ +\w+]*»)',
    'short_public_quotes': r'(пао +[\w+ +]*\"+\w+[ +\w+]*\"+)',

    'short_closed': r'(ао +[\w+ +]*«\w+[ +\w+]*»)',
}

sep_joint_stock = {
    'open': r'обществ[о|а|у|е] +',
    'open_quotes': r'обществ[о|а|у|е] +',
    'public': r'обществ[о|а|у|е] +',
    'public_quotes': r'обществ[о|а|у|е] +',
    'closed': r'обществ[о|а|у|е] +',
    'short_open': r'о +',
    'short_open_quotes': r'о +',
    'short_public': r'о +',
    'short_public_quotes': r'о +',
    'short_closed': r'о +',
}


def update_description(parts):
    parts.update({mark_description: True})
    return True


def update_justification(parts):
    parts.update({mark_justification: True, mark_description: False})
    return True


def update_resolution(parts):
    parts.update({mark_resolution: True, mark_justification: False})
    return True


def split_case(case):
    intro = []
    description = []
    justification = []
    resolution = []
    focus = {}

    regexps = [
        lambda l: update_resolution(focus) if re.search(mark_resolution, ' '.join([' '.join(justification[-3:0]), l]),
                                                        re.IGNORECASE) else False,
        lambda l: update_justification(focus) if re.search(mark_justification, l, re.IGNORECASE) else False,
        lambda l: update_description(focus) if re.search(mark_description, ' '.join([' '.join(intro[-7:0]), l]),
                                                         re.IGNORECASE) else False,
    ]

    for line in case.split('\n'):
        if len(regexps) > 0 and regexps[len(regexps) - 1](line):
            regexps.pop()

        if focus.get(mark_description, False):
            description.append(line)
        elif focus.get(mark_justification, False):
            justification.append(line)
        elif focus.get(mark_resolution, False):
            resolution.append(line)
        else:
            intro.append(line)

    return {
        'intro': intro,
        'description': description,
        'justification': justification,
        'resolution': resolution
    }


def extract_joint_stock(text):
    result = []
    for k in mark_joint_stock:
        found = False
        groups = re.findall(mark_joint_stock[k], text, re.IGNORECASE)
        for group in groups:
            result.append(group)
            found = True
        if found:
            return result
    return result


def clean_name_sides(text):
    for k in mark_joint_stock:
        groups = re.findall(mark_joint_stock[k], text, re.IGNORECASE)
        # определить то что будем удалчть здесь а не сепаратором
        for group in groups:
            parts = re.split(sep_joint_stock[k], group, flags=re.IGNORECASE)
            if len(parts) > 1:
                pattern = f' {parts[1]}'
                print(f'подстрока: {re.findall(parts[1], text, re.IGNORECASE)}, будет удалена')
                text = re.sub(pattern, '', text)

    return text
