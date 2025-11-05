data = []
for idx, var in enumerate(list(df)):
    myPlot = sns.distplot(df[var])
    
    # Fine Line2D objects
    lines2D = [obj for obj in myPlot.findobj() if str(type(obj)) == "<class 'matplotlib.lines.Line2D'>"]
    
    # Retrieving x, y data
    x, y = lines2D[idx].get_data()[0], lines2D[idx].get_data()[1]
    
    # Store as dataframe 
    data.append(pd.DataFrame({'x':x, 'y':y}))
