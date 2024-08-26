import sys
import traceback

class Custom_Exception():
    def custom_exception(self,err,sys):
        _,_,exc_traceback = sys.exc_info()
        last_stack = traceback.extract_tb(exc_traceback)
        file_name = last_stack[-1].filename
        print("An exception has occured in file {0}, at line {1}, with the error message {2}".format(file_name,exc_traceback.tb_lineno,str(err)))


## Test code to see if the exceptions.py files is being executed correctly
# if __name__ == "__main__":
#     try:
#         print(1/0)
#     except Exception as e:
#         exc = Custom_Exception()
#         print(exc.custom_exception(sys,e))
