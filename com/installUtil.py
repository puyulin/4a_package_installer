from tkinter import *
from com.cn.VersionBean import VersionBean
from com.cn.InstallFrame import InstallFrame
tk = Tk()
tk.title("自动化创建4A安装包")
versionBean = VersionBean()
installFrame = InstallFrame(versionBean)
#Foua_WEB
webLineFrame = Frame();
installFrame.fouraFileLine(webLineFrame,textStr="4A_WEB")
webLineFrame.pack(side="top")

#ScheduleServer
webLineFrame = Frame();
installFrame.fouraFileLine(webLineFrame,textStr="ScheduleServer")
webLineFrame.pack(side="top")

#AuditData
webLineFrame = Frame();
installFrame.fouraFileLine(webLineFrame,textStr="AuthServer")
webLineFrame.pack(side="top")

#打包路径
packageFrame = Frame();
installFrame.fouraFileLine(packageFrame,textStr="installPackage")
packageFrame.pack(side="top")


versionLineFrame = Frame();
installFrame.versionLine(versionLineFrame,textStr="版本号")
versionLineFrame.pack(side="top")


commitFrame = Frame();
installFrame.commitBtn(commitFrame)
commitFrame.pack(side="top")

tk.mainloop()

