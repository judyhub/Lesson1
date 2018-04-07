# num1 = input ("Enter any number")
# num2 = 56
# num3 = 23
#
# print (int(num1) + int(num2))

from plotly.offline import plot
import plotly.graph_objs as x

marks = [67, 61, 54, 32, 45, 89]
names = ["Ken","martin","joan","ali"]

mygraph = x.Bar(x=names, y=marks)
#diff btwn obj vs variables

data = x.Data ([mygraph])
plot(data)
