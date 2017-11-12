from tkinter import *
from tkinter import filedialog
from com.cn.FilePackageInstall import FilePackageInstall
class InstallFrame(object):

    def __init__(self,object):
        self.versionBean = object

    def fouraFileLine(self,frame,textStr):

        webLabel = Label(frame,text=textStr,anchor="e",width=14,height=4)
        webLabel.pack(side=LEFT)

        # 空行分割
        spaceLabel = Label(frame, text="  ", width=2)
        spaceLabel.pack(side=LEFT)

        eText = StringVar()
        webInput = Entry(frame,state="readonly",textvariable=eText,width=40)
        webInput.pack(side=LEFT)

        # 空行分割
        spaceLabel = Label(frame,text="  ",width=2)
        spaceLabel.pack(side=LEFT)

        btnFile = Button(frame,text="选择...",command=lambda : self.selectDialog(eText,textStr))
        btnFile.pack(side=LEFT)

        #空行分割
        spaceLabel = Label(frame, text="  ", width=2)
        spaceLabel.pack(side=LEFT)
        return None

    #设置各个组件的安装包位置
    def selectDialog(self,eText,textStr):
        if textStr == "installPackage":
            filename = filedialog.askdirectory(title='打开文件夹')
            pass
        else:
            filename = filedialog.askopenfilename(title='打开文件', filetypes=[('tar', '*.tar *.tar.gz'), ('All Files', '*')])
        print(filename)
        eText.set(filename)
        if textStr=="4A_WEB":
            self.versionBean.setWebPath(filename)
            pass
        elif textStr == "ScheduleServer":
            self.versionBean.setScheduleServerPath(filename)
            pass
        elif textStr == "AuthServer":
            self.versionBean.setAuthServerPath(filename)
            pass
        elif textStr == "installPackage":
            self.versionBean.setPackagePath(filename)




    def versionLine(self,frame,textStr):
        webLabel = Label(frame, text=textStr, anchor="e", width=14, height=4)
        webLabel.pack(side=LEFT)
        # 空行分割
        spaceLabel = Label(frame, text="  ", width=2)
        spaceLabel.pack(side=LEFT)

        versionInput = Entry(frame,width=40)
        versionInput.pack(side=LEFT)

        # 空行分割
        spaceLabel = Label(frame, text="   ", width=12)
        spaceLabel.pack(side=LEFT)

        self.versionInput = versionInput
        pass

    #获取填入的版本号
    def getVersion(self):
        version = self.versionInput.get()
        self.versionBean.setVersion(version)
        print("版本号",version)
        #########################开始处理安装包程序#########################
        packageInstall = FilePackageInstall(self.versionBean)
        packageInstall.installStart()

    def commitBtn(self,frame):
        commitBtn = Button(frame,text="开始制作发布包",command=self.getVersion)
        commitBtn.pack(side=TOP)



