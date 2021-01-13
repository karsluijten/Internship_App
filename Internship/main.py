
from bokeh.io import curdoc
from bokeh.models.widgets import FileInput
from bokeh.models import ColumnDataSource

source = ColumnDataSource(dict())

def upload_fit_data(attr, old, new):
    print("fit data upload succeeded")
    print(file_input.value)
    data = b64decode(file_input.value)
    soure.data = data
    
    
file_input = FileInput(accept=".csv,.json,.txt")
file_input.on_change('value', upload_fit_data)

curdoc().add_root(file_input)
