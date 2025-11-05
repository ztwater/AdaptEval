import logging
from datetime import datetime
c_now=datetime.now()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] :: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("../logs/log_file_{}-{}-{}-{}.log".format(c_now.year,c_now.month,c_now.day,c_now.hour))
    ]
)
DEBUG_LEVELV_NUM = 99 
logging.addLevelName(DEBUG_LEVELV_NUM, "CUSTOM")
def custom_level(message, *args, **kws):
    logging.Logger._log(logging.root,DEBUG_LEVELV_NUM, message, args, **kws) 
logging.custom_level = custom_level
# --- --- --- --- 
logging.custom_level("Waka")
