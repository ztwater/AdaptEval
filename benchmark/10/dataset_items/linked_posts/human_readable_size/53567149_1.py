def testKb():
  kbSize = 3746
  kbStr = formatSize(kbSize)
  print("%s -> %s" % (kbSize, kbStr))

def testI():
  iSize = 87533
  iStr = formatSize(iSize, isUnitWithI=True)
  print("%s -> %s" % (iSize, iStr))

def testSeparator():
  seperatorSize = 98654
  seperatorStr = formatSize(seperatorSize, sizeUnitSeperator=" ")
  print("%s -> %s" % (seperatorSize, seperatorStr))

def testBytes():
  bytesSize = 352
  bytesStr = formatSize(bytesSize)
  print("%s -> %s" % (bytesSize, bytesStr))

def testMb():
  mbSize = 76383285
  mbStr = formatSize(mbSize, decimalNum=2)
  print("%s -> %s" % (mbSize, mbStr))

def testTb():
  tbSize = 763832854988542
  tbStr = formatSize(tbSize, decimalNum=2)
  print("%s -> %s" % (tbSize, tbStr))

def testPb():
  pbSize = 763832854988542665
  pbStr = formatSize(pbSize, decimalNum=4)
  print("%s -> %s" % (pbSize, pbStr))


def demoFormatSize():
  testKb()
  testI()
  testSeparator()
  testBytes()
  testMb()
  testTb()
  testPb()

  # 3746 -> 3.7KB
  # 87533 -> 85.5KiB
  # 98654 -> 96.3 KB
  # 352 -> 352.0B
  # 76383285 -> 72.84MB
  # 763832854988542 -> 694.70TB
  # 763832854988542665 -> 678.4199PB
