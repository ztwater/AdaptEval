def f_template(the_string):
    return eval(f"f'{the_string}'")

print(f_template('some "quoted" string'))
print(f_template("some 'quoted' string"))
