# Guestivus: The Git client for the rest of us!
# MIT License
# Copyright (c) Microsoft Corporation. All rights reserved.
# See https://github.com/microsoft/Guestivus/blob/master/LICENSE for license details.

# This is the library that contains the functional layer and Git integration.
# This library is used by the Guestivus front end as well as other front ends such as DCCs

import subprocess
import os
import socket

class errors:
    # Local system installations
    gitNotInstalled = "Git does not appear to be installed on the local computer."
    lfsNotInstalled = "Git LFS does not appear to be installed on the local computer."
    wrongLfsVersion = "Incorrect version of Git LFS installed.  Guestivus needs v2 or higher."
    
    # Remote server access
    cantAccessRemoteGitRepo = "Can't connect to the remote Git repo."
    cantAccessLFSServer = "Can't access the Repo's LFS server."

    # Local paths
    localPathNotSet = "The local path variable on this object is empty"
    localPathNotExist = "The local path does not exists."
    localPathNotGitRepo = "The local path is not a Git Repository"

class gitStatus:
    def __init__(self):
        pass


class gitConnection:
    # =============================== CONSTRUCTOR ===================================
    def __init__(self, serverUrl, localRoot):
        self.serverUrl = serverUrl
        self.localRoot = localRoot
        self.gitVersion = ""
        self.lfsVersion = ""
        self.error = ""
        self.useStatusCache = True
        self.status = gitStatus()


    # =============================== METHODS ===================================
    def getEnvPaths(self):
        return(os.environ["PATH"].split(";"))
 

    def execGit(self, args):
        self.error = ""
        if (self.localRoot != ""):
            # Local path ok
            if not isinstance(args, list): # Check if args is list or single
                args = [args]

            return(subprocess.run(["git"] + args, cwd=self.localRoot, shell=True, text=True, capture_output=True))
        else:
            self.error = errors.localPathNotSet
            return(None)


    def isGitInstalledWin(self):
        self.error = ""
        procComp =  self.execGit("--version")
        if(procComp.stdout.startswith("git")):
            # Extract version
            self.gitVersion = procComp.stdout.split(" ")[2]
            return(True) # Git installed

        self.error = errors.gitNotInstalled
        return(False) # Git not installed


    def isLFSInstalledWin(self):
        self.error = ""
        procComp =  self.execGit(["lfs", "--version"])
        if(procComp.stdout.startswith("git-lfs")):
            # Extract version
            slashSplitParts = procComp.stdout.split("/")
            self.lfsVersion = slashSplitParts[1].split(" ")[0]
            return(True) # Git lfs installed

        self.error = errors.lfsNotInstalled
        return(False) # Git lfs not installed
    

    def pingRemoteGitHost(self, url, port):
        procComp =  self.execGit("ls-remote")


    def localRepoSupportLFS(self):
        pass


    def localRootValid(self):
        self.error = ""
        rootValid = self.localRoot or not (self.localRoot.isspace())

        if(not rootValid):
            self.error = errors.localPathNotSet
            return(False)

        return(True)
        

    def localRootExists(self):
        self.error = ""
        # Check if root is valid
        if not self.localRootValid():
            return(False)
        
        # Check if root exists
        if(not os.path.exists(self.localRoot)):
            self.error = errors.localPathNotExist
            return(False)

        return(True)
        

    def localRootIsRepo(self):
        if(not self.localRootExists()):
            return(False)

        self.error = ""
        procComp =  self.execGit("branch")
        if(procComp.stdout.startswith("fatal:")):
            self.error = errors.localPathNotGitRepo
            return(False)

        return(True)


    def checkRequirements(self):
        self.error = ""
        
        # is Git installed?
        if(not isGitInstalledWin()):
            return(False)

        # Is LFS installed?
        if(not isLFSInstalledWin()):
            return(False)

         # Do we have the correct version of LFS?
        if(self.lfsVersion.startswith("1") == True):
            self.error = errors.wrongLfsVersion
            return(False)