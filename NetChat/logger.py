class Logger:
    Instance = None
    
    def __new__(cls, log_level, stdout=True, file=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            cls.instance.__init__(log_level, stdout, file)
        return cls.instance
    
    def __init__(self, log_level, stdout=True, file=None):
        self.log_level = log_level
        self.stdout = stdout
        self.file = file
        Logger.Instance = self

log = Logger(Logger.DEBUG)
