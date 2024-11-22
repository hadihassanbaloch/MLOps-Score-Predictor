import sys
from scorePrediction.logger import logging

class CustomException(Exception):
    def __init__(self, error_message):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        
        self.error_message = f"Error Occured in [{file_name}] at line {line_number}: {error_message}"
        logging.error(self.error_message)
        
    def __str__(self):
        return self.error_message