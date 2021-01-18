#!/usr/bin/env python
# coding: utf-8

from bokeh.io import curdoc, output_notebook
from bokeh.models.widgets import FileInput
from bokeh.models import ColumnDataSource
import yaml
from bokeh.server.server import Server
output_notebook()

pd.set_option('chained_assignment', None)
pd.options.display.float_format = '{:.4f}'.format
import warnings
warnings.filterwarnings('ignore')
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
#import fiona
from os.path import dirname, join

source = ColumnDataSource(dict())

def upload_fit_data(attr, old, new):
    print("fit data upload succeeded")
    print(file_input.value)
    data = b64decode(file_input.value)
    soure.data = data
    
    
file_input = FileInput(accept=".csv,.json,.txt")
file_input.on_change('value', upload_fit_data)

curdoc().add_root(file_input)
