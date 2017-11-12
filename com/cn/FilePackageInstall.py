import os
import shutil
class FilePackageInstall(object):

    def __init__(self,versionBean):
        self.versionBean = versionBean
        self.installNormal = str(self.versionBean.getPackagePath())+"/"+"installer_normal"
        self.installOld = str(self.versionBean.getPackagePath())+"/"+"installer"
        self.installPackage = versionBean.getPackagePath()

    def installStart(self):
        print("WEB 安装包路径:",self.versionBean.getWebPath())
        print("ScheduleServer 安装包路径",self.versionBean.getScheduleServerPath())
        print("AuthServer 安装包路径",self.versionBean.getAuthServerPath())
        print("安装包installer输出路径",self.versionBean.getPackagePath())
        self.removeOlds()
        self.addNewFiles()
        pass

    def addNewFiles(self):
        self.copyFile(self.installNormal,"platform","FourA3.0.4.2",self.versionBean.getWebPath())
        self.copyFile(self.installOld, "platform", "FourA3.0.4.2",self.versionBean.getWebPath())

        self.copyFile(self.installNormal, "components" + "/" + "scheduleserver", "ScheduleServer3.0.4.2",self.versionBean.getScheduleServerPath())
        self.copyFile(self.installOld, "components" + "/" + "scheduleserver", "ScheduleServer3.0.4.2",self.versionBean.getScheduleServerPath())

        self.copyFile(self.installNormal, "components" + "/" + "authserver", "AuthServer3.0.4.2",self.versionBean.getAuthServerPath())
        self.copyFile(self.installOld, "components" + "/" + "authserver", "AuthServer3.0.4.2",self.versionBean.getAuthServerPath())

        # 删除AuditData
        self.copyFile(self.installNormal, "components" + "/" + "auditdata", "AuditData3.0.4.2",self.versionBean.getAuthServerPath())
        self.copyFile(self.installOld, "components" + "/" + "auditdata", "AuditData3.0.4.2",self.versionBean.getAuthServerPath())
        pass


    def copyFile(self,installPath,module,indexStr,filePath):
        #installer_normal/platform/FourA3.0.4.2.version.tar.gz
        dst = installPath+"/"+module+"/"+indexStr+"."+self.versionBean.getVersion()+ os.path.splitext(filePath)[1]
        print("copy src :",filePath,"to",dst,"doing...")
        shutil.copyfile(filePath,dst)
        print("copy src :", filePath, "to", dst, "end...")
        pass


    #删除匹配的指定文件
    def removeOldFile(self,installPath,module,indexStr):
        webDirPath = installPath+"/"+module
        childrenPath = os.listdir(webDirPath)
        for line in childrenPath:
            try:
                if line.index(indexStr)>-1:
                    filePath = os.path.join(webDirPath, line)
                    try:
                        print("remove file as",filePath)
                        os.remove(filePath)
                        print("======","remove file ",filePath)
                        pass
                    except Exception as ep:
                        print(ep)
                        pass
                else:
                    pass
                pass
            except Exception as e:
                pass
            pass



    def removeOlds(self):
        #删除WEB
        self.removeOldFile(self.installNormal,"platform","FourA3.0.4.2")
        self.removeOldFile(self.installOld,"platform", "FourA3.0.4.2")

        #删除ScheduleServer
        self.removeOldFile(self.installNormal,"components"+"/"+"scheduleserver","ScheduleServer3.0.4.2")
        self.removeOldFile(self.installOld, "components"+"\\"+"scheduleserver","ScheduleServer3.0.4.2")

        #删除AuthServer
        self.removeOldFile(self.installNormal,"components"+"/"+"authserver","AuthServer3.0.4.2")
        self.removeOldFile(self.installOld,"components"+"/"+"authserver","AuthServer3.0.4.2")

        #删除AuditData
        self.removeOldFile(self.installNormal,"components"+"/"+"auditdata","AuditData3.0.4.2")
        self.removeOldFile(self.installOld,"components"+"/"+"auditdata","AuditData3.0.4.2")
        pass