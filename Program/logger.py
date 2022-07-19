import logging
class log:
    def __init__(self):
        # Create a custom logger
        self.logger = logging.getLogger('Database')
        self.logger.setLevel(logging.DEBUG)
        # Create a handler
        self.handler = logging.FileHandler('program_log.log')
        self.handler.setLevel(logging.DEBUG)
        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s- %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        # Add the handlers to the logger
        self.logger.addHandler(self.handler)
        #create socond logger for the program
        self.logger2 = logging.getLogger('Webscraper')
        self.logger2.setLevel(logging.DEBUG)
        # Create a handler
        self.handler2 = logging.FileHandler('program_log.log')
        self.handler2.setLevel(logging.DEBUG)
        # Create a logging format
        formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler2.setFormatter(formatter2)
        # Add the handlers to the logger
        self.logger2.addHandler(self.handler2)


    def info(self,message):
        self.logger.info(message)
    def error(self,message):
        self.logger.error(message)
    def debug(self,message):
        self.logger.debug(message)
    def warning(self,message):
        self.logger.warning(message)
    def critical(self,message):
        self.logger.critical(message)
    def fatal(self,message):
        self.logger.fatal(message)
    def info2(self,message):
        self.logger2.info(message)
    def rror2(self,message):
        self.logger2.error(message)
    def debug2(self,message):
        self.logger2.debug(message)
    def warning2(self,message):
        self.logger2.warning(message)
    def critical2(self,message):
        self.logger2.critical(message)
    def fatal2(self,message):
        self.logger2.fatal(message)
