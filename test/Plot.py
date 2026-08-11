import plotly.graph_objects as go
import plotly.figure_factory as ff
import math
  
fig = go.Figure(data=go.Scatterpolar(
    r=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    theta=[69, 141, 213, 285, 357,
           429, 501, 573, 645],
    mode='markers',
))
  
fig.show()

r=[1, 2, 3, 4, 5, 6, 7, 8, 9]
theta=[69, 141, 213, 285, 357,429, 501, 573, 645]
x = []
y = []
originx = []
originy = []
for i in range(len(r)):
    x.append(r[i]*math.cos(theta[i]))
    y.append(r[i]*math.sin(theta[i]))
    originx.append(0)
    originy.append(0)
fig1 = ff.create_quiver(originx,originy,x,y)
fig1.add_trace(go.Scatterpolar(
    r=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    theta=[69, 141, 213, 285, 357,
           429, 501, 573, 645],
    mode='markers',))
fig1.show()
