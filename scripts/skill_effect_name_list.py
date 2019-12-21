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

file = open("effect-names.txt", "w", encoding="utf-8")
tooltip = ET.parse('SkillTooltipDataBasicList.txt')
root = tooltip.getroot()
for child in root:
        if findCode(child.find('_code').text) is not None and findCode(child.find('_nameCode').text) is not None:
                file.write(findCode(child.find('_nameCode').text))
                file.write('\n')
file.close()
