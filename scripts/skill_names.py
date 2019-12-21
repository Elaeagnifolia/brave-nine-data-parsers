import xml.etree.ElementTree as ET
import os

def main():
	skills = ET.parse('SkillBasicListText_ENG.txt')

	file = open("skill-names.txt", "w", encoding="utf-8")
	tooltip = ET.parse('SkillTooltipDataBasicList.txt')
	root = skills.getroot()
	for child in root:
		# We only want to get the codes ending in "71" and with
		# length greater than 5 since those are the skill names
	    if child.find('_code').text[-2:] == "71" and len(child.find('_code').text) > 5:
	        file.write(child.find('_text').text)
	        file.write('\n')
	file.close()

if __name__ == "__main__":
	main()