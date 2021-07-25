import cantools
from datetime import date
import os

dbc_path = 'PATH_TO_DBC'
dbc_name_split = dbc_path.split("/")
bus_name = dbc_name_split[len(dbc_name_split)-1].replace('.dbc','')

db = cantools.database.load_file(dbc_path)

nodes = set()

for node in db.nodes:
	nodes.add(node.name)

database = {}

for node in nodes:
	#print(node)
	for message in db.messages:
		#print(message.senders)
		if node in message.senders:
			if not node in database.keys():
				cycle_time_signals = [message.cycle_time]
				for signal in message.signals:
					cycle_time_signals.append(signal.name)
				database[node] = {message.name: cycle_time_signals}
			else:
				cycle_time_signals = [message.cycle_time]
				for signal in message.signals:
					cycle_time_signals.append(signal.name)					
				database[node].update({message.name: cycle_time_signals})


# for node in database.keys():
# 	print("\n===========================================\nNode:", node)
# 	for message in database[node].keys():
# 		print("\n---------------------------------------\nMessage: ",message,", cycle_time: ", database[node][message][0])
# 		for signal in range(1, len(database[node][message])):
# 			print("\nSignal: ", database[node][message][signal])

try:
	os.mkdir(os.path.abspath(os.getcwd()) + "\\Nodes\\" + bus_name + "\\")
except Exception as ex:
	print(ex)

simulationControlFile = open(os.path.abspath(os.getcwd()) + "\\Nodes\\" + bus_name + "\\SimulationControl.can", "w")

simulationControlFile.write("/*@!Python generator script version: v1.0\n@Script author: vrinceanu.ioan.vladut@gmail.com*/\n// CAN\n/*\n" + 
	"-------------------------------------------------------------------------------\n" +
	"Name:        SimulationControl node for " + bus_name + " bus\nDescription: Node used for simulation control\n\n" +
	"Generation date: " + str(date.today().strftime("%d/%m/%Y")) + "\n" +
	"@Generation author: " + os.getlogin() + "\n-------------------------------------------------------------------------------\n*/" +
	"\n\nincludes\n{\n\n}\n\nvariables\n{\n\n}\n\non start\n{\n\n}\n")

simulationControlFile.write("\n/*-----SimulationControl " + bus_name + "-----*/\non sysvar SimulationControl::" + bus_name + "::sv_" + bus_name + "_ON_OFF\n{")

for node in database.keys():

	simulationControlFile.write("\n\t@NodeControl::" + bus_name + "::sv_" + node + "_ON_OFF = @this;")

	canFile = open(os.path.abspath(os.getcwd()) + "\\Nodes\\" + bus_name + "\\" + node +".can", "w")

	canFile.write("/*@!Python generator script version: v1.0\n@Script author: vrinceanu.ioan.vladut@gmail.com*/\n// CAN\n/*\n" + 
		"-------------------------------------------------------------------------------\n" +
		"Name:        " + node + " node\nDescription: Node used for simulating " + node + " node\n\n" +
		"Generation date: " + str(date.today().strftime("%d/%m/%Y")) + "\n" +
		"@Generation author: " + os.getlogin() + "\n-------------------------------------------------------------------------------\n*/" +
		"\n\nincludes\n{\n\n}\n\nvariables\n{")




	for message in database[node].keys():
		canFile.write("\n\t/*-----" + message + "-----*/\n\tmessage " + message + " m_" + message + ";\n\tmstimer t_" + message + ";")
	canFile.write("\n}\n\non start\n{")

	for message in database[node].keys():
		canFile.write("\n\n\t/*-----" + message + "-----*/")
		for signal in range(1, len(database[node][message])):
			canFile.write("\n\tRegisterSignalDriver(" + bus_name + "::" + message + "::" + database[node][message][signal] +
			", \"SetSignal_" + message + "_" + database[node][message][signal] + "\");\n")

	canFile.write("}\n\n/*-----" + node + " Control-----*/\non sysvar NodeControl::" + bus_name + "::sv_" + node + "_ON_OFF\n{" +
		"\n\tif(1 == @this)\n\t\t{\n\t\t\tcanOnline(3);")
	for message in database[node].keys():
		canFile.write("\n\t\t\t@MessageControl::" + bus_name + "::" + message + "::" + "sv_" + message + " = 1;")
	canFile.write("\n\t\t}\n\telse\n\t\t{")

	for message in database[node].keys():
		canFile.write("\n\t\t\t@MessageControl::" + bus_name + "::" + message + "::" + "sv_" + message + " = 0;")

	canFile.write("\n\t\t\tcanOffline(3);\n\t\t}\n}")

	for message in database[node].keys():
		canFile.write("\n\n/*-----" + message + " Controls-----*/\non timer t_" + message + "\n{\n\tcancelTimer(this);\n\t" + 
			message + "_Generate_Output();\n\tif(@MessageControl::" + bus_name + "::" + message + "::sv_" + message + "_CycleTime > 0) " +
			"setTimer(this, @MessageControl::" + bus_name + "::" + message + "::sv_" + message + "_CycleTime);\n}\n")

		canFile.write("\non sysvar MessageControl::" + bus_name + "::" + message + "::" + "sv_" + message + "\n{\n\t" +
			"if(1 == @this)\n\t{\n\t\tif(@MessageControl::" + bus_name + "::" + message + "::sv_" + message + "_CycleTime > 0) " +
			"setTimer(t_" + message + ", random(50));\n\t}\n\telse cancelTimer(t_" + message + ");\n}\n")

		canFile.write("\non sysvar MessageControl::" + bus_name + "::" + message + "::sv_" + message + "_CycleTime\n{\n\tif(@this <= 0) " +
			"cancelTimer(t_" + message + ");\n}\n")

		canFile.write("\non sysvar MessageControl::" + bus_name + "::" + message + "::sv_" + message + "_SendEvent\n{\n\tif( 1 == " +
			"@MessageControl::" + bus_name + "::" + message + "::sv_" + message + ") " + message + "_Generate_Output();\n}\n")

		canFile.write("\nvoid " + message + "_Generate_Output()\n{\n\toutput(m_" + message + ");\n}\n")


	for message in database[node].keys():
		canFile.write("\n\n/*-----SetSignal Callbacks for " + message + "-----*/\n")
		for signal in range(1, len(database[node][message])):
				canFile.write("\nvoid SetSignal_" + message + "_" + database[node][message][signal] + "(double Value)\n{\n\t" +
				"m_" + message + "." + database[node][message][signal] + ".phys = Value;\n}")

simulationControlFile.write("\n}")