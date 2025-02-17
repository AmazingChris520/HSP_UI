import PySimpleGUI as sg
import time as timer
import random
import string

def Events(events, values):
	global window
	global pT_ETH_01Graph
	global pT_ETH_02Graph
	global pT_NO_01Graph
	global pT_NO_02Graph
	global pT_NO_03Graph
	global pT_CH_01Graph
	global tOT_WEIGHTGraph
	global tC_01Graph
	global tC_02Graph
	global tC_03Graph

	if values['TABLE'] == [0]:
		pT_ETH_01Graph = not pT_ETH_01Graph
		window['PT-ETH-01'].update(visible=pT_ETH_01Graph)

	elif values['TABLE'] == [1]:
		pT_ETH_02Graph = not pT_ETH_02Graph
		window['PT-ETH-02'].update(visible=pT_ETH_02Graph)

	elif values['TABLE'] == [2]:
		pT_NO_01Graph = not pT_NO_01Graph
		window['PT-NO-01'].update(visible=pT_NO_01Graph)

	elif values['TABLE'] == [3]:
		pT_NO_02Graph = not pT_NO_02Graph
		window['PT-NO-02'].update(visible=pT_NO_02Graph)

	elif values['TABLE'] == [4]:
		pT_NO_03Graph = not pT_NO_03Graph
		window['PT-NO-03'].update(visible=pT_NO_03Graph)

	elif values['TABLE'] == [5]:
		pT_CH_01Graph = not pT_CH_01Graph
		window['PT-CH-01'].update(visible=pT_CH_01Graph)

	elif values['TABLE'] == [6]:
		tOT_WEIGHTGraph = not tOT_WEIGHTGraph
		window['TOT-WEIGHT'].update(visible=tOT_WEIGHTGraph)

	elif values['TABLE'] == [7]:
		tC_01Graph = not tC_01Graph
		window['TC-01'].update(visible=tC_01Graph)

	elif values['TABLE'] == [8]:
		tC_02Graph = not tC_02Graph
		window['TC-02'].update(visible=tC_02Graph)

	elif values['TABLE'] == [9]:
		tC_03Graph = not tC_03Graph
		window['TC-03'].update(visible=tC_03Graph)
		
	window['col2'].contents_changed()

class Sensor:
	global x

	def __init__(self, window, name, Unit):
		self.graph = window
		self.visible = False
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
						
		#self.value.update(self.title + ":\n" + str(self.data) + " " + self.unit)
	
	def Lines(self, start, height, startRange, endRange, stepSize, dist):
		self.graph.move(dist,0)
		self.graph.DrawLine((-500,-500), (-500,1000))
		self.graph.DrawLine((start,0), (500,0))

		tempTitle = self.title + " (" + self.unit + ")" 
		
		self.graph.DrawText(tempTitle, (0,height), color = 'gray', font = fontAndSize)

		stepSize

		for y in range(startRange, endRange, stepSize):    

			if y != 0:
				self.graph.DrawLine((-500,y), (-450,y))    
				self.graph.DrawText(y, (-400,y), color='gray', font=fontAndSize)  

	def Graph(self, color):
		if (abs(self.data-self.tempData)<1):
			self.graph.DrawCircle((x,self.data), 1, line_color = color)
		else:
			self.graph.DrawLine((x,self.tempData), (x,self.data), color, 2)

	def getData(self):
		return [self.title, str(round(self.data,2)) + " " + self.unit]
			
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

pT_ETH_01Color = "#5C8374" 
pT_ETH_02Color = "#087CB4" 
pT_NO_01Color = "#F2613F" 
pT_NO_02Color = "#E95793" 
pT_NO_03Color = "#5C527F" 
pT_CH_01Color = "#A3C7B3" 
tOT_WEIGHTColor = "#FFD166" 
tC_01Color = "#6EC2EC" 
tC_02Color = "#8CA772" 
tC_03Color = "#C44D2F"

column_layout1 = [[ sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,1600), key='PT-ETH-01', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,1600), key='PT-ETH-02', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,1600), key='PT-NO-01', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,1600), key='PT-NO-02', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,1600), key='PT-NO-03', visible = False, background_color=buttonBackgroundColor)],
			[sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-2), graph_top_right=(500,1600), key='PT-CH-01', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-1400), graph_top_right=(500,1400), key='TOT-WEIGHT', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,100), key='TC-01', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,100), key='TC-02', visible = False, background_color=buttonBackgroundColor),
			sg.Graph(canvas_size=(500, 500),graph_bottom_left=(-500,-20), graph_top_right=(500,100), key='TC-03', visible = False, background_color=buttonBackgroundColor),]]

colors = [
	[0, pT_ETH_01Color, backgroundColor],
	[1, pT_ETH_02Color, backgroundColor],
	[2, pT_NO_01Color, backgroundColor],
	[3, pT_NO_02Color, backgroundColor],
	[4, pT_NO_03Color, backgroundColor],
	[5, pT_CH_01Color, backgroundColor],
	[6, tOT_WEIGHTColor, backgroundColor],
	[7, tC_01Color, backgroundColor],
	[8, tC_02Color, backgroundColor],
	[9, tC_03Color, backgroundColor],
]

layout = [[sg.Table(values=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],], headings=["Sensor", "Value"],
					cols_justification = ['l','r'],
					hide_vertical_scroll = True,
					row_height = 100,
					row_colors = colors,
					font = "Comic 25",
					header_background_color = backgroundColor,
					header_text_color = textColor,
					background_color=backgroundColor,
					key='TABLE',
					enable_events=True,
					expand_x=True,
					expand_y=True,), sg.Column(column_layout1, element_justification='left', background_color=backgroundColor,  vertical_alignment='l', k = 'col2', expand_x=True , expand_y=True, size = (1250,2000), scrollable=True, sbar_arrow_color=buttonBackgroundColor, sbar_background_color=buttonBackgroundColor, sbar_frame_color=buttonBackgroundColor, sbar_trough_color=buttonBackgroundColor)]]

window = sg.Window('HSP UI', layout, grab_anywhere=True, finalize=True, background_color=backgroundColor, size = (1920,1080), resizable=True, scaling=1)  

pT_ETH_01 = Sensor(window['PT-ETH-01'], "PT-ETH-01", "psi")
pT_ETH_02 = Sensor(window['PT-ETH-02'], "PT-ETH-02", "psi")
pT_NO_01 = Sensor(window['PT-NO-01'], "PT-NO-01", "psi")
pT_NO_02 = Sensor(window['PT-NO-02'], "PT-NO-02", "psi")
pT_NO_03 = Sensor(window['PT-NO-03'], "PT-NO-03", "psi")
pT_CH_01 = Sensor(window['PT-CH-01'], "PT-CH-01", "psi")
tOT_WEIGHT = Sensor(window['TOT-WEIGHT'], "TOT-Weight", "lb")
tC_01 = Sensor(window['TC-01'], "TC-01", "F")
tC_02 = Sensor(window['TC-02'], "TC-02", "F")
tC_03 = Sensor(window['TC-03'], "TC-03", "F")

# Draw Graph    
x = -500
h = 0
pT_ETH_01Graph = False
pT_ETH_02Graph = False
pT_NO_01Graph = False
pT_NO_02Graph = False
pT_NO_03Graph = False
pT_CH_01Graph = False
tOT_WEIGHTGraph = False
tC_01Graph = False
tC_02Graph = False
tC_03Graph = False

pT_ETH_01.Lines(-500, 1520, 0, 1600, 250, 0)
pT_ETH_02.Lines(-500, 1520, 0, 1600, 250, 0)
pT_NO_01.Lines(-500, 1520, 0, 1600,  250,0)
pT_NO_02.Lines(-500, 1520, 0, 1600,  250,0)
pT_NO_03.Lines(-500, 1520, 0, 1600, 250, 0)
pT_CH_01.Lines(-500, 1520, 0, 1600, 250, 0)
tOT_WEIGHT.Lines(-500, 1330, -1400, 1400, 200, 0)
tC_01.Lines(-500, 95, -20, 100, 10, 0)
tC_02.Lines(-500, 95, -20, 100, 10, 0)
tC_03.Lines(-500, 95, -20, 100, 10, 0)

startingSize = (1920,1080)

with open('C:\\Users\\chris\\Downloads\\test1.csv') as f:
	while True:
		for line in f:
			if line.count(',') >= 10:
				lineValues = line.split(',')
				time = lineValues[0].split(':')

				pT_ETH_01.Assign(lineValues[1])
				pT_ETH_02.Assign(lineValues[2])
				pT_NO_01.Assign(lineValues[3])
				pT_NO_02.Assign(lineValues[4])
				pT_NO_03.Assign(lineValues[5])
				pT_CH_01.Assign(lineValues[6])
				tOT_WEIGHT.Assign(lineValues[7])
				tC_01.Assign(lineValues[8])
				tC_02.Assign(lineValues[9])
				tC_03.Assign(lineValues[10])

				man = [
					pT_ETH_01.getData(),
					pT_ETH_02.getData(),
					pT_NO_01.getData(),
					pT_NO_02.getData(),
					pT_NO_03.getData(),
					pT_CH_01.getData(),
					tOT_WEIGHT.getData(),
					tC_01.getData(),
					tC_02.getData(),
					tC_03.getData(),
					]
				
				window['TABLE'].update(values = man, row_colors = colors)

				pT_ETH_01.Graph(pT_ETH_01Color)
				pT_ETH_02.Graph(pT_ETH_02Color)
				pT_NO_01.Graph(pT_NO_01Color)
				pT_NO_02.Graph(pT_NO_02Color)
				pT_NO_03.Graph(pT_NO_03Color)
				pT_CH_01.Graph(pT_CH_01Color)
				tOT_WEIGHT.Graph(tOT_WEIGHTColor)
				tC_01.Graph(tC_01Color)
				tC_02.Graph(tC_02Color)
				tC_03.Graph(tC_03Color)

				x+=1

				if (x==500):

					x = -250
										
					pT_ETH_01.Lines(-250, 1520, 0, 1600, 250, -750)
					pT_ETH_02.Lines(-250, 1520, 0, 1600, 250, -750)
					pT_NO_01.Lines(-250, 1520, 0, 1600,  250,-750)
					pT_NO_02.Lines(-250, 1520, 0, 1600,  250,-750)
					pT_NO_03.Lines(-250, 1520, 0, 1600, 250, -750)
					pT_CH_01.Lines(-250, 1520, 0, 1600, 250, -750)
					tOT_WEIGHT.Lines(-250, 1330, -1400, 1400, 200, -750)
					tC_01.Lines(-250, 95, -20, 100, 10, -750)
					tC_02.Lines(-250, 95, -20, 100, 10, -750)
					tC_03.Lines(-250, 95, -20, 100, 10, -750)
					
				event, values = window.read(timeout = 0)
				Events(event, values)

				if event == sg.WIN_CLOSED:
					break

		event, values = window.read(timeout = 0) 

		Events(event, values)
		if event == sg.WIN_CLOSED:
			break