import re

RULES = {}
EIGHT_RECURSION_DEPTH = 0
ELEVEN_RECURSION_DEPTH = 0
MAX_RECURSION_DEPTH = 6


def __main__():
    file_content = open('input.txt', 'r').read()

    file_content = file_content.replace('8: 42', '8: 42 | 42 8')
    file_content = file_content.replace('11: 42 31', '11: 42 31 | 42 11 31')

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
    global ELEVEN_RECURSION_DEPTH, EIGHT_RECURSION_DEPTH
    rule_string = '('

    if rule_key == '8':
        EIGHT_RECURSION_DEPTH += 1
    if rule_key == '11':
        ELEVEN_RECURSION_DEPTH += 1

    if not ((rule_key == '8' and EIGHT_RECURSION_DEPTH >= MAX_RECURSION_DEPTH) or
            rule_key == '11' and ELEVEN_RECURSION_DEPTH >= MAX_RECURSION_DEPTH):
        if len(RULES[rule_key]) == 1:
            rule_value = RULES[rule_key][0]
            if len(rule_value.split()) == 1:
                if rule_value.isdigit():
                    rule_string += pattern_builder(rule_value)
                else:
                    rule_string += rule_value
            else:
                for rule in rule_value.split():
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
