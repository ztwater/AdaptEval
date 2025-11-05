class MapPrice(Model):
    price_before_vat = DecimalType(serialized_name='priceBeforeVat')
    vat_rate = DecimalType(serialized_name='vatRate')
    vat = DecimalType()
    total_price = DecimalType(serialized_name='totalPrice')
