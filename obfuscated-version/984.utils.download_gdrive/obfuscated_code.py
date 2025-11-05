import requests

def download_file_from_google_drive(var_0, var_1):
    var_2 = "https://docs.google.com/uc?export=download"

    var_3 = requests.Session()

    var_4 = var_3.get(var_2, params = { 'id' : var_0 , 'confirm': 1 }, stream = True)
    var_5 = get_confirm_token(var_4)

    if var_5:
        var_6 = { 'id' : var_0, 'confirm' : var_5 }
        var_4 = var_3.get(var_2, var_6 = var_6, stream = True)

    save_response_content(var_4, var_1)    

def get_confirm_token(var_4):
    for key, value in var_4.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(var_4, var_1):
    var_7 = 32768

    with open(var_1, "wb") as f:
        for chunk in var_4.iter_content(var_7):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

