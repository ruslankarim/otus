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
    parts = {}

    regexps = [
        lambda l: update_resolution(parts) if re.search(mark_resolution, ' '.join([' '.join(justification[-3:0]), l]),
                                                        re.IGNORECASE) else False,
        lambda l: update_justification(parts) if re.search(mark_justification, l, re.IGNORECASE) else False,
        lambda l: update_description(parts) if re.search(mark_description, ' '.join([' '.join(intro[-7:0]), l]),
                                                         re.IGNORECASE) else False,
    ]

    for line in case.split('\n'):
        if len(regexps) > 0 and regexps[len(regexps) - 1](line):
            regexps.pop()

        if parts.get(mark_description, False):
            description.append(line)
        elif parts.get(mark_justification, False):
            justification.append(line)
        elif parts.get(mark_resolution, False):
            resolution.append(line)
        else:
            intro.append(line)

    return {
        'intro': intro,
        'description': description,
        'justification': justification,
        'resolution': resolution
    }
