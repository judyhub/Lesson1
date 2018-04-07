from plotly.offline import plot
import plotly.graph_objs as go
#plot displays/draws the graph

labels = ['BMW','TOYOTA','NISSAN','ISUZU','MAZDA']
values = [20000,13000,15000,80000,24000]

#Lets create a Pie Chart.

plot([x.scatter(x=labels, y=values)])
