arg=input('name : ')
colour={'orchid':[218, 214, 112],'violet':[238, 130, 238],'g':[0, 128, 0],'lime':[0, 255, 0], 'r':[255, 0, 0], 
'tomato':[255, 99, 71],'purple':[128, 0, 128], 'darkviolet':[148, 0, 211],'royalblue':[65, 105, 225],
'deepskyblue':[0, 191, 255],'navy':[0, 0, 128], 'b':[0,0,255],'y':[255, 255, 0], 'orange':[255, 165, 0],
'darkorange':[255, 140, 0],'gold':[255, 215, 0],'deeppink':[255, 20, 147],'cyan':[0,255,255],'limegreen':[50, 205, 50],
'crimson':[220, 20, 60],'maroon':[128,0,0],'slategrey':[112, 128, 144],'lightsteelblue':[176, 196, 222],
'steelblue':[70, 130, 180],'grey':[128, 128, 128]}
matlab=[0,0,0]
for i in range(0,3):
	matlab[i]=colour[arg][i]/255
print('rgb: ',matlab)