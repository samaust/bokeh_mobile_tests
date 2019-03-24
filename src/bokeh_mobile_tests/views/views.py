from django.shortcuts import render

from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.models import BoxZoomTool, PanTool, ResetTool, SaveTool
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

site_title = u'bokeh_mobile_tests'


#-----------------------------------------------------------------------------
# Views
#-----------------------------------------------------------------------------

def plot001(request, **kwargs):
    ''' Displays a plot
        
        Based on sample code :
        https://bokeh.pydata.org/en/latest/docs/user_guide/categorical.html
    '''
    title = u'Plot001'
    
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    counts = [5, 3, 4, 2, 4, 6]

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

    tools = [PanTool(), BoxZoomTool(), SaveTool(), ResetTool()]
    plot = figure(x_range=fruits,
                  y_range=(0,9),
                  plot_height=2000,
                  plot_width=2000, 
                  title="Fruit Counts",
                  toolbar_location="above", 
                  tools=tools,
                  active_drag=None,
                  active_scroll=None,
                  active_tap=None)

    plot.vbar(x='fruits', 
              top='counts',
              width=0.9,
              color='color',
              legend="fruits",
              source=source)
    
    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    
    script_bokeh, div_bokeh = components(plot)
    
    return render(request, 'bokeh_mobile_tests/plot001.html', 
        {'site_title': site_title,
         'title': title,
         'script_bokeh': script_bokeh,
         'div_bokeh': div_bokeh,})
