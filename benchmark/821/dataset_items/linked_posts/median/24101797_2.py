statistics.median(map(float, items))
#>>> 3.0

from decimal import Decimal
statistics.median(map(Decimal, items))
#>>> Decimal('3')
