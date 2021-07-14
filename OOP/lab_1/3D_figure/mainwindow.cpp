#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    request req;
    req.t = INIT;
    task_manager(req);
}

MainWindow::~MainWindow()
{
    delete ui;
}

errors draw_action(Ui::MainWindow *ui)
{
    draw dr;
    dr.gV = ui->graphicsView;
    dr.h = ui->graphicsView->height();
    dr.w = ui->graphicsView->width();

    request req;
    req.t = DRAW;
    req.dr = dr;

    errors err = (errors) task_manager(req);

    return  err;
}

errors transform_and_show(request req, Ui::MainWindow *ui)
{
    errors err = (errors) task_manager(req);
    if (err == NONE)
        err = draw_action(ui);

    return err;
}

void MainWindow::on_button_Move_clicked()
{

}

void MainWindow::on_button_Scale_clicked()
{

}

void MainWindow::on_button_Turn_clicked()
{

}

void MainWindow::on_button_Open_clicked()
{
    request req;
    req.t = LOAD_FILE;
    req.load_f.filename = "cube."
                          "txt";

    errors err = transform_and_show(req, ui);

    error_message(err);
}

