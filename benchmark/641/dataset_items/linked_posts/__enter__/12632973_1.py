class FileHolder(object):                                                                                                                 
    def __init__(self,*args,**kwargs):
        self.f= file(*args,**kwargs)

    def __enter__(self,*args,**kwargs):
        return self.f.__enter__(*args,**kwargs)

    def __exit__(self,*args,**kwargs):
        self.f.__exit__(*args,**kwargs)

    def __getattr__(self,item):
        return getattr(self.f,item)
