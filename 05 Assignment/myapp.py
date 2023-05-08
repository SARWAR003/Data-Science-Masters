from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models.widgets import Slider
import numpy as np

# Define the data
x = np.random.normal(size=200)
y = np.random.normal(size=200)

# Create a ColumnDataSource object to hold the data
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a new plot
plot = figure(plot_width=400, plot_height=400)
plot.scatter('x', 'y', source=source)

# Define a callback function that updates the data
def callback(attr, old, new):
    x = np.random.normal(size=200)
    y = np.random.normal(size=200)
    source.data = dict(x=x, y=y)

# Create a slider widget
slider = Slider(start=0, end=10, value=1, step=1, title="Update Frequency")
slider.on_change('value', callback)

# Add the plot and slider to the current document
curdoc().add_root(column(plot, slider))
