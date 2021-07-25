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

indent = "  "

try:
	os.mkdir(os.path.abspath(os.getcwd() + "\\Panels\\" + bus_name + "\\"))
except Exception as ex:
	print(ex)

#bus_MainPanel.xvp -> panel with contains all messages with signals panels


allFrames_panel = open(os.getcwd() + "\\Panels\\" + bus_name + "\\" + bus_name + "_MainPanel" +".xvp", "w")

allFrames_panel.write("<?xml version=\"1.0\"?>\n" + "<Panel Type=\"Vector.CANalyzer.Panels.PanelSerializer, Vector.CANalyzer.Panels.Serializer," + 
	" Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\">\n")

allFrames_panel.write(indent + "<Object Type=\"Vector.CANalyzer.Panels.Runtime.Panel, Vector.CANalyzer.Panels.Common, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"Panel\" Children=\"Controls\" ControlName=\"" + bus_name + "_NodeControl " + "\">")

allFrames_panel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl1\" Children=\"Controls\" ControlName=\"StaticText_PanelName\">")

allFrames_panel.write("\n" + indent*3 + "<Property Name=\"Name\">StaticTextControl1</Property>")
allFrames_panel.write("\n" + indent*3 + "<Property Name=\"Size\">350, 24</Property>")
allFrames_panel.write("\n" + indent*3 + "<Property Name=\"Location\">5, 5</Property>")
allFrames_panel.write("\n" + indent*3 + "<Property Name=\"Font\">Microsoft Sans Serif, 14.25pt, style=Bold</Property>")
allFrames_panel.write("\n" + indent*3 + "<Property Name=\"Text\">" + bus_name + "_MainPanel " + "</Property>")
allFrames_panel.write("\n" + indent*2 + "</Object>")

allFrames_panel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.GroupBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"GroupBoxControl1\" Children=\"Controls\" ControlName=\"Group Box\">")

allFrames_panel_index = 1
allFrames_panel_lenght = 112
allFrames_panel_height = 23
allFrames_panel_location_x = 5
allFrames_panel_location_y = 15
allFrames_panel_columns = 1
allFrames_panel_columns_flag = False

# control all nodes bus_name_NodeControl.xvp

bus_nodeControlPanel = open(os.getcwd() + "\\Panels\\" + bus_name + "\\" + bus_name + "_NodeControl" +".xvp", "w")

bus_nodeControlPanel.write("<?xml version=\"1.0\"?>\n" + "<Panel Type=\"Vector.CANalyzer.Panels.PanelSerializer, Vector.CANalyzer.Panels.Serializer," + 
	" Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\">\n")

bus_nodeControlPanel.write(indent + "<Object Type=\"Vector.CANalyzer.Panels.Runtime.Panel, Vector.CANalyzer.Panels.Common, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"Panel\" Children=\"Controls\" ControlName=\"" + bus_name + "_NodeControl " + "\">")

bus_nodeControlPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl1\" Children=\"Controls\" ControlName=\"StaticText_PanelName\">")

bus_nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Name\">StaticTextControl1</Property>")
bus_nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Size\">350, 24</Property>")
bus_nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Location\">5, 5</Property>")
bus_nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Font\">Microsoft Sans Serif, 14.25pt, style=Bold</Property>")
bus_nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Text\">" + bus_name + "_NodeControl " + "</Property>")
bus_nodeControlPanel.write("\n" + indent*2 + "</Object>")

bus_nodeControlPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.GroupBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"GroupBoxControl1\" Children=\"Controls\" ControlName=\"Group Box\">")

bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.SwitchControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"SwitchControl2\" ControlName=\"Switch/Indicator ChE\">")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Name\">SwitchControl2</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Size\">23, 30</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Location\">5, 15</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"StateCnt\">2</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Activation\">Left</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"SwitchValues\">1;2;0;1</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"SymbolConfiguration\">4;16;SimulationControl::" + bus_name + ";;;sv_" + bus_name + "_ON_OFF;1;;;-1</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"TabIndex\">1</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("</Object>")

bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl2\" Children=\"Controls\" ControlName=\"StaticText_Ch_Enable\">")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Name\">StaticTextControl2</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Size\">120, 13</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Location\">35, 15</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 8.25pt, style=Bold</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"Text\">All " + bus_name + " Nodes</Property>")
bus_nodeControlPanel.write("\n" + indent*4)
bus_nodeControlPanel.write("<Property Name=\"ForeColor\">0, 0, 192</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("</Object>")

bus_nodeControlPanel_index = 1
bus_nodeControlPanel_switchControl_lenght = 23
bus_nodeControlPanel_switchControl_height = 30
bus_nodeControlPanel_switchControl_location_x = 5
bus_nodeControlPanel_switchControl_location_y = 65

bus_nodeControlPanel_staticText_lenght = 128
bus_nodeControlPanel_staticText_height = 23
bus_nodeControlPanel_staticText_location_x = 35
bus_nodeControlPanel_staticText_location_y = 65
bus_nodeControlPanel_columns = 1
bus_nodeControlPanel_columns_flag = False


# iterate nodes
for node in database.keys():
	try:
		os.mkdir(os.path.abspath(os.getcwd() + "\\Panels\\" + bus_name + "\\" + node + "\\"))
	except Exception as ex:
		print(ex)

	#bus_MainPanel.xvp -> panel with contains all messages with signals panels
	if(allFrames_panel_columns_flag):
		allFrames_panel_columns_flag = False
		allFrames_panel_columns += 1

	allFrames_panel.write("\n" + indent*3)
	allFrames_panel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.PanelButtonControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"PanelButtonControl" + str(allFrames_panel_index) + "\" Children=\"Controls\" ControlName=\"" + bus_name + "::" + node + "\">")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"Name\">PanelButtonControl" + str(allFrames_panel_index) + "</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"Size\">" + str(allFrames_panel_lenght) + ", " + str(allFrames_panel_height) + "</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"Location\">" + str(allFrames_panel_location_x) + ", " + str(allFrames_panel_location_y) + "</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"ClosePanels\">False</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"PanelList\">1;1;" + node + "\\" + node + "_SubPanel.xvp</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"NodeList\">1;0</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"NetworkList\">1;0</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"Font\">Microsoft Sans Serif, 8.25pt, style=Bold</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"Text\">" + node + "</Property>")
	allFrames_panel.write("\n" + indent*4)
	allFrames_panel.write("<Property Name=\"TabIndex\">" + str(allFrames_panel_index - 1) + "</Property>")
	allFrames_panel.write("\n" + indent*3)
	allFrames_panel.write("</Object>")

	allFrames_panel_index += 1
	allFrames_panel_location_y += 25

	if(allFrames_panel_location_y%190 == 0):
		allFrames_panel_location_x += 174
		allFrames_panel_columns_flag = True
		allFrames_panel_location_y = 15

	# control all nodes bus_name_NodeControl.xvp
	if(bus_nodeControlPanel_columns_flag):
		bus_nodeControlPanel_columns_flag = False
		bus_nodeControlPanel_columns += 1

	bus_nodeControlPanel.write("\n" + indent*3)
	bus_nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.SwitchControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"SwitchControl" + str(bus_nodeControlPanel_index + 2) + "\" ControlName=\"Switch/Indicator ChE\">")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Name\">SwitchControl" + str(bus_nodeControlPanel_index + 2) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Size\">" + str(bus_nodeControlPanel_switchControl_lenght) + ", " + str(bus_nodeControlPanel_switchControl_height) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Location\">" + str(bus_nodeControlPanel_switchControl_location_x) + ", " + str(bus_nodeControlPanel_switchControl_location_y) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"StateCnt\">2</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Activation\">Left</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"SwitchValues\">1;2;0;1</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"SymbolConfiguration\">4;16;NodeControl::" + bus_name + ";;;sv_" + node + "_ON_OFF;1;;;-1</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"TabIndex\">" + str(bus_nodeControlPanel_index + 1) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*3)
	bus_nodeControlPanel.write("</Object>")

	bus_nodeControlPanel.write("\n" + indent*3)
	bus_nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.PanelButtonControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"PanelButtonControl" + str(bus_nodeControlPanel_index + 2) + "\" Children=\"Controls\" ControlName=\"Panel Control Button " + node + "\">")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Name\">PanelButtonControl" + str(bus_nodeControlPanel_index + 2) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Size\">" + str(bus_nodeControlPanel_staticText_lenght) + ", " + str(bus_nodeControlPanel_staticText_height) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Location\">" + str(bus_nodeControlPanel_staticText_location_x) + ", " + str(bus_nodeControlPanel_staticText_location_y) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"PanelList\">1;1;\\" + node + "\\NodeControl_" + node + ".xvp</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"Text\">" + node + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"TabIndex\">" + str(bus_nodeControlPanel_index + 2) + "</Property>")
	bus_nodeControlPanel.write("\n" + indent*4)
	bus_nodeControlPanel.write("<Property Name=\"ClosePanels\">False</Property>")
	bus_nodeControlPanel.write("\n" + indent*3)
	bus_nodeControlPanel.write("</Object>")


	bus_nodeControlPanel_index +=1 
	bus_nodeControlPanel_switchControl_location_y += 50
	bus_nodeControlPanel_staticText_location_y += 50

	if(bus_nodeControlPanel_switchControl_location_y%365 == 0):
		bus_nodeControlPanel_switchControl_location_x += 174 + 15
		bus_nodeControlPanel_staticText_location_x += 286 - 90
		bus_nodeControlPanel_columns_flag = True
		bus_nodeControlPanel_switchControl_location_y = bus_nodeControlPanel_staticText_location_y = 65


	# node_SubPanel.xvp
	canFile_subPanel = open(os.getcwd() + "\\Panels\\" + bus_name + "\\" + node + "\\"+ node + "_SubPanel" +".xvp", "w")

	canFile_subPanel.write("<?xml version=\"1.0\"?>\n" + "<Panel Type=\"Vector.CANalyzer.Panels.PanelSerializer, Vector.CANalyzer.Panels.Serializer," + 
		" Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\">\n")

	canFile_subPanel.write(indent + "<Object Type=\"Vector.CANalyzer.Panels.Runtime.Panel, Vector.CANalyzer.Panels.Common, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"Panel\" Children=\"Controls\" ControlName=\"" + bus_name + " :: " + node +"\">")

	canFile_subPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl1\" Children=\"Controls\" ControlName=\"StaticText_PanelName\">")

	canFile_subPanel.write("\n" + indent*3 + "<Property Name=\"Name\">StaticTextControl1</Property>")
	canFile_subPanel.write("\n" + indent*3 + "<Property Name=\"Size\">350, 24</Property>")
	canFile_subPanel.write("\n" + indent*3 + "<Property Name=\"Location\">5, 5</Property>")
	canFile_subPanel.write("\n" + indent*3 + "<Property Name=\"Font\">Microsoft Sans Serif, 14.25pt, style=Bold</Property>")
	canFile_subPanel.write("\n" + indent*3 + "<Property Name=\"Text\">" + bus_name + " :: " + node + "</Property>")
	canFile_subPanel.write("\n" + indent*2 + "</Object>")

	canFile_subPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.GroupBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"GroupBoxControl1\" Children=\"Controls\" ControlName=\"Group Box\">")


	nodeControlPanel = open(os.getcwd() + "\\Panels\\" + bus_name + "\\" + node + "\\"+ "NodeControl_" + node +".xvp", "w")

	#############NodeControl_node.xvp
	nodeControlPanel.write("<?xml version=\"1.0\"?>\n" + "<Panel Type=\"Vector.CANalyzer.Panels.PanelSerializer, Vector.CANalyzer.Panels.Serializer," + 
		" Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\">\n")

	nodeControlPanel.write(indent + "<Object Type=\"Vector.CANalyzer.Panels.Runtime.Panel, Vector.CANalyzer.Panels.Common, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"Panel\" Children=\"Controls\" ControlName=\"" + bus_name + " :: " + node +"\">")

	nodeControlPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl1\" Children=\"Controls\" ControlName=\"StaticText_PanelName\">")

	nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Name\">StaticTextControl1</Property>")
	nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Size\">350, 24</Property>")
	nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Location\">5, 5</Property>")
	nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Font\">Microsoft Sans Serif, 10pt, style=Bold</Property>")
	nodeControlPanel.write("\n" + indent*3 + "<Property Name=\"Text\">" + bus_name + " :: " + node + " NodeControl" + "</Property>")
	nodeControlPanel.write("\n" + indent*2 + "</Object>")

	nodeControlPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.GroupBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"GroupBoxControl1\" Children=\"Controls\" ControlName=\"Group Box\">")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.SwitchControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"SwitchControl2\" ControlName=\"Switch/Indicator NoE\">")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Name\">SwitchControl1</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Size\">23, 30</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Location\">5, 15</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"StateCnt\">2</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Activation\">Left</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"SwitchValues\">1;2;0;1</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"SymbolConfiguration\">4;16;NodeControl::" + bus_name + ";;;sv_" + node + "_ON_OFF;1;;;-1</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("</Object>")

	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl2\" Children=\"Controls\" ControlName=\"StaticText_Node_Enable\">")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Name\">StaticTextControl2</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Size\">100, 13</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Location\">35, 15</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 8.25pt, style=Bold</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"Text\">" + node + " Node</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"ForeColor\">0, 0, 192</Property>")
	nodeControlPanel.write("\n" + indent*4)
	nodeControlPanel.write("<Property Name=\"TabIndex\">0</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("</Object>")

	nodeControlPanel_index = 1
	nodeControlPanel_size_x = 174
	nodeControlPanel_size_y = 20
	nodeControlPanel_location_x = 15
	nodeControlPanel_location_y = 65
	nodeControlPanel_columns = 1
	nodeControlPanel_columns_flag = False


	index = 1
	location = 15
	firstLocation = 5
	size = 169
	columns = 1
	columns_flag = False
	for message in database[node].keys():
		if(columns_flag):
			columns_flag = False
			columns += 1
		canFile_subPanel.write("\n" + indent*3)
		canFile_subPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.PanelButtonControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"PanelButtonControl" + str(index) +"\" Children=\"Controls\" ControlName=\"" + bus_name + "::" + node + "::" + message + "\">")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"Name\">PanelButtonControl" + str(index) + "</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"Size\">" + str(size) + ", 23</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"Location\">" + str(firstLocation) +", " + str(location) +"</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"ClosePanels\">False</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"PanelList\">1;1;" + node + "_" + message + ".xvp" + "</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"NodeList\">1;0</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"NetworkList\">1;0</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"Text\">" + message + "</Property>")
		canFile_subPanel.write("\n" + indent*4)
		canFile_subPanel.write("<Property Name=\"TabIndex\">" + str(index-1) + "</Property>")
		canFile_subPanel.write("\n" + indent*3)
		canFile_subPanel.write("</Object>")
		index += 1
		location += 25

		if(location%190 == 0):
			firstLocation += 174
			columns_flag = True
			location = 15

		#node_message.xvp
		frameListPanel = open(os.getcwd() + "\\Panels\\" + bus_name + "\\" + node + "\\"+ node + "_" + message +".xvp", "w")

		frameListPanel.write("<?xml version=\"1.0\"?>\n" + "<Panel Type=\"Vector.CANalyzer.Panels.PanelSerializer, Vector.CANalyzer.Panels.Serializer," + 
			" Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\">\n")

		frameListPanel.write(indent + "<Object Type=\"Vector.CANalyzer.Panels.Runtime.Panel, Vector.CANalyzer.Panels.Common, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"Panel\" Children=\"Controls\" ControlName=\"" + bus_name + " :: " + node +"\">")

		frameListPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl1\" Children=\"Controls\" ControlName=\"StaticText_PanelName\">")

		frameListPanel.write("\n" + indent*3 + "<Property Name=\"Name\">StaticTextControl1</Property>")
		frameListPanel.write("\n" + indent*3 + "<Property Name=\"Size\">350, 24</Property>")
		frameListPanel.write("\n" + indent*3 + "<Property Name=\"Location\">5, 5</Property>")
		frameListPanel.write("\n" + indent*3 + "<Property Name=\"Font\">Microsoft Sans Serif, 10pt, style=Bold</Property>")
		frameListPanel.write("\n" + indent*3 + "<Property Name=\"Text\">" + bus_name + " :: " + node + " :: " + message + "</Property>")
		frameListPanel.write("\n" + indent*2 + "</Object>")

		frameListPanel.write("\n" + indent*2 + "<Object Type=\"Vector.CANalyzer.Panels.Design.GroupBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"GroupBoxControl1\" Children=\"Controls\" ControlName=\"Group Box\">")

		framePanel_index = 1
		framePanel_staticText_lenght = 108
		framePanel_staticText_height = 21
		framePanel_staticText_location_x = 5
		framePanel_staticText_location_y = 15

		framePanel_textBox_lenght = 50
		framePanel_textBox_height = 21
		framePanel_textBox_location_x = 118
		framePanel_textBox_location_y = 15
		framePanel_columns = 1
		framePanel_columns_flag = False

		for signal in range(1, len(database[node][message])):
			if(framePanel_columns_flag):
				framePanel_columns_flag = False
				framePanel_columns += 1
			frameListPanel.write("\n" + indent*3)
			frameListPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.StaticTextControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"StaticTextControl" + 
				str(framePanel_index + 1) + "\" Children=\"Controls\" ControlName=\"Static Text Signal" + database[node][message][signal] + "\">")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Name\">StaticTextControl" + str(framePanel_index + 1) +"</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Size\">" + str(framePanel_staticText_lenght) + ", " + str(framePanel_staticText_height) + "</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Location\">" + str(framePanel_staticText_location_x) + ", " + str(framePanel_staticText_location_y) + "</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 8pt</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"TextAlign\">MiddleLeft</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Text\">" + database[node][message][signal] + "</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"ForeColor\">Black</Property>")
			frameListPanel.write("\n" + indent*3)
			frameListPanel.write("</Object>")

			frameListPanel.write("\n" + indent*3)
			frameListPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.TextBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"TextBoxControl" + 
				str(framePanel_index) + "\" Children=\"Controls\" ControlName=\"Input/Output Box " + str(framePanel_index + 1) + "\">")

			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Name\">TextBoxControl" + str(framePanel_index + 1) + "</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Size\">" + str(framePanel_textBox_lenght) + ", " + str(framePanel_textBox_height) + "</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"Location\">" + str(framePanel_textBox_location_x) + ", " + str(framePanel_textBox_location_y) + "</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmUpperTextColor\">WindowText</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"ValueDecimalPlaces\">0</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmLowerBkgColor\">Salmon</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"ValueDisplay\">Decimal</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmUpperBkgColor\">IndianRed</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmLowerTextColor\">WindowText</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"BoxFont\">Microsoft Sans Serif, 9pt</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmUpperFont\">Microsoft Sans Serif, 9pt</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmGeneralSettings\">1;2;0;0</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"DisplayLabel\">Hide</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"TextFont\">Microsoft Sans Serif, 9pt</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"DescriptionText\" />")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"AlarmLowerFont\">Microsoft Sans Serif, 9pt</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"DescriptionSize\">0, 20</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"SymbolConfiguration\">4;2;" + bus_name + ";" + node + 
				";" + message + ";" + database[node][message][signal] + ";1;" + bus_name + ";;-1</Property>")
			frameListPanel.write("\n" + indent*4)
			frameListPanel.write("<Property Name=\"TabIndex\">" + str(framePanel_index - 1) + "</Property>")
			frameListPanel.write("\n" + indent*3)
			frameListPanel.write("</Object>")

			framePanel_index +=1 
			framePanel_staticText_location_y += 25
			framePanel_textBox_location_y += 25

			if(framePanel_staticText_location_y%190 == 0):
				framePanel_staticText_location_x += 174 + 15
				framePanel_textBox_location_x += 286 - 90
				framePanel_columns_flag = True
				framePanel_staticText_location_y = framePanel_textBox_location_y = 15

		if(nodeControlPanel_columns_flag):
			nodeControlPanel_columns_flag = False
			nodeControlPanel_columns += 1

		nodeControlPanel.write("\n" + indent*3)
		nodeControlPanel.write("<Object Type=\"Vector.CANalyzer.Panels.Design.CheckBoxControl, Vector.CANalyzer.Panels.CommonControls, Version=11.0.96.0, Culture=neutral, PublicKeyToken=null\" Name=\"CheckBoxControl" + str(nodeControlPanel_index + 2) + 
			"\" Children=\"Controls\" ControlName=\"Check Box CBE " + str(nodeControlPanel_index + 2) + "\">")
		nodeControlPanel.write("\n" + indent*4)
		nodeControlPanel.write("<Property Name=\"Name\">CheckBoxControl" + str(nodeControlPanel_index + 2) + "</Property>")
		nodeControlPanel.write("\n" + indent*4)
		nodeControlPanel.write("<Property Name=\"Size\">" + str(nodeControlPanel_size_x) + ", " + str(nodeControlPanel_size_y) + "</Property>")
		nodeControlPanel.write("\n" + indent*4)
		nodeControlPanel.write("<Property Name=\"Location\">" + str(nodeControlPanel_location_x) + ", " + str(nodeControlPanel_location_y) + "</Property>")
		nodeControlPanel.write("\n" + indent*4)
		nodeControlPanel.write("<Property Name=\"Text\">" + message + "</Property>")
		nodeControlPanel.write("\n" + indent*4)
		nodeControlPanel.write("<Property Name=\"SymbolConfiguration\">4;16;MessageControl::" + bus_name + "::" + message + ";;;sv_" + message + ";1;;;-1</Property>")
		nodeControlPanel.write("\n" + indent*4)
		nodeControlPanel.write("<Property Name=\"TabIndex\">" + str(nodeControlPanel_index) + "</Property>")
		nodeControlPanel.write("\n" + indent*3)
		nodeControlPanel.write("</Object>")
		nodeControlPanel_index += 1
		nodeControlPanel_location_y += 25

		if(nodeControlPanel_location_y%190 == 0):
			nodeControlPanel_location_x += 185
			nodeControlPanel_columns_flag = True
			nodeControlPanel_location_y = 65

		frameListPanel.write("\n" + indent*3)
		frameListPanel.write("<Property Name=\"Name\">GroupBoxControl1</Property>")
		frameListPanel.write("\n" + indent*3)
		frameListPanel.write("<Property Name=\"Size\">" + str(framePanel_columns * 190) + ", " + ("200" if (framePanel_index > 7) else str(25 * framePanel_index)) + "</Property>")
		frameListPanel.write("\n" + indent*3)
		frameListPanel.write("<Property Name=\"Location\">5, 40</Property>")
		frameListPanel.write("\n" + indent*3)
		frameListPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 9pt, style=Bold</Property>")
		frameListPanel.write("\n" + indent*3)
		frameListPanel.write("<Property Name=\"Text\">" + message + " Signals List</Property>")
		frameListPanel.write("\n" + indent*3)
		frameListPanel.write("<Property Name=\"TabIndex\">0</Property>")
		frameListPanel.write("\n" + indent*2)
		frameListPanel.write("</Object>")
		frameListPanel.write("\n" + indent*2)
		frameListPanel.write("<Property Name=\"Name\">Panel</Property>")
		frameListPanel.write("\n" + indent*2)
		frameListPanel.write("<Property Name=\"Size\">" + str(framePanel_columns * 190 + 10) + ", " + ("240" if (framePanel_index > 7) else str(25 * framePanel_index + 40)) + "</Property>")
		frameListPanel.write("\n" + indent*1)
		frameListPanel.write("</Object>")
		frameListPanel.write("\n" + "</Panel>")

	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Property Name=\"Name\">GroupBoxControl1</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Property Name=\"Size\">" + str(nodeControlPanel_columns * 190) + ", " + ("200" if (nodeControlPanel_index > 7) else str(22 * nodeControlPanel_index)) + "</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Property Name=\"Location\">5, 40</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 9pt, style=Bold</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Property Name=\"Text\">" + node + " NodeControl</Property>")
	nodeControlPanel.write("\n" + indent*3)
	nodeControlPanel.write("<Property Name=\"TabIndex\">0</Property>")
	nodeControlPanel.write("\n" + indent*2)
	nodeControlPanel.write("</Object>")
	nodeControlPanel.write("\n" + indent*2)
	nodeControlPanel.write("<Property Name=\"Name\">Panel</Property>")
	nodeControlPanel.write("\n" + indent*2)
	nodeControlPanel.write("<Property Name=\"Size\">" + str(nodeControlPanel_columns * 190 + 10) + ",  " + ("240" if (nodeControlPanel_index > 7) else str(22 * nodeControlPanel_index + 40)) + "</Property>")
	nodeControlPanel.write("\n" + indent*1)
	nodeControlPanel.write("</Object>")
	nodeControlPanel.write("\n" + "</Panel>")

	canFile_subPanel.write("\n" + indent*3)
	canFile_subPanel.write("<Property Name=\"Name\">GroupBoxControl1</Property>")
	canFile_subPanel.write("\n" + indent*3)
	canFile_subPanel.write("<Property Name=\"Size\">" + str(columns * 185) + ", " + ("200" if (index > 7) else str(22 * index)) + "</Property>")
	canFile_subPanel.write("\n" + indent*3)
	canFile_subPanel.write("<Property Name=\"Location\">5, 40</Property>")
	canFile_subPanel.write("\n" + indent*3)
	canFile_subPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 9pt, style=Bold</Property>")
	canFile_subPanel.write("\n" + indent*3)
	canFile_subPanel.write("<Property Name=\"Text\">" + node + " Messages List</Property>")
	canFile_subPanel.write("\n" + indent*3)
	canFile_subPanel.write("<Property Name=\"TabIndex\">0</Property>")
	canFile_subPanel.write("\n" + indent*2)
	canFile_subPanel.write("</Object>")
	canFile_subPanel.write("\n" + indent*2)
	canFile_subPanel.write("<Property Name=\"Name\">Panel</Property>")
	canFile_subPanel.write("\n" + indent*2)
	canFile_subPanel.write("<Property Name=\"Size\">" + str(columns * 185 + 10) + ", " + ("240" if (index > 7) else str(22 * index + 40)) + "</Property>")
	canFile_subPanel.write("\n" + indent*1)
	canFile_subPanel.write("</Object>")
	canFile_subPanel.write("\n" + "</Panel>")

bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Property Name=\"Name\">GroupBoxControl1</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Property Name=\"Size\">" + str(bus_nodeControlPanel_columns * 190) + ", " + ("365" if (bus_nodeControlPanel_index > 7) else str(50 * bus_nodeControlPanel_index)) + "</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Property Name=\"Location\">5, 40</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Property Name=\"Font\">Microsoft Sans Serif, 9pt, style=Bold</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Property Name=\"Text\">" + bus_name + " NodeControl</Property>")
bus_nodeControlPanel.write("\n" + indent*3)
bus_nodeControlPanel.write("<Property Name=\"TabIndex\">0</Property>")
bus_nodeControlPanel.write("\n" + indent*2)
bus_nodeControlPanel.write("</Object>")
bus_nodeControlPanel.write("\n" + indent*2)
bus_nodeControlPanel.write("<Property Name=\"Name\">Panel</Property>")
bus_nodeControlPanel.write("\n" + indent*2)
bus_nodeControlPanel.write("<Property Name=\"Size\">" + str(bus_nodeControlPanel_columns * 190 + 10) + ",  " + ("405" if (bus_nodeControlPanel_index > 7) else str(50 * bus_nodeControlPanel_index + 40)) + "</Property>")
bus_nodeControlPanel.write("\n" + indent*1)
bus_nodeControlPanel.write("</Object>")
bus_nodeControlPanel.write("\n" + "</Panel>")



allFrames_panel.write("\n" + indent*3)
allFrames_panel.write("<Property Name=\"Name\">GroupBoxControl1</Property>")
allFrames_panel.write("\n" + indent*3)
allFrames_panel.write("<Property Name=\"Size\">" + str(allFrames_panel_columns * 190) + ", " + ("200" if (allFrames_panel_index > 7) else str(25 * allFrames_panel_index)) + "</Property>")
allFrames_panel.write("\n" + indent*3)
allFrames_panel.write("<Property Name=\"Location\">5, 40</Property>")
allFrames_panel.write("\n" + indent*3)
allFrames_panel.write("<Property Name=\"Font\">Microsoft Sans Serif, 9pt, style=Bold</Property>")
allFrames_panel.write("\n" + indent*3)
allFrames_panel.write("<Property Name=\"Text\">" + bus_name + " MainPanel</Property>")
allFrames_panel.write("\n" + indent*3)
allFrames_panel.write("<Property Name=\"TabIndex\">0</Property>")
allFrames_panel.write("\n" + indent*2)
allFrames_panel.write("</Object>")
allFrames_panel.write("\n" + indent*2)
allFrames_panel.write("<Property Name=\"Name\">Panel</Property>")
allFrames_panel.write("\n" + indent*2)
allFrames_panel.write("<Property Name=\"Size\">" + str(allFrames_panel_columns * 190 + 10) + ",  " + ("240" if (allFrames_panel_index > 7) else str(25 * allFrames_panel_index + 40)) + "</Property>")
allFrames_panel.write("\n" + indent*1)
allFrames_panel.write("</Object>")
allFrames_panel.write("\n" + "</Panel>")