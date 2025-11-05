df = pd.read_json('test.json')
df['date_hour'] = [datetime.strptime(date[0:10],'%Y-%m-%d').date() for date in 
df['date_hour']]
