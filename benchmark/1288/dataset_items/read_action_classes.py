def read_label_map(label_map_path):
    """Reads a label map file and returns a dictionary mapping label names to
    
    Ref: https://stackoverflow.com/questions/55218726/how-to-open-pbtxt-file
    """

    item_id = None
    item_name = None
    items = {}
    
    with open(label_map_path, "r") as file:
        for line in file:
            line.replace(" ", "")
            if line == "item{":
                pass
            elif line == "}":
                pass
            elif " id:" in line:
                try:
                    item_id = int(line.split(":", 1)[1].strip())
                except:
                    import ipdb; ipdb.set_trace()
            elif " name:" in line:
                item_name = line.split(":", 1)[1].replace("'", "").strip()
                # item_name = line.split(":", 1)[1].replace("'", "").replace('"', "").strip()

            if item_id is not None and item_name is not None:
                items[item_name] = item_id
                item_id = None
                item_name = None

    return items
