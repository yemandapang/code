from tkinter import *
import random
import sys
sys.path.append("./para")
from tflite_take import take_one
from PIL import Image, ImageTk

#  批处理
def run1():
     batch = 32

     weight_name = inp1.get()
     weight = take_one(weight_name)
     start = 'the weight_name is \n'
     txt.insert(END, start)#   显示名字并换行
     txt.insert(END, weight)   # 显示weight
     txt.insert(END, '\n')   # 换行
     inp1.delete(0, END)  # 清空输入

#  单张
def run2():
     batch = 1

     biase_name = inp2.get()
     biase = take_one(biase_name)
     start = 'the biase_name is \n'
     txt.insert(END, start)#   显示名字并换行
     txt.insert(END, biase)   # 显示biase
     txt.insert(END, '\n')  # 换行
     inp2.delete(0, END)  # 清空输入

#  发送数据给FPGA
def run3():
     a = float(x)
     b = float(y)
     s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
     start = 'the result is \n'
     txt.insert(END, start)   #   显示名字并换行
     txt.insert(END, s)   # 显示计算结果
     txt.insert(END, '\n')  #  换行

#  得到FPGA计算结果
def run4():

     result = 0

     lb1 = Label(root, text=str(result))
     lb1.place(relx=0.7, rely=0.6, relwidth=0.1, relheight=0.1)

     #
     # a = float(x)
     # b = float(y)
     # s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
     # start = ' passed \n'
     # txt.insert(END, start)  # 显示名字并换行
     # txt.insert(END, '\n')  # 换行
     # inp1.delete(0, END)  # 清空输入
     # inp2.delete(0, END)  # 清空输入

root = Tk()
root.geometry('800x800')
root.title('FPGA 通讯器')

pilImage = Image.open("test0.jpg")
tkImage = ImageTk.PhotoImage(image=pilImage)
lb2 = Label(image=tkImage)
lb2.place(relx=0.1, rely=0.3)


# inp1 = Entry(root)
# inp1.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)
# inp2 = Entry(root)
# inp2.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)

# 设定批处理模式           run1()
btn1 = Button(root, text='批处理', command=run1)
btn1.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)

# 设定单张处理模式             run2()
btn2 = Button(root, text='单张', command=run2)
btn2.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.1)

# 发送数据给FPGA  run3()
btn3 = Button(root, text='发送', command=run3)
btn3.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

# 接受得到的计算结果  run4()
btn4 = Button(root, text='计算mAp', command=run4)
btn4.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.1)


# 显示精度
lb1 = Label(root, text='mAp 是：  ')
lb1.place(relx=0.6, rely=0.6, relwidth=0.1, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
# txt = Text(root)
# txt.place(relx=0.0, rely=0.5, relwidth=0.4,relheight=0.5)

# txt0 = Text(root)
# txt0.place(relx=0.5, rely=0.6, relwidth=0.4,relheight=0.5)

root.mainloop()