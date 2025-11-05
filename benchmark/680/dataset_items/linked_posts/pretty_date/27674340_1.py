>>> _ = humanize.i18n.activate('ru_RU')
>>> print humanize.naturaltime(datetime.now() - timedelta(days=1))
день назад
>>> print humanize.naturaltime(datetime.now() - timedelta(hours=2))
2 часа назад
