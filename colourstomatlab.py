arg=input('name to rgb: ')
colour={'light-grey':[211, 211, 211],'lightgreen':[0.66, 0.89, 0.63],'green':[0,128,0],'limegreen':[50,205,50],
'maroon':[128,0,0],'crimson':[220,20,60],'purple':[128,0,128],'darkviolet':[148,0,211],
'deeppink':[255,20,147],'orchid':[218, 112, 214],'violet':[238, 130, 238],'royalblue':[65, 105, 225],'deepskyblue':[0, 191, 255],
'cyan':[0,255,255],'navy':[0,0,128],'blue':[0,0,255],'darkorange':[255, 140, 0],'gold':[255, 215, 0],'yellow':[255, 255, 0],
'grey':[128, 128, 128],'steelblue':[70, 130, 180],'black':[0,0,0],'fuchsia':[255,0,255],'dodgerblue':[30, 144, 255],
'indigo':[75, 0, 130],'darkorchid':[153, 50, 204],'mediumvioletred':[199, 21, 133],'hotpink':[255, 105, 180],
'plum':[112, 0, 81],'lightplum':[221, 160, 221],'lightslategrey':[119, 136, 153],'slategrey':[112, 128, 144],
'g':[0, 128, 0],'lime':[0, 255, 0], 'r':[255, 0, 0],'tomato':[255, 99, 71], 'b':[0,0,255],'y':[255, 255, 0], 'orange':[255, 165, 0],
'lightsteelblue':[176, 196, 222]}
rgb=[0,0,0]
for i in range(0,3):
	rgb[i]=colour[arg][i]/255
print('rgb: ',rgb)
print('RGB: ',colour[arg])