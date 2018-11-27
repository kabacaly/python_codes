def barh_plot(df, xlabel, ylabel, legend, x_col, y_col, label_col, title, file_name, 
              colors, annotate=True, show_legend=True, legend_position='lower right'):
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    fig = plt.figure(figsize=(20,10))
    plt.rcParams["axes.grid"] = True
    plt.rcParams["axes.edgecolor"] = "0.15"
    plt.rcParams["axes.linewidth"]  = 1.25
    
    for g in range(len(legend)):        
        msk = (df[label_col]==legend[g])
        plt.barh(df[msk][x_col], width=df[msk][y_col], color=colors[g], label=legend[g])

        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        plt.title(title, fontsize=18)
        
        ax = plt.gca()
        ax.set_facecolor('#ffffff')

        plt.xticks(fontsize=12, fontweight='bold')
        plt.yticks(fontsize=12, fontweight='bold')

    if annotate:
        rects = ax.patches

        totals = []

        # find the values and append to list
        for i in ax.patches:
            totals.append(i.get_width())
        total = sum(totals)
        avg = np.median(totals)
        
        #credit : https://stackoverflow.com/a/48372659
        for rect in rects:
            # Get X and Y placement of label from rect.
            x_value = rect.get_width()
            y_value = rect.get_y() + rect.get_height() / 2    

            # Number of points between bar and label. Change to your liking.
            space = 10
            # Vertical alignment for positive values
            ha = 'left'

            # If value of bar is negative: Place label left of bar
            if x_value < 0:
                # Invert space to place label to the left
                space *= -1
                # Horizontally align label at right or left
                ha = 'left'

            # Use X value as label and format number with one decimal place
            label = "{:.2f}".format(x_value/total*100) + '%'

            # Create annotation
            plt.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(space, 0),          # Horizontally shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                va='center',                # Vertically center label
                ha=ha,                      # Horizontally align label differently for
                rotation='vertical',
                fontsize=10
            )                               # positive and negative values.    
    if show_legend:
        plt.legend(loc=legend_position)
    
    plt.show()

    fig.savefig(file_name)    
    
def bar_plot(df, xlabel, ylabel, legend, x_col, y_col, label_col, title, file_name, 
             colors, annotate=True, show_legend=True, legend_position='lower right'):
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    fig = plt.figure(figsize=(20,10))
    plt.rcParams["axes.grid"] = True
    plt.rcParams["axes.edgecolor"] = "0.15"
    plt.rcParams["axes.linewidth"]  = 1.25
    
    for g in range(len(legend)):        
        msk = (df[label_col]==legend[g])
        plt.bar(df[msk][x_col], height=df[msk][y_col], color=colors[g], label=legend[g])

        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        plt.title(title, fontsize=18)
        
        ax = plt.gca()
        ax.set_facecolor('#ffffff')

        plt.xticks(fontsize=12, fontweight='bold')
        plt.yticks(fontsize=12, fontweight='bold')

    if annotate:
        rects = ax.patches

        totals = []

        # find the values and append to list
        for i in ax.patches:
            totals.append(i.get_width())
        total = sum(totals)
        avg = np.median(totals)
        
        #credit : https://stackoverflow.com/a/48372659
        for rect in rects:
            # Get X and Y placement of label from rect.
            x_value = rect.get_width()
            y_value = rect.get_y() + rect.get_height() / 2    

            # Number of points between bar and label. Change to your liking.
            space = 10
            # Vertical alignment for positive values
            ha = 'left'

            # If value of bar is negative: Place label left of bar
            if x_value < 0:
                # Invert space to place label to the left
                space *= -1
                # Horizontally align label at right or left
                ha = 'left'

            # Use X value as label and format number with one decimal place
            label = "{:.2f}".format(x_value/total*100) + '%'

            # Create annotation
            plt.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(space, 0),          # Horizontally shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                va='center',                # Vertically center label
                ha=ha,                      # Horizontally align label differently for
                rotation='vertical',
                fontsize=10
            )                               # positive and negative values.    
    if show_legend:
        plt.legend(loc=legend_position)
    
    plt.show()

    fig.savefig(file_name)        
