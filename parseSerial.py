import serial
import xml.etree.ElementTree as ET
from lxml import etree

recParser = etree.XMLParser(recover=True)	#the parser will try to recover if err

vesper = 'ivolt'

#setup serial
s = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 9600,
)

while True:
	line = s.readline().decode('utf-8', 'replace')
	while line[0:7] != '<li850>':			#handles inadequate parse XML
		line = s.readline().decode('utf-8', 'replace')
	root = ET.fromstring(line, parser=recParser)	#parses the feed
	for child in root:				#for each child of the root of the parse,
		for child in child:
			if child.tag == "co2":			#vesper is a var named on ln ~8
				target = float(child.text)
				print('\nA ', target, '\n')
			if child.tag == "cellpres":
				target = float(child.text)
				print('\nB ', target, '\n')
			print(child.tag, child.text)	#print child's tag/attribute/value
	#print(root)
	#print(root.tag)
