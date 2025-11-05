def DecimaltoDMS(Decimal):
    d = int(Decimal)
    m = int((Decimal - d) * 60)
    s = (Decimal - d - m/60) * 3600.00
    z= round(s, 2)
    if d >= 0:
        print ("N ", abs(d), "º ", abs(m), "' ", abs(z), '" ')
    else:
        print ("S ", abs(d), "º ", abs(m), "' ", abs(z), '" ')
