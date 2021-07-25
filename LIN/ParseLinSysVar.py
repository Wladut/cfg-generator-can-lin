import ldfparser
from datetime import date
import os

ldf_path = 'PATH_TO_LDF'
ldf_name_split = ldf_path.split("/")
bus_name = ldf_name_split[len(ldf_name_split)-1].replace('.ldf','')

db = ldfparser.parseLDF(ldf_path)

nodes = set()

nodes.add(db.master.name)

for node in db.slaves:
	nodes.add(node.name)

database = {}

for node in nodes:
	for frame in db.frames:
		if node == frame.publisher.name:
			if not node in database.keys():
				cycle_time_signals = [0]
				for signal in frame.signals:
					cycle_time_signals.append(signal.name)
				database[node] = {frame.name: cycle_time_signals}
			else:
				cycle_time_signals = [0]
				for signal in frame.signals:
					cycle_time_signals.append(signal.name)
				database[node].update({frame.name: cycle_time_signals})


# for node in database.keys():
# 	print("\n===========================================\nNode:", node)
# 	for message in database[node].keys():
# 		print("\n---------------------------------------\nMessage: ",message,", cycle_time: ", database[node][message][0])
# 		for signal in range(1, len(database[node][message])):
# 			print("\nSignal: ", database[node][message][signal])

try:
	os.mkdir(os.path.abspath(os.getcwd()) + "\\Sysvars\\" + bus_name + "\\")
except Exception as ex:
	print(ex)

indent = "  "

canFile = open(os.path.abspath(os.getcwd()) + "\\Sysvars\\" + bus_name + "\\" + bus_name +".vsysvar", "w")

canFile.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "\n<systemvariables version=\"4\">\n" + indent + 
	  "<namespace name=\"\" comment=\"\" interface=\"\">" + "\n" + indent*2 + "<namespace name=\"MessageControl\" comment=\"\" interface=\"\">" + 
	  "\n" + indent*3 + "<namespace name=\"" + bus_name + "\" comment=\"\" interface=\"\">")

messagesSet = set()


for node in database.keys():
	for message in database[node].keys():
		flag_duplicate = False
		cycle_time = str(database[node][message][0])
		if message not in messagesSet:
			messagesSet.add(message)
		else:
			flag_duplicate = True
		if not flag_duplicate:
			canFile.write("\n" + indent*4 + "<namespace name=\"" + message + "\" comment=\"\" interface=\"\">\n" + indent*5 +
			"<variable anlyzLocal=\"2\" readOnly=\"false\" valueSequence=\"false\" unit=\"\" name=\"" + "sv_" + message + 
			"\" comment=\"\" bitcount=\"32\" isSigned=\"true\" encoding=\"65001\" type=\"int\" startValue=\"0\" />\n")
			canFile.write("\n" + indent*4 + "</namespace>")

canFile.write("\n" + indent*3 + "</namespace>\n" + indent*2 + "</namespace>\n" + indent*2 + "<namespace name=\"NodeControl\" comment=\"\" interface=\"\">" + 
		"\n" + indent*3 + "<namespace name=\"" + bus_name + "\" comment=\"\" interface=\"\">")

for node in database.keys():
	canFile.write("\n" + indent*4 + "<variable anlyzLocal=\"2\" readOnly=\"false\" valueSequence=\"false\" unit=\"\" name=\"" + "sv_" + node + "_ON_OFF" +
		"\" comment=\"\" bitcount=\"32\" isSigned=\"true\" encoding=\"65001\" type=\"int\" startValue=\"0\" />")


canFile.write("\n" + indent*3 + "</namespace>\n" + indent*2 + "</namespace>\n" + indent*2 + "<namespace name=\"SimulationControl\" comment=\"\" interface=\"\">" + 
		"\n" + indent*3 + "<namespace name=\"" + bus_name + "\" comment=\"\" interface=\"\">")
canFile.write("\n" + indent*4)
canFile.write("<variable anlyzLocal=\"2\" readOnly=\"false\" valueSequence=\"false\" unit=\"\" name=\"sv_" + bus_name + "_ON_OFF\" comment=\"\" bitcount=\"32\" isSigned=\"true\" encoding=\"65001\" type=\"int\" startValue=\"0\" />")


canFile.write("\n" + indent*3 + "</namespace>\n" + indent*2 + "</namespace>\n" + indent + "</namespace>\n" + "</systemvariables>")
	 