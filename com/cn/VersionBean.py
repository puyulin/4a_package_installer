class VersionBean(object):

    def __init__(self):
        self.webPath=""
        self.version = ""
        self.authPath=""
        self.schedulePath=""
        self.packagePath=""
        pass

    def setWebPath(self,webPath):
        self.webPath = webPath
        pass

    def getWebPath(self):
        return self.webPath

    def setScheduleServerPath(self,schedulePath):
        self.schedulePath = schedulePath
        pass

    def getScheduleServerPath(self):
        return self.schedulePath

    def setAuthServerPath(self,authPath):
        self.authPath = authPath
        pass

    def getAuthServerPath(self):
        return self.authPath

    def setPackagePath(self,packagePath):
        self.packagePath=packagePath
        pass

    def getPackagePath(self):
        return self.packagePath

    def setVersion(self,version):
        self.version = version
        pass
    def getVersion(self):
        return self.version