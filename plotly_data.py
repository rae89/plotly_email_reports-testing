
###########################
#### Generate Plotly Data  #######
###########################

import plotly.plotly as py
from plotly.graph_objs import *

# Dataset 1

data = Data([
    Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
])

#url1 = py.plot(data, filename='privacy-secret', sharing='secret')
url1 = "https://plot.ly/~robertnixhydra/12.png?share_key=ZeNhjo863BR7FuTY6zmdy8"





# Dataset 2

from plotly.tools import FigureFactory as FF

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

table = FF.create_table(data_matrix)
#url2 = py.plot(table, filename='simple_table')
url2 = "https://plot.ly/~robertnixhydra/14"
