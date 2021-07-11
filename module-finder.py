# Determines whether a module exists within the python version
# The script returns a Boolean value 
# If module exists within that specific python version, it returns True
# otherwise, it returns False

import sys

if sys.version_info <= (3,0): 
   print("Python version os" + str(sys.version_info))
   try:
       import imp
       imp.find_module('requests')
       found = True
       print(found)
   except:
       found = False
       print(found)
else:
    import importlib
    request_found = importlib.util.find_spec('requests')
    found = request_found is not None
    print(found)
