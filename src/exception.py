
# The purpose of the code is to be handling exceptions and providing detailed error messages with file names and line numbers when
#  something goes wrong in the Python script.




# import sys
# import logging

# def error_message_detail(error, error_details:sys):
#     _ , _ , exc_tb = error_details.exc_info()
#     error_message = f'Error occures in python script name [(0)] line number [(1)] error message[(2)]".format()'
#     filename    = exc_tb.tb_frame.f_code.co_filename
#     filename, exc_tb.tb_lineno, str(error) 
   
#     return error_message
    
# class CustomException(Exception):
#     def __init__(self, error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message = error_message_detail(error_message, error_detail=error_detail)

#     def __str__(self):
#         return self.error_message
    


# if __name__=="__main__":


#     try:
#         a = 1/0

#     except Exception as e:
#         logging.info("Dividing by Zero")   
#         raise CustomException(e, sys)

         




import sys

def error_message_detail(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    error_message = f'Error occurs in python script name {exc_tb.tb_frame.f_code.co_filename} line number {exc_tb.tb_lineno} error message: {error}'
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

try:
    a = 1 / 0
except ZeroDivisionError as e:
    raise CustomException(e, sys)
