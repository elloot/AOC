import re

RULES = {}


def __main__():

    file_content = open('input.txt', 'r').read()

    rule_line_pattern = re.compile('^[0-9]+:.+$', re.MULTILINE)

    for line in rule_line_pattern.findall(file_content):
        rule_key_pattern = re.compile('^[0-9]+', re.MULTILINE)
        rule_pattern = re.compile('(?<=[0-9]:\\s).+$', re.MULTILINE)
        rule_key = rule_key_pattern.findall(line)[0]
        RULES[rule_key] = rule_pattern.findall(line)[0].replace('"', '').split(' | ')

    messages_pattern = re.compile('^[ab]+$', re.MULTILINE)
    messages = messages_pattern.findall(file_content)

    validation_pattern = re.compile(pattern_builder('0') + '$', re.MULTILINE)
    valid_messages = []

    for message in messages:
        if re.match(validation_pattern, message):
            valid_messages.append(message)

    print(len(valid_messages))


def pattern_builder(rule_key):
    rule_string = '('

    if len(RULES[rule_key]) == 1:
        rule_group = RULES[rule_key][0]
        if len(rule_group.split()) == 1:
            if RULES[rule_key][0].isdigit():
                rule_string += pattern_builder(RULES[rule_key][0])
            else:
                rule_string += RULES[rule_key][0]
        else:
            for rule in rule_group.split():
                rule_string += '(' + pattern_builder(rule) + ')'
    else:
        for index, rule_group in enumerate(RULES[rule_key]):
            for rule in rule_group.split():
                rule_string += '(' + pattern_builder(rule) + ')'
            if index < len(RULES[rule_key]) - 1:
                rule_string += '|'

    rule_string += ')'

    return rule_string


if __name__ == '__main__':
    __main__()
