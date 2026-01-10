import sys

class Level:
    INFO = 0
    ERROR = 1

class Logger:
    def __init__(self, logs_enabled: bool):
        self.logs_enabled = logs_enabled

    def log(self, level: Level, message: str):
        if self.logs_enabled:
            match level:
                case Level.INFO:
                    print(message)
                case Level.ERROR:
                    print(message, file=sys.stderr)