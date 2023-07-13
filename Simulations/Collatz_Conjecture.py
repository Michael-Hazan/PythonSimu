import pandas 
import plotly.express as px
import alive_progress


max = 1
max = int(input("Amount:"))
num = 0
i = 0
j = 0
currentx = [0]
currenty = [0]
whole = [0]
fig = px.line(currentx, currenty)
with alive_progress.alive_bar(max) as bar:
	for i in range(max):
		num = i+1
		currentx.append(num) # type: ignore
		currenty.append(j) # type: ignore
		while num != 1:
			if num % 2 == 0:
				num /= 2
			else:
				num *= 3
				num += 1
			currentx.append(num) # type: ignore
			currenty.append(j) # type: ignore
			j += 1
		fig.add_traces(list(px.line(x=currenty, y=currentx).select_traces()))
		currentx = []
		currenty = []
		j = 0
		bar()

fig.show()