from plotly.offline import plot
import plotly.graph_objs as go
#plot displays/draws the graph

x = ['BMW','TOYOTA','NISSAN','ISUZU','MAZDA']
y = [20000,13000,15000,80000,24000]

#Lets create a Pie Chart.

mypie = go.Pie(labels=x,values=y)

#Plot it
plot([mypie])