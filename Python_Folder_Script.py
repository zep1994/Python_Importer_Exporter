# ************************************************************
# *** Script Name:   Py_Script
# *** Parameters:    Does folder exist
# *** Output:        Y
# *** Written By:    Thomas Matlock, Ergon, Inc., May 2022
# *** Modified By:   Thomas Matlock, Ergon, Inc.
# *** Version:       1.1.1
# ************************************************************

#import Modules
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]

print(onlyfiles)