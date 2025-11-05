df.eval("NumCol > 0.5 and BoolCol and NumCol * BoolCol >0").pipe(lambda x: x.index[x])
