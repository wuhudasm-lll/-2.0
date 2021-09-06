# # # # # # # #
# python
# # # # # # # #
# coding:utf-8
# 小组成员：
# 余唯炜 2019051009044
# 郭永青 2019051009014
import qtawesome
from tkinter import *
import os
import time
import threading
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
import pymysql
import xlrd


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QStackedWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(self.close1)  # 关闭窗口
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_visit.clicked.connect(self.back)  # 关闭窗口
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(self.showMinimized)  # 最小化窗口

        self.left_label_1 = QtWidgets.QPushButton("信息更改")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("成绩统计")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("帮助与用户")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.address-card-o', color='white'), "信息查找")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.left_button1_clicked2)
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.trash-o', color='white'), "信息删除")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.left_button1_clicked3)
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='white'), "信息修改")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(self.left_button1_clicked4)
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.plus-square-o', color='white'), "信息增加")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(self.left_button1_clicked5)
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart', color='white'), "成绩排名")
        self.left_button_5.setObjectName('left_button')
        self.left_button_5.clicked.connect(self.left_button1_clicked6)
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart', color='white'), "学科统计")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(self.left_button1_clicked7)
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.user-o', color='white'), "个人中心")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.left_button1_clicked)
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.pie-chart', color='white'), "成绩分布")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.left_button1_clicked8)
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(self.left_button1_clicked1)
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        #默认页面
        self.form1 = QWidget()
        self.right_widget.addWidget(self.form1)
        self.formLayout1 = QtWidgets.QGridLayout(self.form1)

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.right_folder_button22 = QtWidgets.QPushButton(qtawesome.icon('fa.folder', color='GoldenRod'), "")
        self.right_folder_button22.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:none}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button22.setObjectName('right_search_button')
        self.right_folder_button22.setFont(qtawesome.font('fa', 16))
        self.right_folder_button22.clicked.connect(self.right_folder_button_clicked31)
        self.right_folder_button22.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button11 = QtWidgets.QPushButton("导入数据库")
        self.right_folder_button11.setObjectName('right_search_button')
        self.right_folder_button11.setFont(qtawesome.font('fa', 16))
        self.right_folder_button11.clicked.connect(self.right_folder_button_clicked51)
        self.right_folder_button11.setFixedSize(140, 40)  # 设置按钮大小
        self.right_folder_button11.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button111 = QtWidgets.QPushButton("清空数据库")
        self.right_folder_button111.setObjectName('right_search_button')
        self.right_folder_button111.setFont(qtawesome.font('fa', 16))
        self.right_folder_button111.clicked.connect(self.view_data23)
        self.right_folder_button111.setFixedSize(140, 40)  # 设置按钮大小
        self.right_folder_button111.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input9 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input9.setPlaceholderText("填入或选择需要上传的文件夹")
        self.right_bar_widget_folder_input9.setObjectName("right_input_item")
        self.right_bar_widget_folder_input9.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.user11 = QtWidgets.QLabel("数据的导入")
        self.user11.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user11, 0, 0,1,10)

        self.recommend_button_11 = QtWidgets.QToolButton()
        self.recommend_button_11.setIcon(QtGui.QIcon('./5.jpg'))
        self.recommend_button_11.setIconSize(QtCore.QSize(1000, 1000))
        self.right_bar_layout1.addWidget(self.recommend_button_11, 0, 0, 10, 10)
        self.recommend_button_11.setStyleSheet('''
                                                QToolButton{border:none;color:black;}
                                                QToolButton:hover{color:white}
                                                 ''')
        self.right_bar_layout1.addWidget(self.right_folder_button22, 8, 1, 20, 6)
        self.right_bar_layout1.addWidget(self.right_folder_button11, 10, 3, 20,1)
        self.right_bar_layout1.addWidget(self.right_folder_button111, 10, 5, 20, 1)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input9, 8, 2, 20, 6)
        self.formLayout1.addWidget(self.right_bar_widget1, 0, 0, 9, 0)

        #个人中心
        self.form2 = QWidget()
        self.right_widget.addWidget(self.form2)
        self.formLayout2 = QtWidgets.QGridLayout(self.form2)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        # 2.2 个人信息
        self.a = QPushButton(qtawesome.icon('fa.user', color="black"), ":")  #个人账号
        self.a.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.mars', color="black"), ":")  # 个人账号
        self.a1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a2 = QPushButton(qtawesome.icon('fa.university', color="black"), ":")  # 个人账号
        self.a2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a3 = QPushButton(qtawesome.icon('fa.birthday-cake', color="black"), ":")  # 个人账号
        self.a3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a4 = QPushButton(qtawesome.icon('fa.child', color="black"), ":")  # 个人账号
        self.a4.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.user9 = QtWidgets.QLabel("个人资料")
        self.user9.setFont(qtawesome.font('fa', 31))
        self.right_bar_layout1.addWidget(self.user9, 0, 1, 2, 4)
        f = open("2.txt", 'r+')
        word = f.readline()
        self.user = QtWidgets.QLabel(word)
        self.user.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user, 3, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a, 3, 2, 2, 3)
        self.user1 = QtWidgets.QLabel("男")
        self.user1.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user1, 5, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a1, 5, 2, 2, 3)
        self.user4 = QtWidgets.QLabel("余唯炜")
        self.user4.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user4, 4, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a4, 4, 2, 2, 3)
        self.user2 = QtWidgets.QLabel("重庆师范大学")
        self.user2.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user2, 6, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a2, 6, 2, 2, 3)
        self.user3 = QtWidgets.QLabel("2001.01.18")
        self.user3.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user3, 7, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a3, 7, 2, 2, 3)
        self.a.setFont(qtawesome.font('fa', 22))
        self.a.setIconSize(QtCore.QSize(20, 20))
        self.user.setObjectName('right_search_button1')
        self.xiugai = QtWidgets.QPushButton(qtawesome.icon('fa.address-card', color='black'), "修改密码")
        self.xiugai.setObjectName('right_search_button2')
        self.xiugai.setFont(qtawesome.font('fa', 30))
        self.xiugai.clicked.connect(self.right_folder_button_clicked)
        self.right_bar_layout1.addWidget(self.xiugai, 26, 4, 1, 3)
        self.xiugai.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.zhuxiao = QtWidgets.QPushButton(qtawesome.icon('fa.reply-all', color='black'),"注销账号")
        self.zhuxiao.setObjectName('right_search_button2')
        self.zhuxiao.setFont(qtawesome.font('fa', 16))
        self.zhuxiao.clicked.connect(self.right_folder_button_clicked1)
        self.right_bar_layout1.addWidget(self.zhuxiao, 27, 4, 1, 3)
        self.zhuxiao.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.bianji = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='black'), "编辑资料")
        self.bianji.setObjectName('right_search_button3')
        self.bianji.setFont(qtawesome.font('fa', 16))
        self.bianji.clicked.connect(self.right_folder_button_clicked2)
        self.right_bar_layout1.addWidget(self.bianji, 25, 4, 1, 3)
        self.bianji.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setIcon(QtGui.QIcon('./3.png'))
        self.recommend_button_1.setIconSize(QtCore.QSize(200, 200))
        self.right_bar_layout1.addWidget(self.recommend_button_1, 3, 1, 6, 1)
        self.recommend_button_1.setStyleSheet('''
                                 QToolButton{border:none;color:black;}
                                 QToolButton:hover{color:white}
                                  ''')
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 9)

        self.right_bar_widget2 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout2 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget2.setLayout(self.right_bar_layout2)
        self.formLayout2.addWidget(self.right_bar_widget2, 1, 0, 1, 9)

        # 右边栏美化
        # 右边框整体风格美化
        self.right_widget.setStyleSheet('''
                    QStackedWidget#right_stacked_Widget{
                        color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-right-radius:10px;
                        border-bottom-right-radius:10px;
                    }

                    QLabel#right_lable{
                        border:none;
                        font-size:16px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                ''')

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
                   QPushButton{border:none;color:white;}
                   QPushButton#left_label{
                       border:none;
                       border-bottom:1px solid SteelBlue;
                       font-size:18px;
                       font-weight:700;
                       font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                   }
                   QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}

                   QWidget#left_widget{
                       background:SteelBlue;
                       border-top:1px solid white;
                       border-bottom:1px solid white;
                       border-left:1px solid white;
                       border-top-left-radius:10px;
                       border-bottom-left-radius:10px;
                   }
               ''')

        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')
        self.main_layout.setSpacing(0)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # 遇到问题
        self.form3 = QWidget()
        self.right_widget.addWidget(self.form3)
        self.formLayout2 = QtWidgets.QGridLayout(self.form3)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        # 2.2 问题
        self.user9 = QtWidgets.QLabel("关于与帮助")
        self.user9.setFont(qtawesome.font('fa', 30))
        self.right_bar_layout1.addWidget(self.user9, 0, 1, 2, 4)
        self.user = QtWidgets.QPushButton(qtawesome.icon('fa.question-circle-o', color="black"), "使用帮助")
        self.user.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user, 8, 3, 1,4)
        self.user.clicked.connect(self.right_folder_button_clicked3)
        self.user.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.user1 = QtWidgets.QPushButton(qtawesome.icon('fa.envelope-open-o', color="black"), "反馈问题")
        self.user1.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user1, 9, 3, 1,4)
        self.user1.clicked.connect(self.right_folder_button_clicked4)
        self.user1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.user2 = QtWidgets.QPushButton(qtawesome.icon('fa.internet-explorer', color="black"), "学校官网")
        self.user2.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user2, 10,3, 1,4)
        self.user2.clicked.connect(self.right_folder_button_clicked5)
        self.user2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.user3 = QtWidgets.QPushButton(qtawesome.icon('fa.users', color="black"), "主创人员")
        self.user3.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user3, 11, 3, 1,4)
        self.user3.clicked.connect(self.right_folder_button_clicked6)
        self.user3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 5)
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setIcon(QtGui.QIcon('./4.jpg'))
        self.recommend_button_1.setIconSize(QtCore.QSize(1000, 1000))
        self.right_bar_layout1.addWidget(self.recommend_button_1, 2, 1, 6, 8)
        self.recommend_button_1.setStyleSheet('''
                                         QToolButton{border:none;color:black;}
                                         QToolButton:hover{color:white}
                                          ''')
        self.right_bar_widget2 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout2 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget2.setLayout(self.right_bar_layout2)
        self.formLayout2.addWidget(self.right_bar_widget2, 1, 0, 1, 9)


        # 信息查询
        self.form4 = QWidget()
        self.right_widget.addWidget(self.form4)
        self.formLayout2 = QtWidgets.QGridLayout(self.form4)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm5 = QtWidgets.QLabel('信息查询')
        self.mm5.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button1 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "查询")
        self.right_folder_button1.setObjectName('right_search_button')
        self.right_folder_button1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button1.setFont(qtawesome.font('fa', 20))
        self.right_folder_button1.clicked.connect(self.view_data111)
        self.right_folder_button1.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "清空")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        self.right_folder_button3.clicked.connect(self.view_data2)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2.clicked.connect(self.view_data)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input88 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input88.setPlaceholderText("请输入学号/姓名")
        self.right_bar_widget_folder_input88.setObjectName("right_input_item");
        self.right_bar_widget_folder_input88.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm5, 0, 0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button1, 1, 21, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input88, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)
        #消息框美化
        self.right_message_Alter.setStyleSheet(''' 
                                           QMessageBox{
                                               background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,stop: 0 rgba(255, 255, 255, 100%),
                                               stop: 1 rgba(70, 130, 180, 100%));
                                               border-top:1px solid black;
                                               border-bottom:1px solid black;
                                               border-left:1px solid black;
                                               border-right:1px solid black;
                                               border-radius:10px;
                                               padding:2px 4px;
                                           }   
                                       ''')
        self.right_batch_result_listView.setStyleSheet('''
                    QListView {
                        alternate-background-color: yellow; 
                        padding:2px 4px;
                    }
                    QListView {
                    show-decoration-selected: 1; /* make the selection span the entire width of the view */
                    }
                    /* 此处QListView::item:alternate覆盖会alternate-background-color: yellow属性*/
                    QListView::item:alternate {
                        background: #EEEEEE; /* item交替变换颜色，如图中灰色 */
                    }
                    QListView::item:selected {
                    border: 1px solid #6a6ea9;
                    }
                    QListView::item:selected:!active {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #ABAFE5, 
                                                 stop: 1 #8588B2);
                    }
                    QListView::item:selected:active {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #6a6ea9, 
                                                 stop: 1 #888dd9);
                    }
                    QListView::item:hover {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #FAFBFE, 
                                                 stop: 1 #DCDEF1);

                ''')

        # 信息删除

        self.form5 = QWidget()
        self.right_widget.addWidget(self.form5)
        self.formLayout2 = QtWidgets.QGridLayout(self.form5)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm5 = QtWidgets.QLabel('信息删除')
        self.mm5.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button211 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "删除")
        self.right_folder_button211.setObjectName('right_search_button')
        self.right_folder_button211.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button211.setFont(qtawesome.font('fa', 20))
        self.right_folder_button211.clicked.connect(self.view_data3)
        self.right_folder_button211.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button211.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "清空")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        self.right_folder_button3.clicked.connect(self.view_data22)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2.clicked.connect(self.view_data11)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input112 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input112.setPlaceholderText("请输入学号/姓名")
        self.right_bar_widget_folder_input112.setObjectName("right_input_item");
        self.right_bar_widget_folder_input112.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm5, 0, 0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button211, 1, 21, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input112, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView1 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView1, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        #信息修改
        self.form6 = QWidget()
        self.right_widget.addWidget(self.form6)
        self.formLayout2 = QtWidgets.QGridLayout(self.form6)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm4 = QtWidgets.QLabel('信息修改')
        self.mm4.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button211 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "查询")
        self.right_folder_button211.setObjectName('right_search_button')
        self.right_folder_button211.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button211.setFont(qtawesome.font('fa', 20))
        self.right_folder_button211.clicked.connect(self.view_data4)
        self.right_folder_button211.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button211.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='balck'), "修改")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        self.right_folder_button3.clicked.connect(self.view_data24)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")


        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2.clicked.connect(self.view_data1111)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input11 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input11.setPlaceholderText("请输入学号/姓名")
        self.right_bar_widget_folder_input11.setObjectName("right_input_item");
        self.right_bar_widget_folder_input11.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm4, 0, 0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button211, 1, 21, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input11, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView2 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView2, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        # 信息增加

        self.form6 = QWidget()
        self.right_widget.addWidget(self.form6)
        self.formLayout2 = QtWidgets.QGridLayout(self.form6)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm = QtWidgets.QLabel('信息增加')
        self.mm.setFont(qtawesome.font('fa', 35))

        self.right_folder_button2111 = QtWidgets.QPushButton(qtawesome.icon('fa.user-o', color='balck'), "查询增加的学生信息")
        self.right_folder_button2111.setObjectName('right_search_button')
        self.right_folder_button2111.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2111.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2111.clicked.connect(self.view_data53)
        self.right_folder_button2111.setFixedSize(250, 30)  # 设置按钮大小
        self.right_folder_button2111.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button28 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'),
                                                             "清空")
        self.right_folder_button28.setObjectName('right_search_button')
        self.right_folder_button28.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button28.setFont(qtawesome.font('fa', 20))
        self.right_folder_button28.clicked.connect(self.view_data54)
        self.right_folder_button28.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button28.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button23 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button23.setObjectName('right_search_button')
        self.right_folder_button23.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button23.setFont(qtawesome.font('fa', 20))
        self.right_folder_button23.clicked.connect(self.view_data52)
        self.right_folder_button23.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button23.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button31 = QtWidgets.QPushButton(qtawesome.icon('fa.check-circle', color='balck'), "完成")
        self.right_folder_button31.setObjectName('right_search_button')
        self.right_folder_button31.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button31.setFont(qtawesome.font('fa', 20))
        self.right_folder_button31.clicked.connect(self.view_data51)
        self.right_folder_button31.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button31.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button311 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='balck'), "增加")
        self.right_folder_button311.setObjectName('right_search_button')
        self.right_folder_button311.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button311.setFont(qtawesome.font('fa', 20))
        self.right_folder_button311.clicked.connect(self.view_data5)
        self.right_folder_button311.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button311.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_layout1.addWidget(self.mm, 0,0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2111, 1, 9, 1, 11)
        self.right_bar_layout1.addWidget(self.right_folder_button23, 0, 9, 1, 6)
        self.right_bar_layout1.addWidget(self.right_folder_button28, 0, 15, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button31, 0, 6, 1, 2)
        self.right_bar_layout1.addWidget(self.right_folder_button311, 0, 4, 1, 2)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView3 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView3, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        # 成绩排名
        self.form7 = QWidget()
        self.right_widget.addWidget(self.form7)
        self.formLayout2 = QtWidgets.QGridLayout(self.form7)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm1 = QtWidgets.QLabel('成绩排名')
        self.mm1.setFont(qtawesome.font('fa', 35))
        self.right_folder_buttona1 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='balck'), "")
        self.right_folder_buttona1.setObjectName('right_search_button')
        self.right_folder_buttona1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_buttona1.setFont(qtawesome.font('fa', 20))
        self.right_folder_buttona1.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button81 = QtWidgets.QPushButton(qtawesome.icon('fa.sort-amount-desc', color='balck'),
                                                             "统计")
        self.right_folder_button81.setObjectName('right_search_button')
        self.right_folder_button81.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button81.setFont(qtawesome.font('fa', 20))
        self.right_folder_button81.clicked.connect(self.view_data6)
        self.right_folder_button81.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button81.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button88 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'),
                                                           "清除")
        self.right_folder_button88.setObjectName('right_search_button')
        self.right_folder_button88.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button88.setFont(qtawesome.font('fa', 20))
        self.right_folder_button88.clicked.connect(self.view_data66)
        self.right_folder_button88.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button88.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input114 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input114.setPlaceholderText("请输入学科")
        self.right_bar_widget_folder_input114.setObjectName("right_input_item");
        self.right_bar_widget_folder_input114.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.right_bar_layout1.addWidget(self.right_folder_buttona1, 1, 1, 1, 20)
        self.right_bar_layout1.addWidget(self.mm1, 0, 0)
        self.right_bar_layout1.addWidget(self.right_folder_button81, 1, 12, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button88, 1, 16, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input114, 1, 2, 1, 10)
        self.formLayout2.addWidget(self.right_bar_widget1, 1, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.textEdit = QtWidgets.QLabel()
        self.textEdit1 = QtWidgets.QLabel()
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView4 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 1)
        self.right_bar_layout3.addWidget(self.textEdit, 0, 1, 1, 3)
        self.right_bar_layout3.addWidget(self.textEdit1, 0, 4, 1, 3)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView4, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        # 学科统计
        self.form8 = QWidget()
        self.right_widget.addWidget(self.form8)
        self.formLayout2 = QtWidgets.QGridLayout(self.form8)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm2 = QtWidgets.QLabel('学科统计')
        self.mm2.setFont(qtawesome.font('fa', 35))
        self.right_folder_buttona1 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='balck'), "")
        self.right_folder_buttona1.setObjectName('right_search_button')
        self.right_folder_buttona1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_buttona1.setFont(qtawesome.font('fa', 20))
        self.right_folder_buttona1.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button811 = QtWidgets.QPushButton(qtawesome.icon('fa.pie-chart', color='balck'),
                                                           "统计")
        self.right_folder_button811.setObjectName('right_search_button')
        self.right_folder_button811.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button811.setFont(qtawesome.font('fa', 20))
        self.right_folder_button811.clicked.connect(self.view_data7)
        self.right_folder_button811.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button811.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button91 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'),
                                                           "清空")
        self.right_folder_button91.setObjectName('right_search_button')
        self.right_folder_button91.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button91.setFont(qtawesome.font('fa', 20))
        self.right_folder_button91.clicked.connect(self.view_data71)
        self.right_folder_button91.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button91.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input115 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input115.setPlaceholderText("请输入学科")
        self.right_bar_widget_folder_input115.setObjectName("right_input_item");
        self.right_bar_widget_folder_input115.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm2, 0, 0, 1, 8)
        self.right_bar_layout1.addWidget(self.right_folder_buttona1, 1, 1, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button811, 1, 15, 1, 2)
        self.right_bar_layout1.addWidget(self.right_folder_button91, 1, 18, 1, 2)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input115, 1, 2, 1, 10)
        self.formLayout2.addWidget(self.right_bar_widget1, 1, 0, 1, 0)

        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView5 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 1)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView5, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        # 成绩分布
        self.form9 = QWidget()
        self.right_widget.addWidget(self.form9)
        self.formLayout2 = QtWidgets.QGridLayout(self.form9)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm3 = QtWidgets.QLabel('成绩分布')
        self.mm3.setFont(qtawesome.font('fa', 35))
        self.right_folder_buttona12 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_buttona12.setObjectName('right_search_button')
        self.right_folder_buttona12.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_buttona12.setFont(qtawesome.font('fa', 20))
        self.right_folder_buttona12.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button911 = QtWidgets.QPushButton(qtawesome.icon('fa.table', color='balck'),
                                                            "统计")
        self.right_folder_button911.setObjectName('right_search_button')
        self.right_folder_button911.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button911.setFont(qtawesome.font('fa', 20))
        self.right_folder_button911.clicked.connect(self.view_data8)
        self.right_folder_button911.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button911.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button101 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'),
                                                           "清空")
        self.right_folder_button101.setObjectName('right_search_button')
        self.right_folder_button101.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button101.setFont(qtawesome.font('fa', 20))
        self.right_folder_button101.clicked.connect(self.view_data81)
        self.right_folder_button101.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button101.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")


        self.right_bar_widget_folder_input119 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input119.setPlaceholderText("请输入姓名/学号")
        self.right_bar_widget_folder_input119.setObjectName("right_input_item");
        self.right_bar_widget_folder_input119.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.right_bar_layout1.addWidget(self.mm3, 0, 0, 1, 8)
        self.right_bar_layout1.addWidget(self.right_folder_buttona12, 1, 1, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button911, 1, 15, 1, 2)
        self.right_bar_layout1.addWidget(self.right_folder_button101, 1, 18, 1, 2)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input119, 1, 2, 1, 10)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView6 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 1)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView6, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)


    # 导入数据库
    def back(self):
            self.right_widget.setCurrentIndex(0)

     #个人中心
    def left_button1_clicked(self):
         self.right_widget.setCurrentIndex(1)

    #遇到问题
    def left_button1_clicked1(self):
        self.right_widget.setCurrentIndex(2)
        #信息查询

    def left_button1_clicked2(self):
         self.right_widget.setCurrentIndex(3)
    #信息删除
    def left_button1_clicked3(self):
        self.right_widget.setCurrentIndex(4)
        # 信息修改

    def left_button1_clicked4(self):
        self.right_widget.setCurrentIndex(5)
        # 信息增加

    def left_button1_clicked5(self):
        self.right_widget.setCurrentIndex(6)

        # 成绩排名

    def left_button1_clicked6(self):
        self.right_widget.setCurrentIndex(7)

        # 学科统计

    def left_button1_clicked7(self):
        self.right_widget.setCurrentIndex(8)

      # 成绩分布
    def left_button1_clicked8(self):
        self.right_widget.setCurrentIndex(9)

    #修改密码
    def right_folder_button_clicked(self):
        w3.show()

    #个人中心注销账号
    def right_folder_button_clicked1(self):
        demo.close()
        login.show()

    #编辑资料
    def right_folder_button_clicked2(self):
        pass

    #默认页面的路径选择
    def right_folder_button_clicked31(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        demo.right_bar_widget_folder_input9.setText(fileName)

     #导入数据库
    def right_folder_button_clicked51(self):
      try:
        file = open("8.txt", 'w').close()
        ap = demo.right_bar_widget_folder_input9.text()
        if ap == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
          book = xlrd.open_workbook(ap)
          sheet = book.sheet_by_index(0)
        # 建立一个MySQL连接
          conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='student',
            charset='utf8'
          )
        # 获得游标
          cur = conn.cursor()
        # 创建插入SQL语句
          query = 'insert into student(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
          for r in range(0, sheet.nrows):
            学号 = sheet.cell(r, 0).value
            姓名 = sheet.cell(r, 1).value
            专业 = sheet.cell(r, 2).value
            班级 = sheet.cell(r, 3).value
            高级程序语言 = sheet.cell(r, 4).value
            python编程 = sheet.cell(r, 5).value
            数据库原理 = sheet.cell(r, 6).value
            数据结构与算法 = sheet.cell(r, 7).value
            数学分析 = sheet.cell(r, 8).value
            高等数学 = sheet.cell(r, 9).value
            网络爬虫 = sheet.cell(r, 10).value
            数据可视化 = sheet.cell(r, 11).value
            数据挖掘 = sheet.cell(r, 12).value
            数据分析 = sheet.cell(r, 13).value
            with open('8.txt', 'a') as f3:
                f3.write(sheet.cell(r, 0).value + " " + sheet.cell(r, 1).value+"\n")
            values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
            # 执行sql语句
            cur.execute(query, values)
          cur.close()
          conn.commit()
          conn.close()
          QMessageBox.information(self, '成功', '导入成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
      except:
          QMessageBox.information(self, '错误', '导入失败', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #使用帮助
    def right_folder_button_clicked3(self):
        self.right_message_Alter.information(self.right_message_Alter, "联系方式", self.tr("如果有什么问题可以通过以下方式联系我们：\nQQ:"
                                                                                       "1370969596\n电话：19115505545\n邮"
                                                                                       "箱：1370969596@qq.com"))

    #反馈问题
    def right_folder_button_clicked4(self):
        self.right_message_Alter.information(self.right_message_Alter, "使用说明", self.tr("该应用程序使用说明如下：\n1.分为了3大类分别为信息的更改，成绩的统计,帮助和用户。\n2.在信息更改中可以实现对学生信息的增删改查。3.在成绩的统计中可以查看到成绩的排名和分布等。\n4.当然如果有问题可以在遇到问题中咨询我们也可以设置自己的密码查看自己的资料。"))

    #学校官网
    def right_folder_button_clicked5(self):
        webbrowser.open("https://www.cqnu.edu.cn/", new=0)

    #主创人员
    def right_folder_button_clicked6(self):
        self.right_message_Alter.information(self.right_message_Alter, "主创人员", self.tr("该程序的主创人员为：\n1.余唯炜 QQ:1370969596\n2.郭永青 QQ:1795880609"))

    #信息查询中查询全部信息
    def view_data(self):
        try:
            global db
            db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName('localhost')
            db.setDatabaseName('student')
            db.setUserName('root')
            db.setPassword('')
            if not db.open():  # 判断数据库是否打开
                print(db.lastError().text())  # 打印操作数据库时出现的错误
                return False
            else:
                print("连接成功")
        except:
            pass

            # 实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView.setModel(self.model)
        self.model.setTable('student')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据

    #删除中的查询全部信息
    def view_data11(self):
            try:
                global db
                # 调用输入框获取数据库名称
                db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName('localhost')
                db.setDatabaseName('student')
                db.setUserName('root')
                db.setPassword('')
                if not db.open():  # 判断数据库是否打开
                    print(db.lastError().text())  # 打印操作数据库时出现的错误
                    return False
                else:
                    print("连接成功")
            except :
                pass

                # 实例化一个可编辑数据模型
            self.model = QtSql.QSqlTableModel()
            self.right_batch_result_listView1.setModel(self.model)
            self.model.setTable('student')  # 设置使用数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model.select()  # 查询所有数据

    #信息查询中的查询
    def view_data111(self):
        account_dict = {}
        f = open("8.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account_keys = list(account_dict.keys())
        account_value = list(account_dict.values())
        gettxt= self.right_bar_widget_folder_input88.text()
        if gettxt == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
              conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
              cur = conn.cursor()  # 获取一个游标
              if gettxt in account_keys:
                 sql_select = "select * from student where 学号='{}'".format(gettxt)  # 定义查询
                 cur.execute(sql_select)  # 执行查询
                 data = cur.fetchall()  # 获取查询到数据
                 # 创建插入SQL语句
                 # 获得游标
                 cur = conn.cursor()
                 query = 'insert ignore into student1(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                 # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
                 for r in range(1):
                     学号 = data[0][0]
                     姓名 = data[0][1]
                     专业 = data[0][2]
                     班级 = data[0][3]
                     高级程序语言 = data[0][4]
                     python编程 = data[0][5]
                     数据库原理 = data[0][6]
                     数据结构与算法 = data[0][7]
                     数学分析 = data[0][8]
                     高等数学 = data[0][9]
                     网络爬虫 = data[0][10]
                     数据可视化 = data[0][11]
                     数据挖掘 = data[0][12]
                     数据分析 = data[0][13]
                     values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
                     # 执行sql语句
                     # cur.execute(query1)
                     cur.execute(query, values)
                 conn.commit()  # 提交事务
                 cur.close()  # 关闭游标
                 conn.close()  # 释放数据库资源在这里插入代码片
                 # 实例化一个可编辑数据模型
                 global db
                 db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                 db.setHostName('localhost')
                 db.setDatabaseName('student')
                 db.setUserName('root')
                 db.setPassword('')
                 if not db.open():  # 判断数据库是否打开
                     print(db.lastError().text())  # 打印操作数据库时出现的错误
                     return False
                 else:
                     self.model = QtSql.QSqlTableModel()
                     self.right_batch_result_listView.setModel(self.model)
                     self.model.setTable('student1')  # 设置使用数据模型的数据表
                     self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                     self.model.select()  # 查询所有数据
              elif gettxt in account_value:
                  sql_select = "select * from student where 姓名='{}'".format(gettxt)  # 定义查询
                  cur.execute(sql_select)  # 执行查询
                  data = cur.fetchall()  # 获取查询到数据
                  # 创建插入SQL语句
                  # 获得游标
                  cur = conn.cursor()
                  query = 'insert ignore into student1(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                  # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
                  for r in range(1):
                      学号 = data[0][0]
                      姓名 = data[0][1]
                      专业 = data[0][2]
                      班级 = data[0][3]
                      高级程序语言 = data[0][4]
                      python编程 = data[0][5]
                      数据库原理 = data[0][6]
                      数据结构与算法 = data[0][7]
                      数学分析 = data[0][8]
                      高等数学 = data[0][9]
                      网络爬虫 = data[0][10]
                      数据可视化 = data[0][11]
                      数据挖掘 = data[0][12]
                      数据分析 = data[0][13]
                      values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
                      # 执行sql语句
                      # cur.execute(query1)
                      cur.execute(query, values)
                  conn.commit()  # 提交事务
                  cur.close()  # 关闭游标
                  conn.close()  # 释放数据库资源在这里插入代码片
                  # 实例化一个可编辑数据模型
                  db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                  db.setHostName('localhost')
                  db.setDatabaseName('student')
                  db.setUserName('root')
                  db.setPassword('')
                  if not db.open():  # 判断数据库是否打开
                      print(db.lastError().text())  # 打印操作数据库时出现的错误
                      return False
                  else:
                      self.model = QtSql.QSqlTableModel()
                      self.right_batch_result_listView.setModel(self.model)
                      self.model.setTable('student1')  # 设置使用数据模型的数据表
                      self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                      self.model.select()  # 查询所有数据
              else:
                  QMessageBox.information(self, '错误', '不存在该学生信息', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #修改中的查询全部信息
    def view_data1111(self):
        try:
            global db
            db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName('localhost')
            db.setDatabaseName('student')
            db.setUserName('root')
            db.setPassword('')
            if not db.open():  # 判断数据库是否打开
                print(db.lastError().text())  # 打印操作数据库时出现的错误
                return False
            else:
                print("连接成功")
        except :
            pass

            # 实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView2.setModel(self.model)
        self.model.setTable('student')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据

    #查询中的清除，清除student1
    def view_data2(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        query1 ='truncate table student1;'
        cur.execute(query1)
        conn.commit()  # 提交事务
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源在这里插入代码片
        global db
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
            self.model = QtSql.QSqlTableModel()
            self.right_batch_result_listView.setModel(self.model)
            self.model.setTable('student1')  # 设置使用数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model.select()  # 查询所有数据

    #删除中的清空，清空student2
    def view_data22(self):
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            query1 = 'truncate table student2;'
            cur.execute(query1)
            conn.commit()  # 提交事务
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源在这里插入代码片
            global db
            db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName('localhost')
            db.setDatabaseName('student')
            db.setUserName('root')
            db.setPassword('')
            if not db.open():  # 判断数据库是否打开
                print(db.lastError().text())  # 打印操作数据库时出现的错误
                return False
            else:
                print("连接成功")
                self.model = QtSql.QSqlTableModel()
                self.right_batch_result_listView1.setModel(self.model)
                self.model.setTable('student2')  # 设置使用数据模型的数据表
                self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                self.model.select()  # 查询所有数据

     #清空数据库student
    def view_data23(self):
        try:
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            query1 = 'truncate table student;'
            cur.execute(query1)
            conn.commit()  # 提交事务
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源在这里插入代码片
            QMessageBox.information(self, '成功', '清除成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        except:
            QMessageBox.information(self, '错误', '清除失败', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #修改
    def view_data24(self):
      try:
        account_dict = {}
        f = open("8.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account_keys = list(account_dict.keys())
        account_value = list(account_dict.values())
        name1 = self.right_bar_widget_folder_input11.text()
        index = self.model.index(0, 0)  # 调用model的index方法获取行和列对应项的索引
        data12 = index.data()
        index = self.model.index(0, 1)  # 调用model的index方法获取行和列对应项的索引
        data13 = index.data()
        index = self.model.index(0, 2)  # 调用model的index方法获取行和列对应项的索引
        data1 = index.data()
        index = self.model.index(0, 3)  # 调用model的index方法获取行和列对应项的索引
        data2 = index.data()
        index = self.model.index(0, 4)  # 调用model的index方法获取行和列对应项的索引
        data3 = index.data()
        index = self.model.index(0, 5)  # 调用model的index方法获取行和列对应项的索引
        data4 = index.data()
        index = self.model.index(0, 6)  # 调用model的index方法获取行和列对应项的索引
        data5 = index.data()
        index = self.model.index(0, 7)  # 调用model的index方法获取行和列对应项的索引
        data6 = index.data()
        index = self.model.index(0, 8)  # 调用model的index方法获取行和列对应项的索引
        data7 = index.data()
        index = self.model.index(0, 9)  # 调用model的index方法获取行和列对应项的索引
        data8 = index.data()
        index = self.model.index(0, 10)  # 调用model的index方法获取行和列对应项的索引
        data9 = index.data()
        index = self.model.index(0, 11)  # 调用model的index方法获取行和列对应项的索引
        data10 = index.data()
        index = self.model.index(0, 12)  # 调用model的index方法获取行和列对应项的索引
        data11 = index.data()
        index = self.model.index(0, 13)  # 调用model的index方法获取行和列对应项的索引
        data = index.data()
        if name1 in account_value:
          conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur1 = conn1.cursor()
          sql = "UPDATE student SET 专业='" + data1 + "' WHERE 姓名='{}'".format(name1)
          cur1.execute(sql)
          conn1.commit()
          cur1.close()
          conn1.close()
          conn2 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur2 = conn2.cursor()
          sql1 = "UPDATE student SET 班级='" + data2 + "' WHERE 姓名='{}'".format(name1)
          cur2.execute(sql1)
          conn2.commit()
          cur2.close()
          conn2.close()
          conn3 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur3 = conn3.cursor()
          sql2 = "UPDATE student SET 高级程序语言='" + data3 + "' WHERE 姓名='{}'".format(name1)
          cur3.execute(sql2)
          conn3.commit()
          cur3.close()
          conn3.close()
          conn4 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur4 = conn4.cursor()
          sql3 = "UPDATE student SET python编程='" + data4 + "' WHERE 姓名='{}'".format(name1)
          cur4.execute(sql3)
          conn4.commit()
          cur4.close()
          conn4.close()
          conn5 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur5 = conn5.cursor()
          sql4 = "UPDATE student SET 数据库原理='" + data5 + "' WHERE 姓名='{}'".format(name1)
          cur5.execute(sql4)
          conn5.commit()
          cur5.close()
          conn5.close()
          conn6 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur6 = conn6.cursor()
          sql5 = "UPDATE student SET 数据结构与算法='" + data6 + "' WHERE 姓名='{}'".format(name1)
          cur6.execute(sql5)
          conn6.commit()
          cur6.close()
          conn6.close()
          conn7 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur7 = conn7.cursor()
          sql6 = "UPDATE student SET 数学分析='" + data7 + "' WHERE 姓名='{}'".format(name1)
          cur7.execute(sql6)
          conn7.commit()
          cur7.close()
          conn7.close()
          conn8 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur8 = conn8.cursor()
          sql7 = "UPDATE student SET 高等数学='" + data8 + "' WHERE 姓名='{}'".format(name1)
          cur8.execute(sql7)
          conn8.commit()
          cur8.close()
          conn8.close()
          conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur = conn.cursor()
          sql8 = "UPDATE student SET 网络爬虫='" + data9 + "' WHERE 姓名='{}'".format(name1)
          cur.execute(sql8)
          conn.commit()
          cur.close()
          conn.close()
          conn10 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur10 = conn10.cursor()
          sql9 = "UPDATE student SET 数据可视化='" + data10 + "' WHERE 姓名='{}'".format(name1)
          cur10.execute(sql9)
          conn10.commit()
          cur10.close()
          conn10.close()
          conn11 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur11 = conn11.cursor()
          sql10 = "UPDATE student SET 数据挖掘='" + data11 + "' WHERE 姓名='{}'".format(name1)
          cur11.execute(sql10)
          conn11.commit()
          cur11.close()
          conn11.close()
          conn12 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur12 = conn12.cursor()
          sql11 = "UPDATE student SET 数据分析='" + data + "' WHERE 姓名='{}'".format(name1)
          cur12.execute(sql11)
          conn12.commit()
          cur12.close()
          conn12.close()
          conn13 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur13 = conn13.cursor()
          sql12 = "UPDATE student SET 学号='" + data12 + "' WHERE 姓名='{}'".format(name1)
          cur13.execute(sql12)
          conn13.commit()
          cur13.close()
          conn13.close()
          conn14 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
          cur14 = conn14.cursor()
          sql13 = "UPDATE student SET 姓名='" + data13 + "' WHERE 姓名='{}'".format(name1)
          cur14.execute(sql13)
          conn14.commit()
          cur14.close()
          conn14.close()
          with open("8.txt", "r") as f22:
              lines = f22.readlines()
          with open("8.txt", "w") as f_w:
              for line in lines:
                  if name1 in line:
                      f_w.write(data12+ " "+data13+'\n')
                      continue
                  f_w.write(line)
          QMessageBox.information(self, '成功', '修改成功!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif name1 in account_keys:
            conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur1 = conn1.cursor()
            sql = "UPDATE student SET 专业='" + data1 + "' WHERE 学号='{}'".format(name1)
            cur1.execute(sql)
            conn1.commit()
            cur1.close()
            conn1.close()
            conn2 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur2 = conn2.cursor()
            sql1 = "UPDATE student SET 班级='" + data2 + "' WHERE 学号='{}'".format(name1)
            cur2.execute(sql1)
            conn2.commit()
            cur2.close()
            conn2.close()
            conn3 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur3 = conn3.cursor()
            sql2 = "UPDATE student SET 高级程序语言='" + data3 + "' WHERE 学号='{}'".format(name1)
            cur3.execute(sql2)
            conn3.commit()
            cur3.close()
            conn3.close()
            conn4 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur4 = conn4.cursor()
            sql3 = "UPDATE student SET python编程='" + data4 + "' WHERE 学号='{}'".format(name1)
            cur4.execute(sql3)
            conn4.commit()
            cur4.close()
            conn4.close()
            conn5 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur5 = conn5.cursor()
            sql4 = "UPDATE student SET 数据库原理='" + data5 + "' WHERE 学号='{}'".format(name1)
            cur5.execute(sql4)
            conn5.commit()
            cur5.close()
            conn5.close()
            conn6 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur6 = conn6.cursor()
            sql5 = "UPDATE student SET 数据结构与算法='" + data6 + "' WHERE 学号='{}'".format(name1)
            cur6.execute(sql5)
            conn6.commit()
            cur6.close()
            conn6.close()
            conn7 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur7 = conn7.cursor()
            sql6 = "UPDATE student SET 数学分析='" + data7 + "' WHERE 学号='{}'".format(name1)
            cur7.execute(sql6)
            conn7.commit()
            cur7.close()
            conn7.close()
            conn8 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur8 = conn8.cursor()
            sql7 = "UPDATE student SET 高等数学='" + data8 + "' WHERE 学号='{}'".format(name1)
            cur8.execute(sql7)
            conn8.commit()
            cur8.close()
            conn8.close()
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur = conn.cursor()
            sql8 = "UPDATE student SET 网络爬虫='" + data9 + "' WHERE 学号='{}'".format(name1)
            cur.execute(sql8)
            conn.commit()
            cur.close()
            conn.close()
            conn10 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur10 = conn10.cursor()
            sql9 = "UPDATE student SET 数据可视化='" + data10 + "' WHERE 学号='{}'".format(name1)
            cur10.execute(sql9)
            conn10.commit()
            cur10.close()
            conn10.close()
            conn11 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur11 = conn11.cursor()
            sql10 = "UPDATE student SET 数据挖掘='" + data11 + "' WHERE 学号='{}'".format(name1)
            cur11.execute(sql10)
            conn11.commit()
            cur11.close()
            conn11.close()
            conn12 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur12 = conn12.cursor()
            sql11 = "UPDATE student SET 数据分析='" + data + "' WHERE 学号='{}'".format(name1)
            print(data1)
            cur12.execute(sql11)
            conn12.commit()
            cur12.close()
            conn12.close()
            conn13 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur13 = conn13.cursor()
            sql12 = "UPDATE student SET 学号='" + data12 + "' WHERE 学号='{}'".format(name1)
            cur13.execute(sql12)
            conn13.commit()
            cur13.close()
            conn13.close()
            conn14 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur14 = conn14.cursor()
            sql13 = "UPDATE student SET 姓名='" + data13 + "' WHERE 学号='{}'".format(name1)
            cur14.execute(sql13)
            conn14.commit()
            cur14.close()
            conn14.close()
            with open("8.txt", "r") as f22:
                lines = f22.readlines()
            with open("8.txt", "w") as f_w:
                for line in lines:
                    if name1 in line:
                        f_w.write(data12 + " " + data13 + '\n')
                        continue
                    f_w.write(line)
            QMessageBox.information(self, '成功', '修改成功!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
      except:
          QMessageBox.information(self, '错误', '操作错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #删除
    def view_data3(self):
        account_dict = {}
        f = open("8.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account_keys = list(account_dict.keys())
        account_value = list(account_dict.values())
        gettxt1 = self.right_bar_widget_folder_input112.text()
        if gettxt1 == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            if gettxt1 in account_keys:
                conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
                cur1 = conn1.cursor()  # 获取一个游标
                sql_select1 = "select * from student where 学号='{}'".format(gettxt1)  # 定义查询
                cur1.execute(sql_select1)  # 执行查询
                data = cur1.fetchall()  # 获取查询到数据
                query = 'insert ignore into student2(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

                for r in range(1):
                    学号 = data[0][0]
                    姓名 = data[0][1]
                    专业 = data[0][2]
                    班级 = data[0][3]
                    高级程序语言 = data[0][4]
                    python编程 = data[0][5]
                    数据库原理 = data[0][6]
                    数据结构与算法 = data[0][7]
                    数学分析 = data[0][8]
                    高等数学 = data[0][9]
                    网络爬虫 = data[0][10]
                    数据可视化 = data[0][11]
                    数据挖掘 = data[0][12]
                    数据分析 = data[0][13]
                    values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
                    # 执行sql语句
                    cur1.execute(query, values)
                conn1.commit()  # 提交事务
                cur1.close()  # 关闭游标
                conn1.close()  # 释放数据库资源在这里插入代码片

                conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
                cur = conn.cursor()  # 获取一个游标
                sql_select = "DELETE from student where 学号='{}'".format(gettxt1)  # 定义查询
                cur.execute(sql_select)  # 执行查询
                conn.commit()
                cur.close()
                conn.close()
                db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName('localhost')
                db.setDatabaseName('student')
                db.setUserName('root')
                db.setPassword('')
                if not db.open():  # 判断数据库是否打开
                    print(db.lastError().text())  # 打印操作数据库时出现的错误
                    return False
                else:
                    print("连接成功")
                    self.model = QtSql.QSqlTableModel()
                    self.right_batch_result_listView1.setModel(self.model)
                    self.model.setTable('student2')  # 设置使用数据模型的数据表
                    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                    self.model.select()  # 查询所有数据
                    with open("8.txt", "r") as f22:
                        lines = f22.readlines()
                    with open("8.txt", "w") as f_w:
                        for line in lines:
                            if gettxt1 in line:
                                continue
                            f_w.write(line)
            elif gettxt1 in account_value:
                conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
                cur1 = conn1.cursor()  # 获取一个游标
                sql_select1 = "select * from student where 姓名='{}'".format(gettxt1)  # 定义查询
                cur1.execute(sql_select1)  # 执行查询
                data = cur1.fetchall()  # 获取查询到数据
                query = 'insert ignore into student2(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

                for r in range(1):
                    学号 = data[0][0]
                    姓名 = data[0][1]
                    专业 = data[0][2]
                    班级 = data[0][3]
                    高级程序语言 = data[0][4]
                    python编程 = data[0][5]
                    数据库原理 = data[0][6]
                    数据结构与算法 = data[0][7]
                    数学分析 = data[0][8]
                    高等数学 = data[0][9]
                    网络爬虫 = data[0][10]
                    数据可视化 = data[0][11]
                    数据挖掘 = data[0][12]
                    数据分析 = data[0][13]
                    values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
                    # 执行sql语句
                    cur1.execute(query, values)
                conn1.commit()  # 提交事务
                cur1.close()  # 关闭游标
                conn1.close()  # 释放数据库资源在这里插入代码片

                conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
                cur = conn.cursor()  # 获取一个游标
                sql_select = "DELETE from student where 姓名='{}'".format(gettxt1)  # 定义查询
                cur.execute(sql_select)  # 执行查询
                conn.commit()
                cur.close()
                conn.close()
                db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName('localhost')
                db.setDatabaseName('student')
                db.setUserName('root')
                db.setPassword('')
                if not db.open():  # 判断数据库是否打开
                    print(db.lastError().text())  # 打印操作数据库时出现的错误
                    return False
                else:
                    print("连接成功")
                    self.model = QtSql.QSqlTableModel()
                    self.right_batch_result_listView1.setModel(self.model)
                    self.model.setTable('student2')  # 设置使用数据模型的数据表
                    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                    self.model.select()  # 查询所有数据
                    with open("8.txt", "r") as f22:
                        lines = f22.readlines()
                    with open("8.txt", "w") as f_w:
                        for line in lines:
                            if gettxt1 in line:
                                continue
                            f_w.write(line)
            else:
                QMessageBox.information(self, '删除错误', '不存在该学生信息', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #修改中的查询
    def view_data4(self):
        demo.view_data2()
        account_dict = {}
        f = open("8.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account_keys = list(account_dict.keys())
        account_value = list(account_dict.values())
        gettxt11 = self.right_bar_widget_folder_input11.text()
        if gettxt11 == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            if gettxt11 in account_keys:
                sql_select = "select * from student where 学号='{}'".format(gettxt11)  # 定义查询
                cur.execute(sql_select)  # 执行查询
                data = cur.fetchall()  # 获取查询到数据
                # 创建插入SQL语句
                # 获得游标
                cur = conn.cursor()
                query = 'insert ignore into student1(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
                for r in range(1):
                    学号 = data[0][0]
                    姓名 = data[0][1]
                    专业 = data[0][2]
                    班级 = data[0][3]
                    高级程序语言 = data[0][4]
                    python编程 = data[0][5]
                    数据库原理 = data[0][6]
                    数据结构与算法 = data[0][7]
                    数学分析 = data[0][8]
                    高等数学 = data[0][9]
                    网络爬虫 = data[0][10]
                    数据可视化 = data[0][11]
                    数据挖掘 = data[0][12]
                    数据分析 = data[0][13]
                    values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
                    # 执行sql语句
                    # cur.execute(query1)
                    cur.execute(query, values)
                conn.commit()  # 提交事务
                cur.close()  # 关闭游标
                conn.close()  # 释放数据库资源在这里插入代码片
                # 实例化一个可编辑数据模型
                global db
                db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName('localhost')
                db.setDatabaseName('student')
                db.setUserName('root')
                db.setPassword('')
                if not db.open():  # 判断数据库是否打开
                    print(db.lastError().text())  # 打印操作数据库时出现的错误
                    return False
                else:
                    self.model = QtSql.QSqlTableModel()
                    self.right_batch_result_listView2.setModel(self.model)
                    self.model.setTable('student1')  # 设置使用数据模型的数据表
                    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                    self.model.select()  # 查询所有数据
            elif gettxt11 in account_value:
                sql_select = "select * from student where 姓名='{}'".format(gettxt11)  # 定义查询
                cur.execute(sql_select)  # 执行查询
                data = cur.fetchall()  # 获取查询到数据
                # 创建插入SQL语句
                # 获得游标
                cur = conn.cursor()
                query = 'insert ignore into student1(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
                for r in range(1):
                    学号 = data[0][0]
                    姓名 = data[0][1]
                    专业 = data[0][2]
                    班级 = data[0][3]
                    高级程序语言 = data[0][4]
                    python编程 = data[0][5]
                    数据库原理 = data[0][6]
                    数据结构与算法 = data[0][7]
                    数学分析 = data[0][8]
                    高等数学 = data[0][9]
                    网络爬虫 = data[0][10]
                    数据可视化 = data[0][11]
                    数据挖掘 = data[0][12]
                    数据分析 = data[0][13]
                    values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
                    # 执行sql语句
                    # cur.execute(query1)
                    cur.execute(query, values)
                conn.commit()  # 提交事务
                cur.close()  # 关闭游标
                conn.close()  # 释放数据库资源在这里插入代码片
                # 实例化一个可编辑数据模型
                db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName('localhost')
                db.setDatabaseName('student')
                db.setUserName('root')
                db.setPassword('')
                if not db.open():  # 判断数据库是否打开
                    print(db.lastError().text())  # 打印操作数据库时出现的错误
                    return False
                else:
                    self.model = QtSql.QSqlTableModel()
                    self.right_batch_result_listView2.setModel(self.model)
                    self.model.setTable('student1')  # 设置使用数据模型的数据表
                    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
                    self.model.select()  # 查询所有数据
            else:
                QMessageBox.information(self, '错误', '不存在该学生信息', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #增加
    def view_data5(self):
        global db
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView3.setModel(self.model)
        self.model.setTable('student')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)

     #增加中的完成
    def view_data51(self):
      try:
        index = self.model.index(self.model.rowCount() - 1, 0)  # 调用model的index方法获取行和列对应项的索引
        data12 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 1)  # 调用model的index方法获取行和列对应项的索引
        data13 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 2)  # 调用model的index方法获取行和列对应项的索引
        data1 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 3)  # 调用model的index方法获取行和列对应项的索引
        data2 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 4)  # 调用model的index方法获取行和列对应项的索引
        data3 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 5)  # 调用model的index方法获取行和列对应项的索引
        data4 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 6)  # 调用model的index方法获取行和列对应项的索引
        data5 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 7)  # 调用model的index方法获取行和列对应项的索引
        data6 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 8)  # 调用model的index方法获取行和列对应项的索引
        data7 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 9)  # 调用model的index方法获取行和列对应项的索引
        data8 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 10)  # 调用model的index方法获取行和列对应项的索引
        data9 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 11)  # 调用model的index方法获取行和列对应项的索引
        data10 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 12)  # 调用model的index方法获取行和列对应项的索引
        data11 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 13)  # 调用model的index方法获取行和列对应项的索引
        data = index.data()
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        # 创建插入SQL语句
        query = 'insert into student(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
        学号 = data12
        姓名 = data13
        专业 = data1
        班级 = data2
        高级程序语言 = data3
        python编程 = data4
        数据库原理 = data5
        数据结构与算法 = data6
        数学分析 = data7
        高等数学 = data8
        网络爬虫 = data9
        数据可视化 = data10
        数据挖掘 = data11
        数据分析 = data
        values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
        # 执行sql语句
        cur.execute(query, values)
        cur.close()
        conn.commit()
        conn.close()
        with open('8.txt', 'a+') as f: # 注意这里a+是可写可追加
            f.write(data12 + " " +data13+'\n')
            QMessageBox.information(self, '成功', '增加成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
      except:
          QMessageBox.information(self, '错误', '操作错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #增加中查询全部
    def view_data52(self):
        try:
            global db
            # 调用输入框获取数据库名称
            db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName('localhost')
            db.setDatabaseName('student')
            db.setUserName('root')
            db.setPassword('')
            if not db.open():  # 判断数据库是否打开
                print(db.lastError().text())  # 打印操作数据库时出现的错误
                return False
            else:
                print("连接成功")
        except :
            pass
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView3.setModel(self.model)
        self.model.setTable('student')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据

     #查询增加的学生信息
    def view_data53(self):
     try:
        index = self.model.index(self.model.rowCount() - 1, 0)  # 调用model的index方法获取行和列对应项的索引
        data12 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 1)  # 调用model的index方法获取行和列对应项的索引
        data13 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 2)  # 调用model的index方法获取行和列对应项的索引
        data1 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 3)  # 调用model的index方法获取行和列对应项的索引
        data2 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 4)  # 调用model的index方法获取行和列对应项的索引
        data3 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 5)  # 调用model的index方法获取行和列对应项的索引
        data4 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 6)  # 调用model的index方法获取行和列对应项的索引
        data5 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 7)  # 调用model的index方法获取行和列对应项的索引
        data6 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 8)  # 调用model的index方法获取行和列对应项的索引
        data7 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 9)  # 调用model的index方法获取行和列对应项的索引
        data8 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 10)  # 调用model的index方法获取行和列对应项的索引
        data9 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 11)  # 调用model的index方法获取行和列对应项的索引
        data10 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 12)  # 调用model的index方法获取行和列对应项的索引
        data11 = index.data()
        index = self.model.index(self.model.rowCount() - 1, 13)  # 调用model的index方法获取行和列对应项的索引
        data = index.data()
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        # 创建插入SQL语句
        query = 'insert into student3(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
        学号 = data12
        姓名 = data13
        专业 = data1
        班级 = data2
        高级程序语言 = data3
        python编程 = data4
        数据库原理 = data5
        数据结构与算法 = data6
        数学分析 = data7
        高等数学 = data8
        网络爬虫 = data9
        数据可视化 = data10
        数据挖掘 = data11
        数据分析 = data
        values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
        # 执行sql语句
        cur.execute(query, values)
        cur.close()
        conn.commit()
        conn.close()
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView3.setModel(self.model)
        self.model.setTable('student3')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据
     except:
         db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
         db.setHostName('localhost')
         db.setDatabaseName('student')
         db.setUserName('root')
         db.setPassword('')
         self.model = QtSql.QSqlTableModel()
         self.right_batch_result_listView3.setModel(self.model)
         self.model.setTable('student3')  # 设置使用数据模型的数据表
         self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
         self.model.select()  # 查询所有数据

    #清空增加的人的信息
    def view_data54(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        query1 = 'truncate table student3;'
        cur.execute(query1)
        conn.commit()  # 提交事务
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源在这里插入代码片
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
           self.model = QtSql.QSqlTableModel()
           self.right_batch_result_listView3.setModel(self.model)
           self.model.setTable('student3')  # 设置使用数据模型的数据表
           self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
           self.model.select()  # 查询所有数据

    #成绩排名
    def view_data6(self):
     gettxt = self.right_bar_widget_folder_input114.text()
     try:
      if gettxt != '':
        conn2 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur2 = conn2.cursor()  # 获取一个游标
        sql_select1 = "create table student4(学号 varchar(100), 姓名 varchar(100), 专业 varchar(100), 班级 varchar(100), {} varchar(100))".format(
              gettxt)
        cur2.execute(sql_select1)  # 执行查询
        conn2.commit()  # 提交事务
        cur2.close()  # 关闭游标
        conn2.close()  # 释放数据库资源在这里插入代码片

        conn3 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur3 = conn3.cursor()  # 获取一个游标
        sql_select3 = "select CAST(SUM({})AS SIGNED ) from student".format(gettxt)
        cur3.execute(sql_select3)  # 执行查询
        number = cur3.fetchall()  # 获取查询到数据
        m =number[0][0]
        conn3.commit()  # 提交事务
        cur3.close()  # 关闭游标
        conn3.close()  # 释放数据库资源在这里插入代码片

        conn4 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur4 = conn4.cursor()  # 获取一个游标
        sql_select4 = "select avg(`{}`) from student".format(gettxt)
        cur4.execute(sql_select4)  # 执行查询
        number1 = cur4.fetchall()  # 获取查询到数据
        m1 = number1[0][0]
        conn4.commit()  # 提交事务
        cur4.close()  # 关闭游标
        conn4.close()  # 释放数据库资源在这里插入代码片
        self.textEdit.setText("总成绩为：" +str(m))
        self.textEdit1.setText("平均成绩：" + str(m1))
        count = 0
        f = open("8.txt", 'r+')
        for line in f:
            count = count+1
        print(count)

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        sql_select = "select student.*,@scoreNum :=@scoreNum+1 as scoreNum from student,(select @scoreNum :=0) init  ORDER BY `{}` DESC".format(gettxt)
        cur.execute(sql_select)  # 执行查询
        data = cur.fetchall()  # 获取查询到数据
        conn.commit()  # 提交事务
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源在这里插入代码片

        # 获得游标
        conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur1 = conn1.cursor()
        query = 'insert into student4(学号,姓名,专业,班级,{}) values (%s, %s, %s, %s, %s)'.format(gettxt)
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
        if gettxt == "高级程序语言":
         for r in range(0, count):
            学号 = data[r][0]
            姓名 = data[r][1]
            专业 = data[r][2]
            班级 = data[r][3]
            gettxt = data[r][4]
            values = (学号, 姓名, 专业, 班级, gettxt)
            cur1.execute(query, values)
        elif gettxt =="python编程":
            for r in range(0, count):
               学号 = data[r][0]
               姓名 = data[r][1]
               专业 = data[r][2]
               班级 = data[r][3]
               gettxt = data[r][5]
               values = (学号, 姓名, 专业, 班级, gettxt)
               cur1.execute(query, values)
        elif gettxt =="数据库原理":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][6]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt =="数据结构与算法":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][7]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt =="数学分析":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][8]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt =="高等数学":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][9]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt =="网络爬虫":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][10]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt == "数据可视化":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][11]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt == "数据挖掘":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][12]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
        elif gettxt == "数据分析":
            for r in range(0, count):
                学号 = data[r][0]
                姓名 = data[r][1]
                专业 = data[r][2]
                班级 = data[r][3]
                gettxt = data[r][13]
                values = (学号, 姓名, 专业, 班级, gettxt)
                cur1.execute(query, values)
            # 执行sql语句
        conn1.commit()  # 提交事务
        cur1.close()  # 关闭游标
        conn1.close()  # 释放数据库资源在这里插入代码片
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
            self.model = QtSql.QSqlTableModel()
            self.right_batch_result_listView4.setModel(self.model)
            self.model.setTable('student4')  # 设置使用数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model.select()  # 查询所有数据
            demo.view_data66()
      else:
         QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
     except:
         QMessageBox.information(self, '错误', '不存在该学科', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #student4的清空
    def view_data66(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        query1 = 'DROP TABLE student4'
        cur.execute(query1)
        conn.commit()  # 提交事务
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源在这里插入代码片

    #及格率统计
    def view_data7(self):
     try:
      gettxt = self.right_bar_widget_folder_input115.text()
      if gettxt != '':
        conn3 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur3 = conn3.cursor()  # 获取一个游标
        sql_select3 = "SELECT truncate(sum(`{}`>=60)/count(`学号`),2) as 及格率 FROM student ".format(gettxt)
        cur3.execute(sql_select3)  # 执行查询
        number = cur3.fetchall()  # 获取查询到数据
        m = number[0][0]
        conn3.commit()  # 提交事务
        cur3.close()  # 关闭游标
        conn3.close()  # 释放数据库资源在这里插入代码片

        conn2 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur2 = conn2.cursor()  # 获取一个游标
        sql_select2 = "SELECT truncate(sum(`{}`<60)/count(`学号`),2) as 不及格率 FROM student ".format(gettxt)
        cur2.execute(sql_select2)  # 执行查询
        number1 = cur2.fetchall()  # 获取查询到数据
        m1 = number1[0][0]
        conn2.commit()  # 提交事务
        cur2.close()  # 关闭游标
        conn2.close()  # 释放数据库资源在这里插入代码片

        conn1= pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur1 = conn1.cursor()  # 获取一个游标
        sql_select1 = 'insert into student5(学科, 及格率, 不及格率) values (%s, %s, %s)'
        学科 = gettxt
        及格率 = m
        不及格率 =m1
        values = (学科, 及格率, 不及格率)
        cur1.execute(sql_select1, values)
        conn1.commit()  # 提交事务
        cur1.close()  # 关闭游标
        conn1.close()  # 释放数据库资源在这里插入代码片

        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
            self.model = QtSql.QSqlTableModel()
            self.right_batch_result_listView5.setModel(self.model)
            self.model.setTable('student5')  # 设置使用数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model.select()  # 查询所有数据
      else:
          QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
     except:
         QMessageBox.information(self, '错误', '不存在该学科', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #student5的清空
    def view_data71(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        query1 = 'truncate table student5'
        cur.execute(query1)
        conn.commit()  # 提交事务
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源在这里插入代码片
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
            print("连接成功")
            self.model = QtSql.QSqlTableModel()
            self.right_batch_result_listView5.setModel(self.model)
            self.model.setTable('student5')  # 设置使用数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model.select()  # 查询所有数据

    #成绩分布
    def view_data8(self):
     try:
      account_dict = {}
      f = open("8.txt", 'r+')
      for line in f:
             (keys, value) = line.strip().split()
             account_dict[keys] = value
      account_keys = list(account_dict.keys())
      account_value = list(account_dict.values())
      gettxt = self.right_bar_widget_folder_input119.text()
      if gettxt !='':
       if gettxt in account_value:
        conn3 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur3 = conn3.cursor()  # 获取一个游标
        sql_select3 = ("SELECT"
                       "`学号` '学号',"
                       "`姓名` '姓名',"
                       "`专业` '专业',"
                       "`班级` '班级',"
                       "(CASE WHEN `高级程序语言` < 60 THEN '不及格' WHEN `高级程序语言` < 70 AND `高级程序语言`>=60 THEN '及格'"
                       " WHEN `高级程序语言` >= 70 AND `高级程序语言`<80 THEN"
                       "'中'"
                       "WHEN `高级程序语言` >= 80 AND `高级程序语言`<90 THEN"
                       "'良'"
                       "WHEN `高级程序语言` >= 90 AND `高级程序语言`<100 THEN"
                       "'优'"
                       "END ) AS '高级程序语言',"
                       "(CASE WHEN `python编程` < 60 THEN"
                       "'不及格'"
                       "WHEN `python编程` < 70 AND `python编程`>=60 THEN"
                       "'及格'"
                       "WHEN `python编程` >= 70 AND `python编程`<80 THEN"
                       "'中'"
                       "WHEN `python编程` >= 80 AND `python编程`<90 THEN"
                       "'良'"
                       "WHEN `python编程` >= 90 AND `python编程`<100 THEN"
                       " '优'"
                       "END ) AS 'python编程',"
                       "(CASE WHEN `数据库原理` < 60 THEN"
                       "'不及格'"
                       " WHEN `数据库原理` < 70 AND `数据库原理`>=60 THEN"
                       "'及格'"
                       " WHEN `数据库原理` >= 70 AND `数据库原理`<80 THEN"
                       " '中'"
                       " WHEN `数据库原理` >= 80 AND `数据库原理`<90 THEN"
                       " '良'"
                       "WHEN `数据库原理` >= 90 AND `数据库原理`<100 THEN"
                       " '优'"
                       " END ) AS '数据库原理',"
                       "(CASE WHEN `数据结构与算法` < 60 THEN"
                       "'不及格'"
                       " WHEN `数据结构与算法` < 70 AND `数据结构与算法`>=60 THEN"
                       "'及格'"
                       " WHEN `数据结构与算法` >= 70 AND `数据结构与算法`<80 THEN"
                       " '中'"
                       " WHEN `数据结构与算法` >= 80 AND `数据结构与算法`<90 THEN"
                       "   '良'"
                       "	WHEN `数据结构与算法` >= 90 AND `数据结构与算法`<100 THEN"
                       "'优'"
                       "END ) AS '数据结构与算法',"
                       "(CASE"
                       " WHEN `数学分析` < 60 THEN"
                       "'不及格'"
                       "WHEN `数学分析` < 70 AND `数学分析`>=60 THEN"
                       " '及格'"
                       " WHEN `数学分析` >= 70 AND `数学分析`<80 THEN"
                       "'中'"
                       " WHEN `数学分析` >= 80 AND `数学分析`<90 THEN"
                       "'良'"
                       "WHEN `数学分析` >= 90 AND `数学分析`<100 THEN"
                       "'优'"
                       "END ) AS '数学分析',"
                       "(CASE WHEN `高等数学` < 60 THEN"
                       "'不及格'"
                       "WHEN `高等数学` < 70 AND `高等数学`>=60 THEN"
                       "'及格'"
                       "WHEN `高等数学` >= 70 AND `高等数学`<80 THEN"
                       "'中'"
                       "WHEN `高等数学` >= 80 AND `高等数学`<90 THEN"
                       "'良'"
                       "WHEN `高等数学` >= 90 AND `高等数学`<100 THEN"
                       "'优'"
                       "END ) AS '高等数学',"
                       "(CASE WHEN `网络爬虫` < 60 THEN"
                       " '不及格'"
                       "WHEN `网络爬虫` < 70 AND `网络爬虫`>=60 THEN"
                       "'及格'"
                       "WHEN `网络爬虫` >= 70 AND `网络爬虫`<80 THEN"
                       " '中'"
                       "WHEN `网络爬虫` >= 80 AND `网络爬虫`<90 THEN"
                       "'良'"
                       "WHEN `网络爬虫` >= 90 AND `网络爬虫`<100 THEN"
                       "'优'"
                       "END ) AS '网络爬虫',"
                       "(CASE WHEN `数据可视化` < 60 THEN"
                       "'不及格'"
                       "WHEN `数据可视化` < 70 AND `数据可视化`>=60 THEN"
                       "'及格'"
                       "WHEN `数据可视化` >= 70 AND `数据可视化`<80 THEN"
                       "'中'"
                       "WHEN `数据可视化` >= 80 AND `数据可视化`<90 THEN"
                       "'良'"
                       "WHEN `数据可视化` >= 90 AND `数据可视化`<100 THEN"
                       "'优'"
                       " END ) AS '数据可视化',"
                       "(CASE WHEN `数据挖掘` < 60 THEN"
                       "'不及格'"
                       "WHEN `数据挖掘` < 70 AND `数据挖掘`>=60 THEN"
                       "'及格'"
                       "WHEN `数据挖掘` >= 70 AND `数据挖掘`<80 THEN"
                       " '中'"
                       "WHEN `数据挖掘` >= 80 AND `数据挖掘`<90 THEN"
                       " '良'"
                       "WHEN `数据挖掘` >= 90 AND `数据挖掘`<100 THEN"
                       " '优'"
                       " END ) AS '数据挖掘',"
                       "(CASE WHEN `数据分析` < 60 THEN"
                       "'不及格'"
                       "WHEN `数据分析` < 70 AND `数据分析`>=60 THEN"
                       "'及格'"
                       " WHEN `数据分析` >= 70 AND `数据分析`<80 THEN"
                       "'中'"
                       " WHEN `数据分析` >= 80 AND `数据分析`<90 THEN"
                       "'良'"
                       "WHEN `数据分析` >= 90 AND `数据分析`<100 THEN"
                       "'优'"
                       "END ) AS '数据分析'"
                       "FROM student WHERE `姓名` = '{}' ;").format(gettxt)
        cur3.execute(sql_select3)  # 执行查询
        number = cur3.fetchall()  # 获取查询到数据
        conn3.commit()  # 提交事务
        cur3.close()  # 关闭游标
        conn3.close()  # 释放数据库资源在这里插入代码片

        conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur1 = conn1.cursor()  # 获取一个游标
        sql_select1 = 'insert into student6(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
        学号 = number[0][0]
        姓名 = number[0][1]
        专业 = number[0][2]
        班级 = number[0][3]
        高级程序语言 = number[0][4]
        python编程 = number[0][5]
        数据库原理 = number[0][6]
        数据结构与算法 = number[0][7]
        数学分析 = number[0][8]
        高等数学 = number[0][9]
        网络爬虫 = number[0][10]
        数据可视化 = number[0][11]
        数据挖掘 = number[0][12]
        数据分析 = number[0][13]
        values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
        cur1.execute(sql_select1, values)
        conn1.commit()  # 提交事务
        cur1.close()  # 关闭游标
        conn1.close()

        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
            print("连接成功")
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView6.setModel(self.model)
        self.model.setTable('student6')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据
       elif gettxt in account_keys:
         conn3 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
         cur3 = conn3.cursor()  # 获取一个游标
         sql_select3 = ("SELECT"
                    "`学号` '学号',"
                    "`姓名` '姓名',"
                    "`专业` '专业',"
                    "`班级` '班级',"
                    "(CASE WHEN `高级程序语言` < 60 THEN '不及格' WHEN `高级程序语言` < 70 AND `高级程序语言`>=60 THEN '及格'"
                    " WHEN `高级程序语言` >= 70 AND `高级程序语言`<80 THEN"
                    "'中'"
                    "WHEN `高级程序语言` >= 80 AND `高级程序语言`<90 THEN"
                    "'良'"
                    "WHEN `高级程序语言` >= 90 AND `高级程序语言`<100 THEN"
                    "'优'"
                    "END ) AS '高级程序语言',"
                    "(CASE WHEN `python编程` < 60 THEN"
                    "'不及格'"
                    "WHEN `python编程` < 70 AND `python编程`>=60 THEN"
                    "'及格'"
                    "WHEN `python编程` >= 70 AND `python编程`<80 THEN"
                    "'中'"
                    "WHEN `python编程` >= 80 AND `python编程`<90 THEN"
                    "'良'"
                    "WHEN `python编程` >= 90 AND `python编程`<100 THEN"
                    " '优'"
                    "END ) AS 'python编程',"
                    "(CASE WHEN `数据库原理` < 60 THEN"
                    "'不及格'"
                    " WHEN `数据库原理` < 70 AND `数据库原理`>=60 THEN"
                    "'及格'"
                    " WHEN `数据库原理` >= 70 AND `数据库原理`<80 THEN"
                    " '中'"
                    " WHEN `数据库原理` >= 80 AND `数据库原理`<90 THEN"
                    " '良'"
                    "WHEN `数据库原理` >= 90 AND `数据库原理`<100 THEN"
                    " '优'"
                    " END ) AS '数据库原理',"
                    "(CASE WHEN `数据结构与算法` < 60 THEN"
                    "'不及格'"
                    " WHEN `数据结构与算法` < 70 AND `数据结构与算法`>=60 THEN"
                    "'及格'"
                    " WHEN `数据结构与算法` >= 70 AND `数据结构与算法`<80 THEN"
                    " '中'"
                    " WHEN `数据结构与算法` >= 80 AND `数据结构与算法`<90 THEN"
                    "   '良'"
                    "	WHEN `数据结构与算法` >= 90 AND `数据结构与算法`<100 THEN"
                    "'优'"
                    "END ) AS '数据结构与算法',"
                    "(CASE"
                    " WHEN `数学分析` < 60 THEN"
                    "'不及格'"
                    "WHEN `数学分析` < 70 AND `数学分析`>=60 THEN"
                    " '及格'"
                    " WHEN `数学分析` >= 70 AND `数学分析`<80 THEN"
                    "'中'"
                    " WHEN `数学分析` >= 80 AND `数学分析`<90 THEN"
                    "'良'"
                    "WHEN `数学分析` >= 90 AND `数学分析`<100 THEN"
                    "'优'"
                    "END ) AS '数学分析',"
                    "(CASE WHEN `高等数学` < 60 THEN"
                    "'不及格'"
                    "WHEN `高等数学` < 70 AND `高等数学`>=60 THEN"
                    "'及格'"
                    "WHEN `高等数学` >= 70 AND `高等数学`<80 THEN"
                    "'中'"
                    "WHEN `高等数学` >= 80 AND `高等数学`<90 THEN"
                    "'良'"
                    "WHEN `高等数学` >= 90 AND `高等数学`<100 THEN"
                    "'优'"
                    "END ) AS '高等数学',"
                    "(CASE WHEN `网络爬虫` < 60 THEN"
                    " '不及格'"
                    "WHEN `网络爬虫` < 70 AND `网络爬虫`>=60 THEN"
                    "'及格'"
                    "WHEN `网络爬虫` >= 70 AND `网络爬虫`<80 THEN"
                    " '中'"
                    "WHEN `网络爬虫` >= 80 AND `网络爬虫`<90 THEN"
                    "'良'"
                    "WHEN `网络爬虫` >= 90 AND `网络爬虫`<100 THEN"
                    "'优'"
                    "END ) AS '网络爬虫',"
                    "(CASE WHEN `数据可视化` < 60 THEN"
                    "'不及格'"
                    "WHEN `数据可视化` < 70 AND `数据可视化`>=60 THEN"
                    "'及格'"
                    "WHEN `数据可视化` >= 70 AND `数据可视化`<80 THEN"
                    "'中'"
                    "WHEN `数据可视化` >= 80 AND `数据可视化`<90 THEN"
                    "'良'"
                    "WHEN `数据可视化` >= 90 AND `数据可视化`<100 THEN"
                    "'优'"
                    " END ) AS '数据可视化',"
                    "(CASE WHEN `数据挖掘` < 60 THEN"
                    "'不及格'"
                    "WHEN `数据挖掘` < 70 AND `数据挖掘`>=60 THEN"
                    "'及格'"
                    "WHEN `数据挖掘` >= 70 AND `数据挖掘`<80 THEN"
                    " '中'"
                    "WHEN `数据挖掘` >= 80 AND `数据挖掘`<90 THEN"
                    " '良'"
                    "WHEN `数据挖掘` >= 90 AND `数据挖掘`<100 THEN"
                    " '优'"
                    " END ) AS '数据挖掘',"
                    "(CASE WHEN `数据分析` < 60 THEN"
                    "'不及格'"
                    "WHEN `数据分析` < 70 AND `数据分析`>=60 THEN"
                    "'及格'"
                    " WHEN `数据分析` >= 70 AND `数据分析`<80 THEN"
                    "'中'"
                    " WHEN `数据分析` >= 80 AND `数据分析`<90 THEN"
                    "'良'"
                    "WHEN `数据分析` >= 90 AND `数据分析`<100 THEN"
                    "'优'"
                    "END ) AS '数据分析'"
                    "FROM student WHERE `姓名` = '{}' ;").format(gettxt)
         cur3.execute(sql_select3)  # 执行查询
         number = cur3.fetchall()  # 获取查询到数据
         conn3.commit()  # 提交事务
         cur3.close()  # 关闭游标
         conn3.close()  # 释放数据库资源在这里插入代码片

         conn1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
         cur1 = conn1.cursor()  # 获取一个游标
         sql_select1 = 'insert into student6(学号,姓名,专业,班级,高级程序语言,python编程,数据库原理,数据结构与算法,数学分析,高等数学,网络爬虫,数据可视化,数据挖掘,数据分析) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
          # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
         学号 = number[0][0]
         姓名 = number[0][1]
         专业 = number[0][2]
         班级 = number[0][3]
         高级程序语言 = number[0][4]
         python编程 = number[0][5]
         数据库原理 = number[0][6]
         数据结构与算法 = number[0][7]
         数学分析 = number[0][8]
         高等数学 = number[0][9]
         网络爬虫 = number[0][10]
         数据可视化 = number[0][11]
         数据挖掘 = number[0][12]
         数据分析 = number[0][13]
         values = (学号, 姓名, 专业, 班级, 高级程序语言, python编程, 数据库原理, 数据结构与算法, 数学分析, 高等数学, 网络爬虫, 数据可视化, 数据挖掘, 数据分析)
         cur1.execute(sql_select1, values)
         conn1.commit()  # 提交事务
         cur1.close()  # 关闭游标
         conn1.close()

         db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
         db.setHostName('localhost')
         db.setDatabaseName('student')
         db.setUserName('root')
         db.setPassword('')
         if not db.open():  # 判断数据库是否打开
           print(db.lastError().text())  # 打印操作数据库时出现的错误
           return False
         else:
           print("连接成功")
           self.model = QtSql.QSqlTableModel()
           self.right_batch_result_listView6.setModel(self.model)
           self.model.setTable('student6')  # 设置使用数据模型的数据表
           self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
           self.model.select()  # 查询所有数据
       else:
           QMessageBox.information(self, '错误', '不存在该学生信息', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
     except:
         QMessageBox.information(self, '错误', '输入错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #成绩分布中的清空
    def view_data81(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='student', charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        query1 = 'truncate table student6'
        cur.execute(query1)
        conn.commit()  # 提交事务
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源在这里插入代码片
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('localhost')
        db.setDatabaseName('student')
        db.setUserName('root')
        db.setPassword('')
        if not db.open():  # 判断数据库是否打开
            print(db.lastError().text())  # 打印操作数据库时出现的错误
            return False
        else:
            print("连接成功")
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView6.setModel(self.model)
        self.model.setTable('student6')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据

    #主界面的关闭按钮
    def close1(self):
     try:
        demo.view_data2()
        demo.view_data22()
        self.close()
     except:
         self.close()


#修改密码
class myform3(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('修改密码')
        self.resize(800, 450)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./1.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QPushButton(qtawesome.icon('fa.user-secret', color='white'), " ")
        self.verticalLayout.addWidget(self.a, 2, 3, 2, 2)
        self.a.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入原有密码")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 2, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_account.setEchoMode(QLineEdit.Password)
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入新密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.a1 = QPushButton(qtawesome.icon('fa.lock', color='white'), " ")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                                   QPushButton{border:none;color:black;}
                                                   QPushButton:hover{color:white}
                                                    ''')
        self.lineEdit_password1 = QLineEdit()
        self.lineEdit_password1.setPlaceholderText("请再次输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password1, 4, 4, 1, 3)
        self.lineEdit_password1.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.a = QPushButton(qtawesome.icon('fa.lock', color='white'), " ")
        self.verticalLayout.addWidget(self.a, 4, 3, 1, 2)
        self.a.setStyleSheet('''
                                           QPushButton{border:none;color:black;}
                                           QPushButton:hover{color:white}
                                            ''')
        self.lineEdit_password1.setEchoMode(QLineEdit.Password)
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("修改")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)
        self.pushButton_quit.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        ###### 绑定按钮事件
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.pushButton_quit.clicked.connect(self.back)

    def on_pushButton_enter_clicked1(self):
        f1 = open("2.txt", 'r+')
        word = f1.readline()
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        password1 = self.lineEdit_password.text()
        password2 = self.lineEdit_password1.text()
        if account1 == account_dict[word]:
         if account1 != "" and password1 != "" and password2 != "":
            if password2 != password1:
                QMessageBox.information(self, '错误', '密码输入错误,请重新确认', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                account_dict[word] = password1
                with open('1.txt', 'w') as f4:
                    f4.write("")
                for item in account_dict.items():
                        for i in range(len(item)):
                            print(item[i], end=' ')
                            with open('1.txt', 'a') as f3:
                                f3.write(item[i]+" ")
                        with open('1.txt', 'a') as f5:
                            f5.write('\n')

                QMessageBox.information(self, '成功', '修改成功',QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
         else:
            QMessageBox.information(self, '错误', '输入不能为空' , QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '输入的密码与本账号不符', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def QCoreApplication(self):
        w3.close()

    def mini(self):
        w3.showMinimized()

    def back(self):
        w3.close()
#找回密码
class myform(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('找回密码')
        self.resize(800, 450)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./1.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'), ":")
        self.verticalLayout.addWidget(self.a, 3, 3, 2, 2)
        self.a.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 3, 4, 2, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("找回密码")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)
        self.pushButton_quit.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        ###### 绑定按钮事件
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.pushButton_quit.clicked.connect(self.back)

    def on_pushButton_enter_clicked1(self):
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        if account1 == "" :
            QMessageBox.information(self, '注册失败', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
                account_keys = list(account_dict.keys())
                if account1 not in account_keys:
                    QMessageBox.information(self, '错误', '不存在该账号', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '密码找回成功', '你的密码为：'+account_dict[account1] , QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #找回密码的关闭
    def QCoreApplication(self):
        w1.close()
    #找回密码的最小化
    def mini(self):
        w1.showMinimized()
    #返回
    def back(self):
        w1.close()
#注册账号
class myform2(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('注册账号')
        self.resize(800, 450)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./1.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'), ":")
        self.verticalLayout.addWidget(self.a, 2, 3, 1, 2)
        self.a.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.unlock-alt', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                           QPushButton{border:none;color:black;}
                                           QPushButton:hover{color:white}
                                            ''')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.a1 = QPushButton(qtawesome.icon('fa.unlock-alt', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 4, 3, 1, 2)
        self.a1.setStyleSheet('''
                                           QPushButton{border:none;color:black;}
                                           QPushButton:hover{color:white}
                                            ''')
        self.lineEdit_password1 = QLineEdit()
        self.lineEdit_password1.setPlaceholderText("请再次输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password1, 4, 4, 1, 3)
        self.lineEdit_password1.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_password1.setEchoMode(QLineEdit.Password)

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)
        self.pushButton_quit.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        ###### 绑定按钮事件
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.pushButton_quit.clicked.connect(self.back)

    def on_pushButton_enter_clicked1(self):
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        password1 = self.lineEdit_password.text()
        password2 = self.lineEdit_password1.text()
        if account1 != "" and password1 != "" and password2 != "":
            if password2 != password1:
                QMessageBox.information(self, '错误', '密码输入错误,请重新确认', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                account_keys = list(account_dict.keys())
                if account1 not in account_keys:
                    f = "1.txt"
                    with open(f, "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内
                        file.write(account1 + " " + password1 + "\n")
                    QMessageBox.information(self, '注册成功', '注册成功！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '注册失败', '账号已存在！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '注册失败', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def QCoreApplication(self):
        w2.close()
    def mini(self):
        w2.showMinimized()
    def back(self):
        w2.close()
#登录界面
class Login(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mode = mode
        self.setWindowTitle('登录界面')
        self.resize(800, 450)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./1.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.h = QPushButton("找回密码->>")
        self.verticalLayout.addWidget(self.h, 7, 5)
        self.h.setStyleSheet('''
                   QPushButton{border:none;color:black;}
                   QPushButton:hover{color:white}
                    ''')
        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'),":")
        self.verticalLayout.addWidget(self.a, 2, 3, 1 ,2)
        self.a.setStyleSheet('''
                           QPushButton{border:none;color:black;}
                           QPushButton:hover{color:white}
                            ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1,3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                        border:1px solid gray;
                        width:200px;
                        border-radius:10px;
                        padding:2px 4px;
                }''')

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.lock', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                        border:1px solid gray;
                        width:200px;
                        border-radius:10px;
                        padding:2px 4px;
                }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.checkBox_remeberpassword = QCheckBox()
        self.checkBox_remeberpassword.setText("记住密码")
        self.verticalLayout.addWidget(self.checkBox_remeberpassword, 4, 4, 1, 3)
        self.checkBox_remeberpassword.setStyleSheet(
            "QCheckBox { color : white; }; QCheckBox::indicator { color:black; }");

        self.checkBox_autologin = QtWidgets.QCheckBox()
        self.checkBox_autologin.setText("自动登录")
        self.verticalLayout.addWidget(self.checkBox_autologin, 4, 5, 1, 3)
        self.checkBox_autologin.setStyleSheet(
            "QCheckBox { color : white; }; QCheckBox::indicator { color:black; }");
        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("登录")
        self.verticalLayout.addWidget(self.pushButton_enter, 5, 4, 1, 3)
        self.pushButton_enter.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 6, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.h.clicked.connect(self.h1)

        ####初始化登录信息
        self.init_login_info()

        ####自动登录
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.goto_autologin)
        self.timer.setSingleShot(True)
        self.timer.start(1000)

    # 自动登录
    def goto_autologin(self):
        if self.checkBox_autologin.isChecked() == True and self.mode == 0:
            self.on_pushButton_enter_clicked()

    def on_pushButton_enter_clicked(self):
        # 账号判断
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        password1 = self.lineEdit_password.text()
        account_keys = list(account_dict.keys())
        f1 = "2.txt"
        with open(f1, "w") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内
            file.write(account1)
        if account1 != "" and password1 != "":

            if account1 not in account_keys:
                reply1 = QMessageBox.information(self, '登录出错', '用户不存在', QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.Yes)
            elif password1 == account_dict[account1]:
                ####### 保存登录信息
                self.save_login_info()
                # 通过验证，关闭对话框并返回1
                self.close()
                demo.show()
            else:
                QMessageBox.information(self, '登录出错', '密码错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def on_pushButton_enter_clicked1(self):
        w2.show()

    def QCoreApplication(self):
        login.close()

    def mini(self):
        login.showMinimized()

    def h1(self):
        w1.show()

    # 保存登录信息
    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("account", self.lineEdit_account.text())
        settings.setValue("password", self.lineEdit_password.text())
        settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
        settings.setValue("autologin", self.checkBox_autologin.isChecked())

    # 初始化登录信息
    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        the_account = settings.value("account")
        the_password = settings.value("password")
        the_remeberpassword = settings.value("remeberpassword")
        the_autologin = settings.value("autologin")
        ########
        self.lineEdit_account.setText(the_account)
        if the_remeberpassword == "true" or the_remeberpassword == True:
            self.checkBox_remeberpassword.setChecked(True)
            self.lineEdit_password.setText(the_password)

        if the_autologin == "true" or the_autologin == True:
            self.checkBox_autologin.setChecked(True)
#欢迎界面
def showWelcome():
    sw = root1.winfo_screenwidth()  # 获取屏幕宽度
    sh = root1.winfo_screenheight()  # 获取屏幕高度r
    root1.overrideredirect(True)  # 去除窗口边框
    root1.attributes("-alpha", 1)  # 窗口透明度（1为不透明，0为全透明）
    x = (sw - 800) / 2
    y = (sh - 450) / 2
    root1.geometry("800x450+%d+%d" % (x, y))  # 将窗口置于屏幕中央
    if os.path.exists(r'./9.gif'):  # 搜索图片文件（只能是gif格式）
        bm = PhotoImage(file=r'./9.gif')
        lb_welcomelogo = Label(root1, image=bm)  # 将图片放置于窗口
        lb_welcomelogo.bm = bm
        lb_welcomelogo.place(x=-2, y=-2, )  # 设置图片位置

def closeWelcome():
    for i in range(2):
        time.sleep(1)  # 屏幕停留时间
    root1.destroy()


if __name__ == '__main__':
    root1 = Tk()
    tMain = threading.Thread(target=showWelcome)  # 开始展示
    tMain.start()
    t1 = threading.Thread(target=closeWelcome)  # 结束展示
    t1.start()
    root1.mainloop()
    app = QtWidgets.QApplication(sys.argv)
    demo = MainUi()
    login = Login()
    w2 = myform2()
    w1 = myform()
    w3 = myform3()
    login.show()
    sys.exit(app.exec_())
