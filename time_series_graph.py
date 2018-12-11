def timeseries_graph(df, date_column, value_column,title=None,y_axis_label=None,x_axis_label=None,title_align='center' \
                     ,title_font_size='14px',color='black', plot_width=800 \
                     , plot_height=400, tools='wheel_zoom, box_select, reset', x_axis_type='datetime'):
    from bokeh.plotting import output_notebook, figure, show
    output_notebook(hide_banner=True)
    
    p = figure(plot_width= plot_width, plot_height=plot_height, tools=tools, x_axis_type=x_axis_type)
    p.line(df[date_column], df[value_column], color=color)
    p.yaxis.axis_label=y_axis_label
    p.xaxis.axis_label=x_axis_label
    p.title.text=title
    p.title.align=title_align
    p.title.text_font_size = title_font_size
    show(p)
