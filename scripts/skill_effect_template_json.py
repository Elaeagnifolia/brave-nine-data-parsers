import json
import os

skills = ""

with open('SkillBasicListText_ENG.txt', "r", encoding="utf-8") as skills_json_file:
    skills = json.load(skills_json_file)

def find_code(code):
    for node in skills['LocalTextBasicList']['_itemList']:
        if node['_code'] == code:
            text = remove_extra_text(node['_text'])
            return text

def remove_extra_text(text):
        text = text.replace('[ABCCEA]', '')
        text = text.replace('[FEF8D5]', '')
        text = text.replace('[F8AC61]', '')
        text = text.replace('[-]', '')
        text = text.replace('\\n', '<br/>')
        text = text.replace('\n', ' ')
        return text

def get_parsed_template_wikicode(node):
    line = ""
    if find_code(node['_code']) is not None and find_code(node['_nameCode']) is not None:
        line = line + '{{EffectDetails'
        line = line + '|name=' + find_code(node['_nameCode'])
        line = line + '|id=' + str(node['_code'])
        line = line + '|type=' + find_code(node['_skillTypeTextCode'])
        line = line + '|target=' + find_code(node['_targetTextCode'])
        line = line + '|applyTime=' + find_code(node['_applyTimeTextCode'])
        line = line + '|turn=' + find_code(node['_turnTextCode'])
        line = line + '|description=' + find_code(node['_code'])
        if find_code(node['_exceptionTextCode']) is not None:
                line = line + '|exception=' + find_code(node['_exceptionTextCode'])
        else:
                line = line + '|exception='
        line = line + '}}\n'
    return line

def main():
    file = open("effects-parsed.txt", "w", encoding="utf-8")
    lines = []
    with open('SkillTooltipDataBasicList.txt', "r", encoding="utf-8") as skill_tooltip_json_file:
        tooltip = json.load(skill_tooltip_json_file)
        for node in tooltip['SkillTooltipDataBasicList']['_itemList']:
            lines.append(get_parsed_template_wikicode(node))
    lines.sort()
    for line in lines:
        file.write(line)
    file.close()

if __name__ == "__main__":
    main()