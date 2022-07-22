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
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
        #create third logger for the general program
        self.logger3 = logging.getLogger('General')
        self.logger3.setLevel(logging.DEBUG)
        # Create a handler
        self.handler3 = logging.FileHandler('program_log.log')
        self.handler3.setLevel(logging.DEBUG)
        # Create a logging format
        formatter3 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler3.setFormatter(formatter3)
        # Add the handlers to the logger
        self.logger3.addHandler(self.handler3)



    def info_database(self,message):
        self.logger.info(message)
    def error_database(self,message):
        self.logger.error(message)
    def debug_database(self,message):
        self.logger.debug(message)
    def warning_database(self,message):
        self.logger.warning(message)
    def critical_database(self,message):
        self.logger.critical(message)
    def fatal_database(self,message):
        self.logger.fatal(message)
    def info_webscraper(self,message):
        self.logger2.info(message)
    def error_webscraper(self,message):
        self.logger2.error(message)
    def debug_webscraper(self,message):
        self.logger2.debug(message)
    def warning_webscraper(self,message):
        self.logger2.warning(message)
    def critical_webscraper(self,message):
        self.logger2.critical(message)
    def fatal_webscraper(self,message):
        self.logger2.fatal(message)
    def info_general(self,message):
        self.logger3.info(message)
    def error_general(self,message):
        self.logger3.error(message)
    def debug_general(self,message):
        self.logger3.debug(message)
    def warning_general(self,message):
        self.logger3.warning(message)
    def critical_general(self,message):
        self.logger3.critical(message)
    def fatal_general(self,message):
        self.logger3.fatal(message)


