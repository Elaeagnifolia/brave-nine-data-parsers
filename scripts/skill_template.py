import xml.etree.ElementTree as ET
import os

skills = ET.parse('SkillBasicListText_ENG.txt')

def findCode(code):
        root = skills.getroot()
        for child in root:
                if child.find('_code').text == code:
                        text = child.find('_text').text
                        return text
        return ''

def getEffect(code):
        return ''

def writeEffects(prefix):
        prevme1 = ''
        prevme2 = ''
        prevme3 = ''
        awakenPrefix = int(prefix) + 1;
        
        i = 0;
        prenum = '0';
        for i in range(0, 16):
                if i == 10:
                        prenum = ''
                if findCode(prefix + prenum + str(i) + '01') != '':
                        prevme1 = prefix + prenum + str(i) + '01'
                if findCode(prefix + prenum + str(i) + '03') != '':
                        prevme2 = prefix + prenum + str(i) + '03'
                if findCode(prefix + prenum + str(i) + '05') != '':
                        prevme3 = prefix + prenum + str(i) + '05'
                file.write("\n{{Skill level|attackRange=|me1=" + prevme1)
                if prevme2 != '':
                        file.write("|me2=" + prevme2)
                if prevme3 != '':
                        file.write("|me3=" + prevme3)
                if findCode(str(awakenPrefix) + "0007") != '':
                        file.write("|awakened=" + str(awakenPrefix) + "0007")
                file.write("}}")
        return ''

file = open("skill-template.txt", "w", encoding="utf-8")
tooltip = ET.parse('SkillTooltipDataBasicList.txt')
root = skills.getroot()
for child in root:
    if child.find('_code').text[-2:] == "71" and len(child.find('_code').text) > 5:
        prefix = child.find('_code').text[:-2]
        file.write('{{Skill')
        file.write('\n|name=' + child.find('_text').text)
        file.write('\n|round=')
        file.write('\n|target=')
        file.write('\n|description=' + findCode(prefix + "81"))
        file.write('\n|effects=')
        writeEffects(prefix[:-2])
        file.write('\n}}\n')
file.close()
