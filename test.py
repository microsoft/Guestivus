import sys
sys.path.append('C:\Github\Guestivus')

import importlib

from GuestivusLib import GuestivusLib
importlib.reload(GuestivusLib)

gc = GuestivusLib.gitConnection("https://github.com/microsoft/Guestivus", "C:\Github\Guestivus")
#gc = GuestivusLib.gitConnection("github.com/microsoft/Guestivus")
envPaths = gc.getEnvPaths()
for p in envPaths:
    print(p)

print("isGitInstalledWin:")
print(gc.isGitInstalledWin())
print(gc.gitVersion)


print("isLFSInstalledWin:")
print(gc.isLFSInstalledWin())
print(gc.lfsVersion)


print("localRootValid:")
print(gc.localRootValid())

print("localRootExists:")
print(gc.localRootExists())

print("localRootIsRepo:")
print(gc.localRootIsRepo())