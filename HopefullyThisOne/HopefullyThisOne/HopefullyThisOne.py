import PySimpleGUI as sg
import time as timer
import random
import string
import operator

def sort_table(table, cols):
    """ sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list
               represents a row
        cols:  a list (or tuple) specifying the column numbers to sort by
               e.g. (1,0) would sort by column 1, then by column 0
    """
    for col in reversed(cols):
        try:
            table = sorted(table, key=operator.itemgetter(col))
        except Exception as e:
            sg.popup_error('Error in sort_table', 'Exception in sort_table', e)
    return table

def Events(events, values):
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

	if event == 'Double':
		for i in range(1, len(data)):
			data.append(data[i])
		window['-TABLE-'].update(values=data[1:][:])
	if isinstance(event, tuple):
		# TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
		if event[0] == '-TABLE-':
			if event[2][0] == -1 and event[2][1] != -1:           # Header was clicked and wasn't the "row" column
				col_num_clicked = event[2][1]
				new_table = sort_table(data[1:][:],(col_num_clicked, 0))
				window['-TABLE-'].update(new_table)
				data = [data[0]] + new_table
			window['-CLICKED-'].update(f'{event[2][0]},{event[2][1]}')
	print(values['TABLE'])
	if values['TABLE'] == [0]:
		print("geeffsd")
		LoadGraph = not LoadGraph
		window['LoadGraph'].update(visible=LoadGraph)
		
	elif event == 'TABLE':
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

column_layout5 = [[sg.Column(column_layout1, scrollable=True, key='dsd', background_color=backgroundColor, expand_x=True , expand_y=True, sbar_arrow_color=buttonBackgroundColor, sbar_background_color=buttonBackgroundColor, sbar_frame_color=buttonBackgroundColor, sbar_trough_color=buttonBackgroundColor)]]

colors = [
	[0, "#000000", backgroundColor],
	[1, "#023000", backgroundColor],
	[2, "#006050", backgroundColor],
	[3, "#000540", backgroundColor],
	[4, "#034000", backgroundColor],
	[5, "#002600", backgroundColor],
	[6, "#001200", backgroundColor],
	[7, "#002300", backgroundColor],
	[8, "#004320", backgroundColor],
	[9, "#006500", backgroundColor],
]

layout = [[sg.Table(values=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],], headings=["Sensor", "Value"],
					cols_justification = ['l','r'],
					col_widths = [1,1],
					def_col_width = 2,
					auto_size_columns = False,
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
					expand_y=True,), sg.Column(column_layout5, element_justification='center', background_color=backgroundColor,  vertical_alignment='c', k = 'col2', expand_x=True , expand_y=True)]]

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
LoadGraph = False
TPGraph = False
VDGraph = False
IPGraph = False
ITGraph = False
CTGraph = False
FPGraph = False

pT_ETH_01.Lines(-500, 950, -10, 1600, 0)
pT_ETH_02.Lines(-500, 190, -10, 1600, 0)
pT_NO_01.Lines(-500, 190, -10, 1600, 0)
pT_NO_02.Lines(-500, 190, -10, 1600, 0)
pT_NO_03.Lines(-500, 190, -10, 1600, 0)
pT_CH_01.Lines(-500, 190, -10, 1600, 0)
tOT_WEIGHT.Lines(-500, 1200, -1400, 1400, 0)
tC_01.Lines(-500, 90, -20, 100, 0)
tC_02.Lines(-500, 90, -20, 100, 0)
tC_03.Lines(-500, 90, -20, 100, 0)

'''
load.Lines(-500, 190, 20, 200, 0)
tankPress.Lines(-500, 950, 100, 1000, 0)
tankTemp.Lines(-500, 55, -40, 60, 0)
combPress.Lines(-500, 950, 100, 1000, 0)
combTopTemp.Lines(-500, 95, 10, 100, 0)
combBotTemp.Lines(-500, 95, 10, 100, 0)
feedPress.Lines(-500, 950, 100, 1000, 0)
'''
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

				'''
				load.Assign(lineValues[11])
				tankPress.Assign(lineValues[2])
				tankTemp.Assign(lineValues[1])
				combTopTemp.Assign(lineValues[3])
				combBotTemp.Assign(lineValues[4])
				combPress.Assign(lineValues[6])
				feedPress.Assign(lineValues[5])
				'''

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

				'''
				load.Graph('#5C8374')
				tankPress.Graph('#087cb4')
				tankTemp.Graph('#F2613F')
				combTopTemp.Graph('#E95793')
				combBotTemp.Graph('#E95793')
				combPress.Graph('#5C527F')
				feedPress.Graph('#5C527F')
				'''

				pT_ETH_01.Graph('#5C527F')
				pT_ETH_02.Graph('#5C527F')
				pT_NO_01.Graph('#5C527F')
				pT_NO_02.Graph('#5C527F')
				pT_NO_03.Graph('#5C527F')
				pT_CH_01.Graph('#5C527F')
				tOT_WEIGHT.Graph('#5C527F')
				tC_01.Graph('#5C527F')
				tC_02.Graph('#5C527F')
				tC_03.Graph('#5C527F')

				x+=1

				if (x==500):

					x = -250
					
					pT_ETH_01.Lines(-250, 950, -10, 1600, -750)
					pT_ETH_02.Lines(-250, 190, -10, 1600, -750)
					pT_NO_01.Lines(-250, 190, -10, 1600, -750)
					pT_NO_02.Lines(-250, 190, -10, 1600, -750)
					pT_NO_03.Lines(-250, 190, -10, 1600, -750)
					pT_CH_01.Lines(-250, 190, -10, 1600, -750)
					tOT_WEIGHT.Lines(-250, 1200, -1400, 1400, -750)
					tC_01.Lines(-250, 90, -20, 100, -750)
					tC_02.Lines(-250, 90, -20, 100, -750)
					tC_03.Lines(-250, 90, -20, 100, -750)
					
					'''
					load.Lines(-250, 190, 20, 200, -750)
					tankPress.Lines(-250, 950, 100, 1000, -750)
					tankTemp.Lines(-250, 55, -40, 60, -750)
					combPress.Lines(-250, 950, 100, 1000, -750)
					combTopTemp.Lines(-250, 95, 10, 100, -750)
					combBotTemp.Lines(-250, 95, 10, 100, -750)
					feedPress.Lines(-250, 950, 100, 1000, -750)
					'''
					
				event, values = window.read(timeout = 1)
				Events(event, values)

				if event == sg.WIN_CLOSED:
					break

		event, values = window.read(timeout = 1) 

		Events(event, values)
		if event == sg.WIN_CLOSED:
			break