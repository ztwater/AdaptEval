def time_ago(self):
        start_time = self.date # The start date
        now_time = datetime.now()

        difference = int((now_time - start_time).total_seconds())

        second = [1, 'seconds']
        minute = [60, 'minutes']
        hour = [60 * minute[0], 'hours']
        day = [24 * hour[0], 'days']
        week = [7 * day[0], 'weeks']
        month = [4 * week[0], 'months']
        year = [12 * month[0], 'years']

        times = [year, month, week, day, hour, minute, second]
        for time in times:
            if difference >= time[0]:
                time_ago = int(difference / time[0])
                if time_ago <= 1:
                    timeframe = time[1].rstrip('s')
                else:
                    timeframe = time[1]

                time_item = str(time_ago) + ' ' + timeframe
                return time_item
        return 'Date Error'
