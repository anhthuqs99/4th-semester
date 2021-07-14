/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGraphicsView *graphicsView;
    QGroupBox *group_Move;
    QPushButton *button_Move;
    QLabel *label_MoveX;
    QLabel *label_MoveY;
    QLabel *label_MoveZ;
    QLineEdit *lineEdit_MoveX;
    QLineEdit *lineEdit_MoveZ;
    QLineEdit *lineEdit_MoveY;
    QGroupBox *group_Scale;
    QPushButton *button_Scale;
    QLabel *label_ScaleX;
    QLabel *label_ScaleY;
    QLabel *label_ScaleZ;
    QLineEdit *lineEdit_ScaleX;
    QLineEdit *lineEdit_ScaleY;
    QLineEdit *lineEdit_ScaleZ;
    QGroupBox *group_Turn;
    QPushButton *button_Turn;
    QLabel *label_TurnX;
    QLabel *label_TurnY;
    QLabel *label_TurnZ;
    QLineEdit *lineEdit_TurnX;
    QLineEdit *lineEdit_TurnY;
    QLineEdit *lineEdit_TurnZ;
    QPushButton *button_Open;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(830, 600);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setGeometry(QRect(20, 20, 500, 500));
        group_Move = new QGroupBox(centralWidget);
        group_Move->setObjectName(QString::fromUtf8("group_Move"));
        group_Move->setGeometry(QRect(550, 10, 250, 150));
        button_Move = new QPushButton(group_Move);
        button_Move->setObjectName(QString::fromUtf8("button_Move"));
        button_Move->setGeometry(QRect(80, 100, 91, 31));
        label_MoveX = new QLabel(group_Move);
        label_MoveX->setObjectName(QString::fromUtf8("label_MoveX"));
        label_MoveX->setGeometry(QRect(20, 30, 21, 16));
        label_MoveY = new QLabel(group_Move);
        label_MoveY->setObjectName(QString::fromUtf8("label_MoveY"));
        label_MoveY->setGeometry(QRect(100, 30, 21, 16));
        label_MoveZ = new QLabel(group_Move);
        label_MoveZ->setObjectName(QString::fromUtf8("label_MoveZ"));
        label_MoveZ->setGeometry(QRect(190, 30, 21, 16));
        lineEdit_MoveX = new QLineEdit(group_Move);
        lineEdit_MoveX->setObjectName(QString::fromUtf8("lineEdit_MoveX"));
        lineEdit_MoveX->setGeometry(QRect(20, 50, 31, 20));
        lineEdit_MoveZ = new QLineEdit(group_Move);
        lineEdit_MoveZ->setObjectName(QString::fromUtf8("lineEdit_MoveZ"));
        lineEdit_MoveZ->setGeometry(QRect(190, 50, 31, 20));
        lineEdit_MoveY = new QLineEdit(group_Move);
        lineEdit_MoveY->setObjectName(QString::fromUtf8("lineEdit_MoveY"));
        lineEdit_MoveY->setGeometry(QRect(100, 50, 31, 20));
        group_Scale = new QGroupBox(centralWidget);
        group_Scale->setObjectName(QString::fromUtf8("group_Scale"));
        group_Scale->setGeometry(QRect(550, 180, 250, 150));
        button_Scale = new QPushButton(group_Scale);
        button_Scale->setObjectName(QString::fromUtf8("button_Scale"));
        button_Scale->setGeometry(QRect(80, 100, 91, 31));
        label_ScaleX = new QLabel(group_Scale);
        label_ScaleX->setObjectName(QString::fromUtf8("label_ScaleX"));
        label_ScaleX->setGeometry(QRect(20, 30, 21, 16));
        label_ScaleY = new QLabel(group_Scale);
        label_ScaleY->setObjectName(QString::fromUtf8("label_ScaleY"));
        label_ScaleY->setGeometry(QRect(110, 30, 21, 16));
        label_ScaleZ = new QLabel(group_Scale);
        label_ScaleZ->setObjectName(QString::fromUtf8("label_ScaleZ"));
        label_ScaleZ->setGeometry(QRect(190, 30, 21, 16));
        lineEdit_ScaleX = new QLineEdit(group_Scale);
        lineEdit_ScaleX->setObjectName(QString::fromUtf8("lineEdit_ScaleX"));
        lineEdit_ScaleX->setGeometry(QRect(20, 50, 31, 20));
        lineEdit_ScaleY = new QLineEdit(group_Scale);
        lineEdit_ScaleY->setObjectName(QString::fromUtf8("lineEdit_ScaleY"));
        lineEdit_ScaleY->setGeometry(QRect(190, 50, 31, 20));
        lineEdit_ScaleZ = new QLineEdit(group_Scale);
        lineEdit_ScaleZ->setObjectName(QString::fromUtf8("lineEdit_ScaleZ"));
        lineEdit_ScaleZ->setGeometry(QRect(110, 50, 31, 20));
        group_Turn = new QGroupBox(centralWidget);
        group_Turn->setObjectName(QString::fromUtf8("group_Turn"));
        group_Turn->setGeometry(QRect(550, 340, 250, 150));
        button_Turn = new QPushButton(group_Turn);
        button_Turn->setObjectName(QString::fromUtf8("button_Turn"));
        button_Turn->setGeometry(QRect(80, 100, 91, 31));
        label_TurnX = new QLabel(group_Turn);
        label_TurnX->setObjectName(QString::fromUtf8("label_TurnX"));
        label_TurnX->setGeometry(QRect(20, 30, 21, 16));
        label_TurnY = new QLabel(group_Turn);
        label_TurnY->setObjectName(QString::fromUtf8("label_TurnY"));
        label_TurnY->setGeometry(QRect(110, 30, 21, 16));
        label_TurnZ = new QLabel(group_Turn);
        label_TurnZ->setObjectName(QString::fromUtf8("label_TurnZ"));
        label_TurnZ->setGeometry(QRect(190, 30, 21, 16));
        lineEdit_TurnX = new QLineEdit(group_Turn);
        lineEdit_TurnX->setObjectName(QString::fromUtf8("lineEdit_TurnX"));
        lineEdit_TurnX->setGeometry(QRect(20, 50, 31, 20));
        lineEdit_TurnY = new QLineEdit(group_Turn);
        lineEdit_TurnY->setObjectName(QString::fromUtf8("lineEdit_TurnY"));
        lineEdit_TurnY->setGeometry(QRect(190, 50, 31, 20));
        lineEdit_TurnZ = new QLineEdit(group_Turn);
        lineEdit_TurnZ->setObjectName(QString::fromUtf8("lineEdit_TurnZ"));
        lineEdit_TurnZ->setGeometry(QRect(110, 50, 31, 20));
        button_Open = new QPushButton(centralWidget);
        button_Open->setObjectName(QString::fromUtf8("button_Open"));
        button_Open->setGeometry(QRect(610, 500, 121, 31));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 830, 17));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        MainWindow->insertToolBarBreak(mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        group_Move->setTitle(QApplication::translate("MainWindow", "Move", nullptr));
        button_Move->setText(QApplication::translate("MainWindow", "Move", nullptr));
        label_MoveX->setText(QApplication::translate("MainWindow", "x:", nullptr));
        label_MoveY->setText(QApplication::translate("MainWindow", "y:", nullptr));
        label_MoveZ->setText(QApplication::translate("MainWindow", "z:", nullptr));
        lineEdit_MoveX->setText(QApplication::translate("MainWindow", "0", nullptr));
        lineEdit_MoveZ->setText(QApplication::translate("MainWindow", "0", nullptr));
        lineEdit_MoveY->setText(QApplication::translate("MainWindow", "0", nullptr));
        group_Scale->setTitle(QApplication::translate("MainWindow", "Scale", nullptr));
        button_Scale->setText(QApplication::translate("MainWindow", "Scale", nullptr));
        label_ScaleX->setText(QApplication::translate("MainWindow", "x:", nullptr));
        label_ScaleY->setText(QApplication::translate("MainWindow", "y:", nullptr));
        label_ScaleZ->setText(QApplication::translate("MainWindow", "z:", nullptr));
        lineEdit_ScaleX->setText(QApplication::translate("MainWindow", "0", nullptr));
        lineEdit_ScaleY->setText(QApplication::translate("MainWindow", "0", nullptr));
        lineEdit_ScaleZ->setText(QApplication::translate("MainWindow", "0", nullptr));
        group_Turn->setTitle(QApplication::translate("MainWindow", "Turn", nullptr));
        button_Turn->setText(QApplication::translate("MainWindow", "Turn", nullptr));
        label_TurnX->setText(QApplication::translate("MainWindow", "x:", nullptr));
        label_TurnY->setText(QApplication::translate("MainWindow", "y:", nullptr));
        label_TurnZ->setText(QApplication::translate("MainWindow", "z:", nullptr));
        lineEdit_TurnX->setText(QApplication::translate("MainWindow", "0", nullptr));
        lineEdit_TurnY->setText(QApplication::translate("MainWindow", "0", nullptr));
        lineEdit_TurnZ->setText(QApplication::translate("MainWindow", "0", nullptr));
        button_Open->setText(QApplication::translate("MainWindow", "Open", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
