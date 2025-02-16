import PySimpleGUI as sg
import socket
import time as timer

def Send(message):
	TCP_IP = '192.168.1.200' # Pi Ethernet IP Address
	TCP_PORT = 6005
	BUFFER_SIZE = 1024

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(bytes(message,'utf-8'))
	s.close()

def Events(events):
	global a
	global b
	global c
	global d
	global e
	global isFillOpen
	global isMainOn
	global isIgniteOn
	global isVentOpen
	global window
	global LoadGraph
	global TPGraph
	global VDGraph
	global IPGraph
	global ITGraph
	global CTGraph
	global FPGraph
	global FlightMode
	global isSeq
	global seqTime
	global start_time

	if event == "FS":
		isFillOpen = True
		Send("fill on")

	elif event == "OM":
		isMainOn = True
		Send("main on")

	elif event == "SI":
		isIgniteOn = True
		Send("ignite on")

	elif event == "OV":
		isVentOpen = True
		Send("vent on")

	elif event == "Close Fill Servo":
		isFillOpen = False
		Send("fill off")

	elif event == "Close Main":
		isMainOn = False
		Send("main off")

	elif event == "Close Ignition":
		isIgniteOn = False
		Send("ignite off")

	elif event == "Close Vent":
		isVentOpen = False
		Send("vent off")

	elif event == "Seq":
		try:
			seqTime = float(values['inp'])
			isSeq = True
			isVentOpen = True
			start_time = timer.time()
			Send("vent on")
		except:
			window['Seq'].update(disabled=True)
			window['inp'].update(readonly=False)
			e+=1

	elif event == "Arm Fill":
		if (a % 2 == 1):
			window['FS'].update(disabled=False)
		else:
			window['FS'].update(disabled=True)

		a+=1

	elif event == "Arm Main":
		if (b % 2 == 1):
			window['OM'].update(disabled=False)
		else:
			window['OM'].update(disabled=True)

		b+=1

	elif event == "Arm Ignition":
		if (c % 2 == 1):
			window['SI'].update(disabled=False)
		else:
			window['SI'].update(disabled=True)

		c+=1

	elif event == "Arm Vent":
		if (d % 2 == 1):
			window['OV'].update(disabled=False)
		else:
			window['OV'].update(disabled=True)

		d+=1

	elif event == "Arm Seq":
		if (e % 2 == 1):
			window['Seq'].update(disabled=False)
			window['inp'].update(readonly=True)
		else:
			window['Seq'].update(disabled=True)
			window['inp'].update(readonly=False)

		e+=1

	elif event == 'LOAD':
		LoadGraph = not LoadGraph
		window['LoadGraph'].update(visible=LoadGraph)
		
	elif event == 'TP':
		TPGraph = not TPGraph
		window['TPGraph'].update(visible=TPGraph)
		
	elif event == 'VD':
		VDGraph = not VDGraph
		window['VDGraph'].update(visible=VDGraph)
		
	elif event == 'IT':
		ITGraph = not ITGraph
		window['ITGraph'].update(visible=ITGraph)
		
	elif event == 'IP':
		IPGraph = not IPGraph
		window['IPGraph'].update(visible=IPGraph)
		
	elif event == 'CT':
		CTGraph = not CTGraph
		window['CTGraph'].update(visible=CTGraph)
		
	elif event == 'FP':
		FPGraph = not FPGraph
		window['FPGraph'].update(visible=FPGraph)
	
	elif event == "Check":
		FlightMode = not FlightMode
		if FlightMode:
			window['CT'].update(visible=False)
			window['IT'].update(visible=False)
			window['CTGraph'].update(visible=False)
			window['ITGraph'].update(visible=False)
		else:
			window['CT'].update(visible=True)
			window['IT'].update(visible=True)

	window['dsd'].contents_changed()

class Sensor:
	global x

	def __init__(self, window, box, name, Unit):
		self.graph = window
		self.visible = False
		self.value = box
		self.tempData = 0
		self.data = 0
		self.title = name
		self.unit = Unit

	def Assign(self, value):
		self.tempData = self.data
		try:
			self.data = float(value)
		except:
			self.data = 0
						
		self.value.update(self.title + ":\n" + str(self.data) + " " + self.unit)

	def Lines(self, start, height, startRange, endRange, dist):
		self.graph.move(dist,0)
		self.graph.DrawLine((-500,-500), (-500,1000))
		self.graph.DrawLine((start,0), (500,0))

		v = 100

		tempTitle = self.title + " (" + self.unit + ")" 
		
		self.graph.DrawText(tempTitle, (0,height), color = 'gray', font = fontAndSize)

		temp = int(((abs(startRange)+abs(endRange))/10))

		for y in range(startRange, endRange, round(temp,-1)):    

			if endRange == 1000:
				self.graph.DrawLine((-500,v), (-450,v))    
				self.graph.DrawText(v, (-400,v), color='gray', font=fontAndSize)  
				v+=100

			elif y != 0:
				self.graph.DrawLine((-500,y), (-450,y))    
				self.graph.DrawText(y, (-400,y), color='gray', font=fontAndSize)  

	def Graph(self, color):
		if (abs(self.data-self.tempData)<1):
			self.graph.DrawCircle((x,self.data), 1, line_color = color)
		else:
			self.graph.DrawLine((x,self.tempData), (x,self.data), color, 2)
			

# Original Colors by Ashlyn
# backgroundColor = "#32B1D0"
# buttonColor = "#983C3C"

backgroundColor = "#121212"
buttonColor = "#8e3563"
disabledButton = "#000000"
buttonBackgroundColor = "#222222"
offColor = "#28bc64"
onColor = "#6f0000"
textColor = "#bcbcbc"
fontAndSize = "Comic 15"
font2 = "Comic 20"
padding = [10,10]
paddingSensor = [15,2]

column_layout1 = [ [sg.Text("Main", text_color = textColor, background_color=backgroundColor, justification='c', font = font2, p=padding, key = 'Main'), sg.Button("Arm", key = 'Arm Main', button_color = buttonColor, font = font2, p=padding)],
					[sg.Button("On", button_color = buttonColor, key = 'OM', disabled = True, font = font2, p=padding), sg.Button("Off", key = 'Close Main', button_color = buttonColor,  font = font2, p=padding), sg.Text(key = 'MA', justification = 'center', background_color = offColor,  font = font2, p=padding)],
					[sg.Text("Ignition", text_color = textColor, background_color=backgroundColor,  font = font2, p=padding), sg.Button("Arm", key = 'Arm Ignition', button_color = buttonColor,  font = font2, p=padding)],
					[sg.Button("On", key = 'SI', disabled = True, button_color = buttonColor,  font = font2, p=padding), sg.Button("Off", key = 'Close Ignition', button_color = buttonColor,  font = font2, p=padding), sg.Text(key = 'IA', justification = 'center', background_color = offColor,  font = font2, p=padding)],
					[sg.Text("Fill", text_color = textColor, background_color=backgroundColor,  font = font2, p=padding), sg.Button("Arm", key = 'Arm Fill', button_color = buttonColor,  font = font2, p=padding)],
					[sg.Button("On", key = 'FS', disabled = True, button_color = buttonColor,  font = font2, p=padding), sg.Button("Off", key = 'Close Fill Servo', button_color = buttonColor,  font = font2), sg.Text(key = 'FA', justification = 'center', background_color = offColor,  font = font2, p=padding)],
					[sg.Text("Purge", text_color = textColor, background_color=backgroundColor,  font = font2, p=padding), sg.Button("Arm", key = 'Arm Vent', button_color = buttonColor,  font = font2, p=padding)],
					[sg.Button("On", key = 'OV', disabled = True, button_color = buttonColor,  font = font2, p=padding), sg.Button("Off", key = 'Close Vent', button_color = buttonColor,  font = font2, p=padding), sg.Text(key = 'TA', justification = 'center', background_color = offColor,  font = font2, p=padding)],
					[sg.Text("Automatic Purge Sequence (Input Time In Seconds)", text_color = textColor, background_color=backgroundColor,  font = font2, p=padding)],
				    [sg.Input("", font=font2, k = 'inp', p=padding, size=(10,20))],
					[sg.Button("On", key = 'Seq', disabled = True, button_color = buttonColor,  font = font2), sg.Button("Arm", key = 'Arm Seq', button_color = buttonColor,  font = font2, p=padding)],
				    [sg.Checkbox("Launch Mode", font=font2, background_color=backgroundColor, checkbox_color=buttonColor, key='Check', enable_events=True, p=padding)]]

column_layout2 = [	
			[ sg.Button(key = 'LOAD', button_color = ("#5C8374",buttonBackgroundColor),  font = fontAndSize, size = paddingSensor), sg.Button(key = 'TP', button_color = ("#087cb4", buttonBackgroundColor),  font = fontAndSize, size = paddingSensor), sg.Button(key = 'VD', button_color = ("#F2613F",buttonBackgroundColor),  font = fontAndSize, size = paddingSensor)]]

col_layout3 = [[ sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-20), graph_top_right=(500,200), key='LoadGraph', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-20), graph_top_right=(500,1000), key='TPGraph', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-50), graph_top_right=(500,60), key='VDGraph', visible = False, background_color=buttonBackgroundColor)],
			[sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-2), graph_top_right=(500,100), key='ITGraph', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-20), graph_top_right=(500,1000), key='IPGraph', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-2), graph_top_right=(500,100), key='CTGraph', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(400, 400),graph_bottom_left=(-500,-20), graph_top_right=(500,1000), key='FPGraph', visible = False, background_color=buttonBackgroundColor)]]

col_layout4 = [[sg.Button(key = 'FP', button_color = ('#5C527F',buttonBackgroundColor),  font = fontAndSize, size = paddingSensor), sg.Button(key = 'IP', button_color = ('#5C527F',buttonBackgroundColor),  font = fontAndSize, size = paddingSensor)],
			[sg.Button(key = 'CT', button_color = ('#E95793',buttonBackgroundColor),  font = fontAndSize, size = paddingSensor), sg.Button(key = 'IT', button_color = ('#E95793',buttonBackgroundColor),  font = fontAndSize, size = paddingSensor)] ]

column_layout5 = [[sg.Col(column_layout2, background_color=backgroundColor, k = 'col2.5')], [sg.Column(col_layout3, scrollable=True, key='dsd', background_color=backgroundColor, expand_x=True , expand_y=True, sbar_arrow_color=buttonBackgroundColor, sbar_background_color=buttonBackgroundColor, sbar_frame_color=buttonBackgroundColor, sbar_trough_color=buttonBackgroundColor)], [sg.Col(col_layout4, background_color=backgroundColor, k='col4.5')]]

layout = [[sg.Column(column_layout1, element_justification='left', background_color=backgroundColor, expand_x=True, expand_y=True, k = 'col1'), sg.Column(column_layout5, element_justification='center', background_color=backgroundColor,  vertical_alignment='c', k = 'col2', expand_x=True , expand_y=True)]]

window = sg.Window('Valkryie UI', layout, grab_anywhere=True, finalize=True, background_color=backgroundColor, size = (1280,720), resizable=True, scaling=1)  

load = Sensor(window['LoadGraph'], window['LOAD'], "Load", "kg")
tankPress = Sensor(window['TPGraph'], window['TP'], "Tank Press", "psi")
tankTemp = Sensor(window['VDGraph'], window['VD'], "Tank Temp", "C")
combPress = Sensor(window['IPGraph'], window['IP'], "Comb Press", "psi")
combTopTemp = Sensor(window['ITGraph'], window['IT'], "Comb Top Temp", "C")
combBotTemp = Sensor(window['CTGraph'], window['CT'], "Comb Bot Temp", "C")
feedPress = Sensor(window['FPGraph'], window['FP'], "Feed Press", "psi")

# Draw Graph    
x = -500
h = 0
a = 1
b = 1
c = 1
d = 1
e = 1
isFillOpen = False
isVentOpen = False
isMainOn = False
isIgniteOn = False
LoadGraph = False
TPGraph = False
VDGraph = False
IPGraph = False
ITGraph = False
CTGraph = False
FPGraph = False
FlightMode = False
seqTime = 0
isSeq = False
start_time = 0

load.Lines(-500, 190, 20, 200, 0)
tankPress.Lines(-500, 950, 100, 1000, 0)
tankTemp.Lines(-500, 55, -40, 60, 0)
combPress.Lines(-500, 950, 100, 1000, 0)
combTopTemp.Lines(-500, 95, 10, 100, 0)
combBotTemp.Lines(-500, 95, 10, 100, 0)
feedPress.Lines(-500, 950, 100, 1000, 0)
startingSize = (1920,1080)

with open('C:\\Users\\chris\\Documents\\ValkryieLaunchData.csv') as f:
	while True:
		for line in f:
			if line.count(',') >= 13:
				lineValues = line.split(',')
				time = lineValues[0].split(':')

				if isSeq:
					if (timer.time() - start_time > seqTime):
						isVentOpen = False
						Send("vent off")
						isSeq = False

				load.Assign(lineValues[11])
				tankPress.Assign(lineValues[2])
				tankTemp.Assign(lineValues[1])
				combTopTemp.Assign(lineValues[3])
				combBotTemp.Assign(lineValues[4])
				combPress.Assign(lineValues[6])
				feedPress.Assign(lineValues[5])
				'''
				windowSize = window.size
				column = window['col1']
				newSize = "Comic " + str(int((0.002)*((windowSize[0]*windowSize[1])/100)))
				for row in column.Rows:
					for element in row:
						element.Widget.config(font = newSize)
				newerSize = "Comic " + str(int((0.0015)*((windowSize[0]*windowSize[1])/100)))
				column = window['col2.5']
				for row in column.Rows:
					for element in row:
						element.Widget.config(font = newerSize)
				column = window['col4.5']
				for row in column.Rows:
					for element in row:
						element.Widget.config(font = newerSize)
						'''
				if (isFillOpen):
					window['FA'].update("Feed Line Open", background_color = onColor)
				else:
					window['FA'].update("Feed Line Closed", background_color = offColor)

				if (isVentOpen):
					window['TA'].update("Purge Valve Open", background_color = onColor)
				else:
					window['TA'].update("Purge Valve Closed", background_color = offColor)

				if (isMainOn):
					window['MA'].update("Main OX On", background_color = onColor)
				else:
					window['MA'].update("Main OX Off", background_color = offColor)

				if (isIgniteOn):
					window['IA'].update("Ignition On", background_color = onColor)
				else:
					window['IA'].update("Ignition Off", background_color = offColor)

				load.Graph('#5C8374')
				tankPress.Graph('#087cb4')
				tankTemp.Graph('#F2613F')
				combTopTemp.Graph('#E95793')
				combBotTemp.Graph('#E95793')
				combPress.Graph('#5C527F')
				feedPress.Graph('#5C527F')

				x+=1

				if (x==500):

					x = -250

					load.Lines(-250, 190, 20, 200, -750)
					tankPress.Lines(-250, 950, 100, 1000, -750)
					tankTemp.Lines(-250, 55, -40, 60, -750)
					combPress.Lines(-250, 950, 100, 1000, -750)
					combTopTemp.Lines(-250, 95, 10, 100, -750)
					combBotTemp.Lines(-250, 95, 10, 100, -750)
					feedPress.Lines(-250, 950, 100, 1000, -750)
					
				event, values = window.read(timeout = 1)

				Events(event)

				if event == sg.WIN_CLOSED:
					break

		if (isFillOpen):
			window['FA'].update("Feed Line Open", background_color = onColor)
		else:
			window['FA'].update("Feed Line Closed", background_color = offColor)

		if (isVentOpen):
			window['TA'].update("Purge Valve Open", background_color = onColor)
		else:
			window['TA'].update("Purge Valve Closed", background_color = offColor)

		if (isMainOn):
			window['MA'].update("Main OX On", background_color = onColor)
		else:
			window['MA'].update("Main OX Off", background_color = offColor)

		if (isIgniteOn):
			window['IA'].update("Ignition On", background_color = onColor)
		else:
			window['IA'].update("Ignition Off", background_color = offColor)

		event, values = window.read(timeout = 1) 

		if isSeq:
			if (timer.time() - start_time > seqTime):
				isVentOpen = False
				Send("vent off")
				isSeq = False

		Events(event)
		if event == sg.WIN_CLOSED:
			break