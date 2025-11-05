import math

def format_back_to_bytes(value):
    for power, unit in enumerate(["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]):
        if value[-3:-1] == unit:
            return round(float(value[:-3])*math.pow(2, 10*power))
