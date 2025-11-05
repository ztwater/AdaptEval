def formatSize(sizeInBytes, decimalNum=1, isUnitWithI=False, sizeUnitSeperator=""):
  """format size to human readable string"""
  # https://en.wikipedia.org/wiki/Binary_prefix#Specific_units_of_IEC_60027-2_A.2_and_ISO.2FIEC_80000
  # K=kilo, M=mega, G=giga, T=tera, P=peta, E=exa, Z=zetta, Y=yotta
  sizeUnitList = ['','K','M','G','T','P','E','Z']
  largestUnit = 'Y'

  if isUnitWithI:
    sizeUnitListWithI = []
    for curIdx, eachUnit in enumerate(sizeUnitList):
      unitWithI = eachUnit
      if curIdx >= 1:
        unitWithI += 'i'
      sizeUnitListWithI.append(unitWithI)

    # sizeUnitListWithI = ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']
    sizeUnitList = sizeUnitListWithI

    largestUnit += 'i'

  suffix = "B"
  decimalFormat = "." + str(decimalNum) + "f" # ".1f"
  finalFormat = "%" + decimalFormat + sizeUnitSeperator + "%s%s" # "%.1f%s%s"
  sizeNum = sizeInBytes
  for sizeUnit in sizeUnitList:
      if abs(sizeNum) < 1024.0:
        return finalFormat % (sizeNum, sizeUnit, suffix)
      sizeNum /= 1024.0
  return finalFormat % (sizeNum, largestUnit, suffix)
