def identical_elements(list):
    series = pd.Series(list)
    if series.nunique() == 1: identical = True
    else:  identical = False
    return identical



identical_elements(['a', 'a'])
Out[427]: True

identical_elements(['a', 'b'])
Out[428]: False
