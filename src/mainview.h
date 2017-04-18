#ifndef MAINVIEW_H
#define MAINVIEW_H

#include <QMainWindow>
#include <newcontact.h>

namespace Ui {
class MainView;
}

class MainView : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainView(QWidget *parent = 0);
    ~MainView();

private slots:
    void on_saveBtn_clicked();

    void on_searchBtn_clicked();

private:
    Ui::MainView *ui;
};

#endif // MAINVIEW_H
