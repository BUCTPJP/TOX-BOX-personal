import os
import sys
import time
import math
import win32ui
import pyzbar
import qrcode
import ctypes
import webbrowser
import tkinter as tk
from tkinter.filedialog import askdirectory
import numpy as np
from MyQR import myqr
import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance,ImageTk
from tkinter import END, INSERT, RAISED, SUNKEN,filedialog,DISABLED, messagebox
from PIL.ImageFilter import EMBOSS, CONTOUR,BLUR,DETAIL,EDGE_ENHANCE,FIND_EDGES,SMOOTH,SHARPEN

from Ui_common import Ui_MainWindow as Ui_MainWindow1
from Ui_Qrcode_make import Ui_MainWindow as Ui_MainWindow1_4
from Ui_QRcode_analyzing import Ui_MainWindow as Ui_MainWindow1_5

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import  QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow

window = tk.Tk()
width = 356
heigh = 200
ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
window.tk.call('tk', 'scaling', ScaleFactor/75)                             #设置程序缩放
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
window.title('小工具盒')                                                     #窗口标题
window.iconbitmap('res/img/main.ico')
window.configure(bg = 'white')                                         #窗口背景

def tip(self):#使用提示
    tk.messagebox.showinfo(title="提示",message="请利用上方菜单栏\n选择所需要的功能")

def common():#日常功能界面
    class MyWindow(QMainWindow,Ui_MainWindow1):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(BMI)
            self.pushButton_2.clicked.connect(temp_transform)
            self.pushButton_3.clicked.connect(outbreak_query)
            self.pushButton_4.clicked.connect(QRcode_make)
            self.pushButton_5.clicked.connect(QRcode_analyzing)
            self.pushButton_6.clicked.connect(picture_torrent)
            self.pushButton_7.clicked.connect(word_frequency_en)
            self.pushButton_8.clicked.connect(Bvideo_download)
    app = QApplication(sys.argv)
    myWindow1 = MyWindow()               #实例化
    myWindow1.show()
    app.exec_()
    myWindow1.close()
    
def BMI():#BMI指数计算
    W1_1 = tk.Toplevel()
    width = 350
    heigh = 200
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W1_1 .tk.call('tk', 'scaling', ScaleFactor/75)                                 #设置程序缩放
    screenwidth = W1_1.winfo_screenwidth()
    screenheight = W1_1.winfo_screenheight()
    W1_1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W1_1.title('BMI指数计算')                                                      #窗口标题
    W1_1.configure(bg = 'aquamarine')                                             #窗口背景

    def make():
        height = eval(e1.get())
        weight = eval(e2.get())
        BMI = weight / pow(height,2)
        a = 'BMI:{:.2f}'.format(BMI)
        if BMI < 18.5:
            INT,DOM = '偏瘦','偏瘦'
        elif 18.5 <= BMI <24:
            INT,DOM = '正常','正常'
        elif 24 <= BMI < 25:
            INT,DOM = '正常','偏胖'
        elif 25 <= BMI < 28:
            INT,DOM = '偏胖','偏胖'
        elif 28 <= BMI < 30:
            INT,DOM = '偏胖','肥胖'
        else:
            INT,DOM = '肥胖','肥胖'
        b = "指标:国际'{0}'，国内'{1}'".format(INT,DOM)
        showarea.config(state='normal')
        showarea.delete('1.0','end')
        showarea.insert(INSERT,a)
        showarea.insert(INSERT,'\n')
        showarea.insert(END,b)
        showarea.config(state='disable')

    showarea = tk.Text(W1_1,bg = 'palegreen',font = ('隶书',12),width = 30,height = 2,exportselection = True,relief = RAISED,state = 'disable')
    tip1 = tk.Label(W1_1,bg='aquamarine',text='身高：',font = ('楷体',12))
    e1 = tk.Entry(W1_1,cursor = 'xterm',relief = SUNKEN)
    m = tk.Label(W1_1,bg='aquamarine',text='米',font = ('楷体',12))
    tip2 = tk.Label(W1_1,bg='aquamarine',text='体重：',font = ('楷体',12))
    e2 = tk.Entry(W1_1,cursor = 'xterm',relief = SUNKEN)
    kg = tk.Label(W1_1,bg='aquamarine',text='千克',font = ('楷体',12))
    button = tk.Button(W1_1,bg='honeydew',text='计\n算',command = make,relief = RAISED,font=('隶书',14))
    tip1.place(relx = 0.01,rely = 0.1)
    e1.place(relx = 0.2,rely = 0.1)
    m.place(relx = 0.65,rely = 0.1)
    tip2.place(relx = 0.01,rely = 0.4)
    e2.place(relx = 0.2,rely = 0.4)
    kg.place(relx = 0.65,rely = 0.4)
    button.place(relx = 0.82,rely = 0.15)
    showarea.place(relx=0.05,rely=0.6)
    e1.focus_set()
def temp_transform():#温度转换
        W1_2 = tk.Toplevel()
        width = 350
        heigh = 200
        ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
        ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
        W1_2.tk.call('tk', 'scaling', ScaleFactor/75)                                 #设置程序缩放
        screenwidth = W1_2.winfo_screenwidth()
        screenheight = W1_2.winfo_screenheight()
        W1_2.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
        W1_2.title('温度转换')                                                        #窗口标题
        W1_2.configure(bg = 'aquamarine')                                             #窗口背景

        def make():
            TempStr = e1.get()
            if TempStr[-1] in ['F','f']:
                C=(eval(TempStr[0:-1])-32)/1.8
                c = "  转换后的温度是：{:.2f}C".format(C)
            elif TempStr[-1] in ['C','c']:
                F=1.8*eval(TempStr[0:-1])+32
                c = "  转换后的温度是：{:.2f}F".format(F)
            else:
                c = "  输入格式有误"
            showarea.config(state='normal')
            showarea.delete('1.0','end')
            showarea.insert(INSERT,c)
            showarea.config(state='disable')

        showarea = tk.Text(W1_2,bg = 'palegreen',font = ('隶书',12),width = 30,height = 2,exportselection = True,relief = RAISED,state = 'disable')
        tip1 = tk.Label(W1_2,bg='linen',text='  请输入带有符号的温度值：',font = ('楷体',12))
        e1 = tk.Entry(W1_2,cursor = 'xterm',relief = SUNKEN)
        tip2 = tk.Label(W1_2,bg='linen',text='摄氏:c/C 华氏:f/F',font = ('楷体',12))
        button = tk.Button(W1_2,bg='honeydew',text='计\n算',command = make,relief = RAISED,font=('隶书',14))
        tip1.place(relx = 0.01,rely = 0.1)
        e1.place(relx = 0.01,rely = 0.25)
        tip2.place(relx = 0.01,rely = 0.4)
        button.place(relx = 0.82,rely = 0.15)
        showarea.place(relx=0.05,rely=0.7)
        e1.focus_set()
def outbreak_query():#疫情查询
        W1_3 = tk.Toplevel()
        width = 350
        heigh = 100
        ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
        ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
        W1_3.tk.call('tk', 'scaling', ScaleFactor/75)                                 #设置程序缩放
        screenwidth = W1_3.winfo_screenwidth()
        screenheight = W1_3.winfo_screenheight()
        W1_3.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
        W1_3.title('疫情查询')                                                        #窗口标题
        W1_3.configure(bg = 'aquamarine')                                             #窗口背景

        def make_1():
            webbrowser.open('http://bmfw.www.gov.cn/yqfxdjcx/risk.html',new=0)
        def make_2():
            webbrowser.open('http://www.gov.cn/zhuanti/2021yqfkgdzc/index.htm#/',new=0)
        
        button1 = tk.Button(W1_3,bg='honeydew',text='风险等级\n查询',command = make_1,relief = RAISED,font=('隶书',14))
        button2 = tk.Button(W1_3,bg='honeydew',text='出入政策\n查询',command = make_2,relief = RAISED,font=('隶书',14))
        button1.place(relx = 0.58,rely = 0.1)
        button2.place(relx = 0.05,rely = 0.1)
def QRcode_make():#二维码生成
    def produce():#直接生成
        start = time.time()                                         #开始计时
        string = myWindow.textEdit.toPlainText()                 #获取用户输入内容
        saved = myWindow.lineEdit_2.text()
        color = myWindow.lineEdit.text()                          #获取用户输入内容
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)                                           #使用make方法生成
        img = qr.make_image() 
        img = qr.make_image(fill_color=color, back_color='#FFF')  # 得到二维码对象，并可以通过修改fill_color、back_color参数来调整小格子颜色和背景色
        img.save(saved)                                             #保存二维码
        end = time.time()                                           #结束计时
        a = end - start
        runtime = "生成用时：{:.2f}s".format(a)                      
        myWindow.label_4.clear()
        myWindow.label_4.setText("\n")
        myWindow.label_4.setText(runtime)                             #显示二维码生成用时
        time.sleep(1)
        Image.open(saved).show()
    def logo():#带logo
        string = myWindow.textEdit.toPlainText()                 #获取用户输入内容
        saved = myWindow.lineEdit_2.text()
        color = myWindow.lineEdit.text()                          #获取用户输入内容
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)
        img = qr.make_image() 
        img = qr.make_image(fill_color=color, back_color='#FFF')  # 得到二维码对象，并可以通过修改fill_color、back_color参数来调整小格子颜色和背景色
    
        dlg = win32ui.CreateFileDialog(1)   #选择文件
        dlg.DoModal()
        filename = dlg.GetPathName()
        image = str(filename).replace('\\','\\\\')
        start = time.time()
        icon = Image.open(image).convert('RGBA')                   #转换为RGBA4通道
        img_w, img_h = img.size                                    #获得二维码尺寸
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        icon_w, icon_h = icon.size
        if icon_w > size_w:                                        #调整logo图片大小
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h),Image.Resampling.LANCZOS)
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        img.paste(icon, (w, h), icon)                              #将logo图片贴在二维码指定位置
        img = img.convert('RGB')
        img.save(saved)                                            #保存

        end = time.time()
        a = end - start
        runtime = "生成用时：{:.2f}s".format(a)
        myWindow.label_4.clear()
        myWindow.label_4.setText("\n")
        myWindow.label_4.setText(runtime)                             #显示二维码生成用时
        time.sleep(1)
        Image.open(saved).show()
    def bg():#带背景
        content =  myWindow.textEdit.toPlainText()
        saved = myWindow.lineEdit_2.text()
        dlg = win32ui.CreateFileDialog(1)   #选择文件
        dlg.DoModal()
        filename = dlg.GetPathName()
        start = time.time()
        img = str(filename).replace('\\','\\\\')
        print(img)
        myqr.run(
            words=content,                             # 扫描二维码后，显示的内容，或是跳转的链接
            version=10,                                 # 设置容错率
            level='H',                                 # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
            picture=img,                               # 图片所在目录，可以是动图
            colorized=True,                            # 黑白(False)还是彩色(True)
            contrast=1.0,                              # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
            brightness=1.0,                            # 用来调节图片的亮度，用法同上。
            save_name=saved,                           # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
        )

        end = time.time()
        a = end - start
        runtime = "生成用时：{:.2f}s".format(a)
        myWindow.label_4.clear()
        myWindow.label_4.setText("\n")
        myWindow.label_4.setText(runtime)                             #显示二维码生成用时
        time.sleep(1)
        Image.open(saved).show()
    def help1_4():#使用帮助
        os.system(r'notepad ./使用说明/二维码生成使用说明.txt')
    class MyWindow(QMainWindow,Ui_MainWindow1_4):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(produce)
            self.pushButton_2.clicked.connect(logo)
            self.pushButton_3.clicked.connect(bg)
            self.pushButton_4.clicked.connect(help1_4)
    app = QApplication(sys.argv)
    myWindow = MyWindow()               #实例化
    myWindow.show()
    app.exec_()
    myWindow.close()
def QRcode_analyzing():#解析二维码
    def choose():
        dlg = win32ui.CreateFileDialog(1)   #选择文件
        dlg.DoModal()
        filename = dlg.GetPathName()
        image = str(filename).replace('\\','\\\\')
        start = time.time()                                         #运行计时 
        img = Image.open(image)
        #处理图片
        img = ImageEnhance.Sharpness(img).enhance(1.0)              #锐利化          0~1~2
        img = img.filter(SMOOTH)                                   #SMOOTH：突出图像的宽大区域、低频成分和主干部分，或抑制图像噪声和高频成分，使图像亮度平缓渐变，减小突变梯度，改善图像质量
        img = img.filter(SHARPEN)                                   #SHARPEN：补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰
        texts = pyzbar.decode(img)                                  #解析到信息
        print(texts)                                                #data-内容；type-类型；rect-尺寸;polygon-边角定位点；quality-质量；orientation-方向
        if texts == []:
            result = '此图片不包含二维码,请重试或更换'
        else:                                              
            for text in texts:                                      #查找输出结果
                content = text.data.decode("utf-8")                                         
                result = "二维码中的内容是:\n{:\0^39}".format(content)
        end = time.time()
        
        runtime = end - start
        runtime = "解析用时:{:.2f}s".format(runtime)                #解析内容格式化
        myWindow.label_2.clear()
        myWindow.label_2.setText("\n")
        myWindow.label_2.setText(runtime)                             #显示二维码生成用时
        myWindow.label.clear()
        myWindow.label.setText("\n")
        myWindow.label.setText(result)                             #显示二维码生成用时
    class MyWindow(QMainWindow,Ui_MainWindow1_5):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(choose)
    app = QApplication(sys.argv)
    myWindow = MyWindow()               #实例化
    myWindow.show()
    app.exec_()
    myWindow.close()
def picture_torrent():#图种制作
    W1_6 = tk.Toplevel()
    width = 350
    heigh = 200
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W1_6 .tk.call('tk', 'scaling', ScaleFactor/75)                              #设置程序缩放
    screenwidth = W1_6.winfo_screenwidth()
    screenheight = W1_6.winfo_screenheight()
    W1_6.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W1_6.title('图种制作')                                                        #窗口标题
    W1_6.configure(bg = 'aquamarine')                                             #窗口背景
    W1_6.iconbitmap('img/picture_torrent.ico')

    def select1():
        explore = tk.Tk()
        explore.withdraw()
        global name1
        name1 = filedialog.askopenfilename()
        name1 = name1.replace('/','\\\\')
        W1_6.focus_set()
    def select2():
        explore = tk.Tk()
        explore.withdraw()
        global name2
        name2 = filedialog.askopenfilename()
        name2 = name2.replace('/','\\\\')
        W1_6.focus_set()
    def make():
        cmd = 'copy'+' /b '+name1+'+'+name2+' = output.jpg'
        a = os.system(cmd)
        print(name1,name2,cmd,a) 
        if a == 0:
            a = '制作成功！'
            tk.messagebox.showinfo(title="结果",message="制作成功！")
            W1_6.focus_set()
        else:
            a = '重试或再次阅读使用帮助！'                      
        showarea.config(state='normal')
        showarea.delete('1.0','end')
        showarea.insert(INSERT,'\n')
        showarea.insert(INSERT,a)
        showarea.config(state='disable')
    def help1_6():
        os.system(r'notepad ./使用说明/图种制作使用说明.txt')
    showarea = tk.Text(W1_6,bg = 'palegreen',font = ('隶书',12),width = 30,height = 3,exportselection = True,relief = RAISED,state = 'disable')
    tip1 = tk.Label(W1_6,bg='aquamarine',text='图片文件：',font = ('楷体',12))
    button1 = tk.Button(W1_6,bg='honeydew',text='选择文件',command = select1,relief = RAISED,font=('隶书',12))
    tip2 = tk.Label(W1_6,bg='aquamarine',text='压缩文件：',font = ('楷体',12))
    button2 = tk.Button(W1_6,bg='honeydew',text='选择文件',command = select2,relief = RAISED,font=('隶书',12))
    button3 = tk.Button(W1_6,bg='honeydew',text='制\n作',command = make,relief = RAISED,font=('隶书',14))
    button4 = tk.Button(W1_6,bg='honeydew',text='使用\n帮助',command = help1_6,relief = RAISED,font=('隶书',14))
    tip1.place(relx = 0.01,rely = 0.1)
    button1.place(relx = 0.35,rely = 0.1)
    tip2.place(relx = 0.01,rely = 0.4)
    button2.place(relx = 0.35,rely = 0.4)
    button3.place(relx = 0.65,rely = 0.15)
    button4.place(relx = 0.8,rely = 0.15)
    showarea.place(relx=0.05,rely=0.6)
def word_frequency_en():#词频统计（en）
    W1_7 = tk.Toplevel()
    width = 550
    heigh = 330
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W1_7.tk.call('tk', 'scaling', ScaleFactor/75)                                 #设置程序缩放
    screenwidth = W1_7.winfo_screenwidth()
    screenheight = W1_7.winfo_screenheight()
    W1_7.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W1_7.title('词频统计(en)')
    W1_7.iconbitmap('img/word_frequency_en.ico')
    W1_7.configure(bg = 'aquamarine')
    def choose():
        W1_7.focus_set()
        global file
        explore = tk.Tk()                                          #打开资源管理器窗口
        explore.withdraw()                             
        file = filedialog.askopenfilename()
        W1_7.focus_set()
        showarea1.config(state='normal')
        showarea1.delete('1.0','end')
        showarea1.insert(INSERT,file)
        showarea1.config(state='disable')
    def make():
        showarea2.delete('1.0','end')
        try:
            txt = open(file, "r",encoding='utf-8').read()
        except:
            tk.messagebox.showerror(title='错误',message='请查看使用说明\n并检查文件')
            W1_7.focus_set()
        txt = txt.lower()
        for sign in '!"#$%&()*+,-./:;<=>?@[\]^_{|}~':
            txt =txt.replace(sign, " ")
        words = txt.split()
        counts = {}
        for word in words :
            counts[word] = counts.get(word,0) + 1
        items = list(counts.items())
        items.sort(key=lambda x:x[1], reverse=True)
        for i in range(10):
            word,count = items[i]
            result = "{0:<2}{1:^10}出现次数：{2:>5}".format(i+1,word,count)
            showarea2.config(state='normal')
            showarea2.insert(INSERT,result)
            showarea2.insert(INSERT,'\n')
            showarea2.config(state='disable')
        tk.messagebox.showinfo(title="提示",message="统计完成！")
        W1_7.focus_set()
    def help1_7():
        os.system(r'notepad ./使用说明/词频统计(en)使用说明.txt')
        W1_7.focus_set()
    button1 = tk.Button(W1_7,bg='honeydew',text='选择文件',command = choose,relief = RAISED,font=('隶书',14))
    button2 = tk.Button(W1_7,bg='honeydew',text='开始\n统计',command = make,relief = RAISED,font=('隶书',14))
    button3 = tk.Button(W1_7,bg='honeydew',text='使用\n帮助',command = help1_7,relief = RAISED,font=('隶书',14))
    showarea1 = tk.Text(W1_7,bg = 'whitesmoke',font = ('隶书',10),width = 40,height = 2,exportselection = True,relief = RAISED,state='disable')
    showarea2 = tk.Text(W1_7,bg = 'paleturquoise',font = ('隶书',12),width = 40,height = 10,exportselection = True,relief = RAISED,state='disable')
    button1.place(relx=0.01,rely=0.1)
    button2.place(relx=0.01,rely=0.45)
    button3.place(relx=0.15,rely=0.45)
    showarea1.place(relx=0.3,rely=0.1)
    showarea2.place(relx=0.3,rely=0.3)
def Bvideo_download():#B站视频下载器
    W1_8 = tk.Toplevel()
    width = 900
    heigh = 550
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W1_8.tk.call('tk', 'scaling', ScaleFactor/75)                             #设置程序缩放
    screenwidth = W1_8.winfo_screenwidth()
    screenheight = W1_8.winfo_screenheight()
    W1_8.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W1_8.title('下载器') 
    W1_8.iconbitmap('img/bili_download.ico')                                                     #窗口标题
    W1_8.configure(bg = 'aquamarine')                                         #窗口背景
    def download():#B站视频下载
        url = e1.get()
        clarity = e2.get()
        cmd1 = 'cd C:/Users/10957'
        cmd2 = 'you-get -o '+path_+' '+'--format=dash-flv'+clarity+ url
        cmd = cmd1 + '&&' + cmd2
        messagebox.showinfo(title="提示",message="下载开始,请耐心等待,可能会些许卡顿！")            #弹窗提醒
        result = os.popen(cmd)
        show = result.buffer.read().decode('utf-8')
        print (show)
        messagebox.showinfo(title="提示",message="下载完成！")                                    #弹窗提醒
    def analyzing():#解析B站视频信息
        url = e1.get()
        b = os.popen('you-get -i '+ url)
        messagebox.showinfo(title="提示",message="解析开始,请耐心等待,可能会些许卡顿！")            #弹窗提醒
        c = b.buffer.read().decode('utf-8')
        print (c)
        d = open('视频信息.txt',encoding='utf-8', mode = 'w+')
        d.write(c)
        showarea1.config(state='normal')
        showarea1.delete('1.0','end')
        showarea1.insert(INSERT,c)
        showarea1.config(state='disabled')
        messagebox.showinfo(title="提示",message="解析信息已保存为文件，可前往软件同目录下查看")    #弹窗提醒
    def choose():#选取保存位置
        global path_
        path = tk.StringVar()
        path.set(os.path.abspath("."))
        path_ = askdirectory() #使用askdirectory()方法返回文件夹的路径
        if path_ == "":
            path.get() #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        else:
            path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
            path.set(path_)
        showarea2.config(state='normal')
        showarea2.delete('1.0','end')
        showarea2.insert(INSERT,path_)
        showarea2.config(state='disabled')
    def prepare():
        webbrowser.open('https://buctpjp.lanzouw.com/iCXB10aihdpe')
        time.sleep(3)
        window.focus_set()
        messagebox.showinfo(title="提示",message="下载密码为:er5k")
        time.sleep(1)
        messagebox.showinfo(title="提示",message="请将文件下载解压至 D盘根目录")
    def config():
        os.environ["PATH"] += os.pathsep + 'D:/ffmpeg/bin'
        messagebox.showinfo(title="提示",message="环境配置完成")
    def help():#使用说明
        os.system(r'notepad ./使用说明/B站视频下载器使用说明.txt')
    def communicate():#联系作者
        webbrowser.open('http://wpa.qq.com/msgrd?v=3&uin=1095765918&site=qq&menu=yes',new=0)

    button1 = tk.Button(W1_8,bg='honeydew',text='解析',command = analyzing,relief = RAISED,font=('华文新魏',18))
    button2 = tk.Button(W1_8,bg='honeydew',text='下载',command = download,background = 'black',fg = 'white',relief = RAISED,font=('华文新魏',18))
    button3 = tk.Button(W1_8,bg='honeydew',text='选择下载位置',command = choose,relief = RAISED,font=('华文新魏',14))
    showarea1 = tk.Text(W1_8,bg = 'palegreen',font = ('隶书',12),width = 70,height = 15,exportselection = True,relief = RAISED,state = 'disable')
    showarea2 = tk.Text(W1_8,bg='white',font = ('隶书',12),width = 54,height = 1,exportselection = True,relief = RAISED,state = 'disable')
    tip1 = tk.Label(W1_8,bg='aquamarine',text='   输入url地址:    ',font = ('楷体',12),padx=5,pady=5)
    e1 = tk.Entry(W1_8,cursor = 'xterm',relief = SUNKEN,width=60)
    e1.focus_set()
    tip2 = tk.Label(W1_8,bg='aquamarine',text='输入下载视频清晰度:',font = ('楷体',12),padx=5,pady=5)
    e2 = tk.Entry(W1_8,cursor = 'xterm',relief = SUNKEN,width=10)
    tip3 = tk.Label(W1_8,bg='lightcyan',fg = 'red',text='请务必阅读\n使用说明后使用',font = ('楷体',12,"bold"),padx=5,pady=5)
    tip4 = tk.Label(W1_8,bg='lightcyan',fg = 'red',text='记得添加\n空格',font = ('楷体',12,"bold"),padx=5,pady=5)

    showarea1.place(relx=0.02,rely=0.05)
    button1.place(relx=0.83,rely=0.2)
    button2.place(relx=0.83,rely=0.3)
    button3.place(relx=0.02,rely=0.7)
    showarea2.place(relx=0.3,rely=0.72)
    tip1.place(relx=0.02,rely=0.8)
    e1.place(relx=0.3,rely=0.8)
    tip2.place(relx=0.02,rely=0.9)
    e2.place(relx=0.3,rely=0.9)
    tip3.place(relx=0.8,rely=0.88)
    tip4.place(relx=0.65,rely=0.88)

    menu = tk.Menu(W1_8)                                                    #顶级菜单
    functionmenu = tk.Menu (menu, tearoff=False,background='oldlace')
    functionmenu.add_command (label="工具准备",command = prepare)
    functionmenu.add_command (label="环境配置",command=config)
    functionmenu.add_separator ()
    functionmenu.add_command (label="退出",command=window.quit)
    helpmenu = tk.Menu (menu, tearoff=False,background='oldlace')
    helpmenu.add_command (label="使用说明",command=help)
    helpmenu.add_command (label="联系作者",command=communicate)
    menu.add_cascade (label="功能",menu=functionmenu)                    
    menu.add_cascade (label="帮助",menu=helpmenu)

    W1_8.config (menu=menu)
def mathematics():#数学功能界面
    W2 = tk.Toplevel()
    width = 900
    heigh = 600
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W2.tk.call('tk', 'scaling', ScaleFactor/75)                             #设置程序缩放
    screenwidth = W2.winfo_screenwidth()
    screenheight = W2.winfo_screenheight()
    W2.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W2.title('数学')                                                            #窗口标题
    W2.iconbitmap('img/math.ico')                                                  
    W2.configure(bg = 'linen')   
def phy():#物理功能界面
    W3 = tk.Toplevel()
    width = 900
    heigh = 600
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W3.tk.call('tk', 'scaling', ScaleFactor/75)                             #设置程序缩放
    screenwidth = W3.winfo_screenwidth()
    screenheight = W3.winfo_screenheight()
    W3.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W3.title('物理')                                                      #窗口标题
    W3.iconbitmap('img/phy.ico')
    W3.configure(bg = 'linen')

    button1 = tk.Button(W3,bg='honeydew',text='不确定度(直接测量)',command = uncertainty_direct,relief = RAISED,font=('华文新魏',14))
    button1.place(relx=0.01,rely=0.2)
def uncertainty_direct():#不确定度(直接测量)
    W3_1 = tk.Toplevel()
    width = 550
    heigh = 300
    ctypes.windll.shcore.SetProcessDpiAwareness(1)                              #告诉操作系统使用程序自身的dpi适配
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)                 #获取屏幕的缩放因子
    W3_1 .tk.call('tk', 'scaling', ScaleFactor/75)                                 #设置程序缩放
    screenwidth = W3_1.winfo_screenwidth()
    screenheight = W3_1.winfo_screenheight()
    W3_1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    W3_1.title('不确定度(直接测量)')                                                      #窗口标题
    W3_1.configure(bg = 'aquamarine')                                                  #窗口背景

    def make():
        a = e1.get()
        f = eval(e2.get())
        g = e3.get()
        b=eval(a)
        c=list(b)
        n=len(c)
        x = round(np.mean(c),int(g))      #平均值
        e=[]
        for i in c:
            d=np.square(i-x)
            e.append(d)
            #print(d)
        s = round(math.sqrt(sum(e)/(n-1)),int(g))   #偏差
        u_A = round(s-math.sqrt(n),int(g))          #A类不确定度
        u_B = round(f/math.sqrt(3),int(g))          #B类不确定度
        u = round(math.sqrt(np.square(u_A)+np.square(u_B)),int(g))    #总不确定度
        o = "X = {}".format(x)
        p = "S = {}".format(s)
        q = "u_A = {}".format(u_A)
        r = "u_B = {}".format(u_B)
        t = "u = {}".format(u)
        #print(o,p,q,r,t)
        showarea.config(state='normal')
        showarea.delete('1.0','end')
        showarea.insert(INSERT,o)
        showarea.insert(INSERT,'\n')
        showarea.insert(INSERT,p)
        showarea.insert(INSERT,'\n')
        showarea.insert(INSERT,q)
        showarea.insert(INSERT,'\n')
        showarea.insert(INSERT,r)
        showarea.insert(INSERT,'\n')
        showarea.insert(INSERT,t)
        showarea.config(state='disable')
        button.focus_set()

    showarea = tk.Text(W3_1,bg = 'palegreen',font = ('隶书',12),width = 30,height = 5,exportselection = True,relief = RAISED,state = 'disable')
    tip1 = tk.Label(W3_1,bg='aquamarine',text='请输入数据:',font = ('楷体',12))
    e1 = tk.Entry(W3_1,cursor = 'xterm',relief = SUNKEN)
    mm1 = tk.Label(W3_1,bg='aquamarine',text='mm(逗号隔开)',font = ('楷体',12))
    tip2 = tk.Label(W3_1,bg='aquamarine',text='请输入仪器不确定度:',font = ('楷体',12))
    e2 = tk.Entry(W3_1,cursor = 'xterm',relief = SUNKEN)
    kg = tk.Label(W3_1,bg='aquamarine',text='mm',font = ('楷体',12))
    tip3 = tk.Label(W3_1,bg='aquamarine',text='需要保留的小数位数:',font = ('楷体',12))
    e3 = tk.Entry(W3_1,cursor = 'xterm',relief = SUNKEN)
    button = tk.Button(W3_1,bg='honeydew',text='计\n算',command = make,relief = RAISED,font=('隶书',14))
    tip1.place(relx = 0.01,rely = 0.1)
    e1.place(relx = 0.4,rely = 0.1)
    mm1.place(relx = 0.77,rely = 0.1)
    tip2.place(relx = 0.01,rely = 0.3)
    e2.place(relx = 0.4,rely = 0.3)
    kg.place(relx = 0.77,rely = 0.3)
    tip3.place(relx = 0.01,rely = 0.5)
    e3.place(relx = 0.4,rely = 0.5)
    button.place(relx = 0.82,rely = 0.23)
    showarea.place(relx=0.05,rely=0.6)
    e1.focus_set()  
def communicate():#联系作者
    webbrowser.open('http://wpa.qq.com/msgrd?v=3&uin=1095765918&site=qq&menu=yes',new=0)
def help():#使用帮助
    os.startfile(r".\\使用说明")

pic = Image.open('res/img/bg.jpg')
pic1 = pic.resize((356,200),Image.Resampling.LANCZOS)
picture = ImageTk.PhotoImage(pic1)
showarea = tk.Label(window,bg='white',image=picture)
showarea.bind("<Button-1>", tip)  
showarea.place(relx=0,rely=0)

menu = tk.Menu(window)                                                    

functionmenu = tk.Menu (menu, tearoff=False,background='oldlace')
functionmenu.add_command (label="日常",command=common)
functionmenu.add_command (label="物理",command=phy)
functionmenu.add_command (label="数学",command=mathematics)
functionmenu.add_separator ()
functionmenu.add_command (label="退出",command=window. quit)
helpmenu = tk.Menu (menu, tearoff=False,background='oldlace')
helpmenu.add_command (label="使用说明",command=help)
helpmenu.add_command (label="联系作者",command=communicate)
menu.add_cascade(label="软件功能",menu=functionmenu)
menu.add_cascade(label="反馈帮助",menu=helpmenu)

window.config (menu=menu)
window.mainloop()

