object = bucket.Object('tiles/10/S/DG/2015/12/7/0/B01.jp2')
img_data = object.get().get('Body').read()
