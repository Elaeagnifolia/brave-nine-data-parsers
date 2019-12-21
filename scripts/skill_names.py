import xml.etree.ElementTree as ET
import os

skills = ET.parse('SkillBasicListText_ENG.txt')

def findCode(code):
        root = skills.getroot()
        for child in root:
                if child.find('_code').text == code:
                        text = removeExtraText(child.find('_text').text)
                        return text

file = open("skill-names.txt", "w", encoding="utf-8")
tooltip = ET.parse('SkillTooltipDataBasicList.txt')
root = skills.getroot()
for child in root:
    if child.find('_code').text[-2:] == "71" and len(child.find('_code').text) > 5:
        file.write(child.find('_text').text)
        file.write('\n')
file.close()
