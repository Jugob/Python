#! /usr/bin/env python3

def forced_param(*, arg1="value1", arg2="value2", arg3="value3"):
    print("arg1={}, arg2={}, arg3={}".format(arg1, arg2, arg3))
    return True

#calling the function without using keyword parameters.
#forced_param("V1","V2","V3")

#calling the function using the keyword parameters
forced_param(arg1="V1",arg2="V2",arg3="V3")

