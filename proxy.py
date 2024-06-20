"""
Author  : chuiting.kong
Date    : 2024.05.10
Usage   : run scripts
"""
import os.path
import sys
import importlib
import traceback

logFile=os.path.abspath(os.path.join(os.path.dirname(__file__),'scripts.log'))
sys.path.insert(0,sys.argv[1])
return_value={}
try:
    module_name = importlib.import_module(sys.argv[2])
    func_name = getattr(module_name, sys.argv[3])
    dic = eval(sys.argv[4])
    return_value = func_name(dic)
except Exception as reason:
    print(f"Call script {sys.argv[2]} error!\n")
    with open(logFile,'a',encoding='utf-8') as f:
        traceback.print_exc(file=f)
        f.write('\n')
    exit(-1)

print("%s"% (sys.argv[5]), end = '')
for key, value in return_value.items():
    print("%s" % key, end ='')
    print("%s"% (sys.argv[5]), end = '')
    print("%s" % value, end ='')
    print("%s"% (sys.argv[5]), end = '')