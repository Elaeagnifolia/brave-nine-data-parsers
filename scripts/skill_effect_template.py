import xml.etree.ElementTree as ET
import os

skills = ET.parse('SkillBasicListText_ENG.txt')

def findCode(code):
        root = skills.getroot()
        for child in root:
                if child.find('_code').text == code:
                        text = removeExtraText(child.find('_text').text)
                        return text

def removeExtraText(text):
        text = text.replace('[ABCCEA]', '')
        text = text.replace('[FEF8D5]', '')
        text = text.replace('[F8AC61]', '')
        text = text.replace('[-]', '')
        text = text.replace('\\n', '<br/>')
        return text

file = open("effects.txt", "w", encoding="utf-8")
tooltip = ET.parse('SkillTooltipDataBasicList.txt')
root = tooltip.getroot()
for child in root:
        if findCode(child.find('_code').text) is not None and findCode(child.find('_nameCode').text) is not None:
                file.write('{{EffectDetails')
                file.write('|name=' + findCode(child.find('_nameCode').text))
                file.write('|id=' + child.find('_code').text)
                file.write('|type=' + findCode(child.find('_skillTypeTextCode').text))
                file.write('|target=' + findCode(child.find('_targetTextCode').text))
                file.write('|applyTime=' + findCode(child.find('_applyTimeTextCode').text))
                file.write('|turn=' + findCode(child.find('_turnTextCode').text))
                file.write('|description=' + findCode(child.find('_code').text))
                if findCode(child.find('_exceptionTextCode').text) is not None:
                        file.write('|exception=' + findCode(child.find('_exceptionTextCode').text))
                else:
                        file.write('|exception=')
                file.write('}}\n')
file.close()
