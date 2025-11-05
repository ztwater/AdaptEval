def zoom_at(var_0, var_1, var_2, var_3):
    w, h = var_0.size
    var_4 = var_3 * 2
    var_0 = var_0.crop((var_1 - w / var_4, var_2 - h / var_4, 
                    var_1 + w / var_4, var_2 + h / var_4))
    return var_0.resize((w, h), Image.LANCZOS)
