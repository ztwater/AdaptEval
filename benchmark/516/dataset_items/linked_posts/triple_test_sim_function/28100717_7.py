todays_file = directory / str(datetime.datetime.utcnow().date())
if todays_file.exists():
    logger.info("todays_file exists: " + str(todays_file))
    df = pd.read_json(str(todays_file))
