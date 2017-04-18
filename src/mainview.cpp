#include "mainview.h"
#include "ui_mainview.h"

MainView::MainView(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainView)
{
    ui->setupUi(this);
}

MainView::~MainView()
{
    delete ui;
}

void MainView::on_saveBtn_clicked()
{
    NewContact *Contact = new NewContact(this);
    Contact->show();
}

void MainView::on_searchBtn_clicked()
{
    this->hide ();

}
