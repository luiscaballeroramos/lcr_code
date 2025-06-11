import os
import sys

# search for OneDrive/01_Python folder in user home directory
# C:\Users\myUser\OneDrive\01_Python
base = os.path.expanduser("~")  # C:\Users\myUser
oneDrivePath = os.path.join(base, "OneDrive")
# check if onedrive is a directory
if not os.path.isdir(oneDrivePath):
    raise ValueError("onedrive (" + oneDrivePath + ") must be valid folder path")
if oneDrivePath:
    pythonFolder = os.path.join(oneDrivePath, "01_Python")
    if not os.path.isdir(pythonFolder):
        raise ValueError("folder '01_Python' doesn't exist in OneDrive folder")

# default settings
mode = "Developer"  # "User" or "Developer"
serverPath = pythonFolder
managementPath = os.path.join(serverPath, "management")
codeDefault = "code"
codeDefaultPath = os.path.join(serverPath, codeDefault)
toolDefault = "tool"
toolDefaultPath = os.path.join(serverPath, toolDefault)
codeDevDefault = "codedev"
codeDevDefaultPath = os.path.join(serverPath, codeDevDefault)
toolDevDefault = "tooldev"
toolDevDefaultPath = os.path.join(serverPath, toolDevDefault)
codePath = None
toolPath = None
if not os.path.isdir(serverPath):
    raise ValueError("serverPath (" + serverPath + ") doesn´t exist")
else:
    # add serverPath to sys if it isn't in sys
    if serverPath not in sys.path:
        sys.path.append(serverPath)
# serverPath, codePath, toolPath
if mode == "User":
    codePath = codeDefault
    toolPath = toolDefault
if mode == "Developer":
    codePath = codeDevDefaultPath
    toolPath = toolDevDefaultPath
# append codePath to sys path actual path
if codePath not in sys.path:
    sys.path.append(codePath)
# append toolPath to sys path actual path
if toolPath not in sys.path:
    sys.path.append(toolPath)
