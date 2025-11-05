# Lower than debug which is 10
TRACE = 5
class MyLogger(logging.Logger):
    def trace(self, msg, *args, **kwargs):
        self.log(TRACE, msg, *args, **kwargs)
