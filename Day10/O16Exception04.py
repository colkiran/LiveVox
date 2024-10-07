"""
traceback
type error
message

interpreter  will call sys.execepthook() with three arguments
  a. the exception class  - TypeError
  b. exception value   - Unsuppported opperands.....
  c. traceback object - traceback
"""
import sys

def format_traceback(exc_type, exc_val, exc_traceback):
    print("Something went wrong......")
    print(exc_type)
    print(exc_val)
    print(list(exc_traceback))
    # print(list(sys.excepthook))

sys.excepthook = format_traceback

def fun():
    print(1 + "hello")


fun()
