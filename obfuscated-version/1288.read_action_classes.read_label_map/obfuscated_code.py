def read_label_map(var_0):

    var_1 = None
    var_2 = None
    var_3 = {}
    
    with open(var_0, "r") as file:
        for line in file:
            line.replace(" ", "")
            if line == "item{":
                pass
            elif line == "}":
                pass
            elif "id" in line:
                var_1 = int(line.split(":", 1)[1].strip())
            elif "name" in line:
                var_2 = line.split(":", 1)[1].replace("'", "").replace('"', "").strip()

            if var_1 is not None and var_2 is not None:
                var_3[var_2] = var_1
                var_1 = None
                var_2 = None

    return var_3

