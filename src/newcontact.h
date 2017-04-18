#ifndef NEWCONTACT_H
#define NEWCONTACT_H

#include <QDialog>

namespace Ui {
class NewContact;
}

class NewContact : public QDialog
{
    Q_OBJECT

public:
    explicit NewContact(QWidget *parent = 0);
    ~NewContact();

private:
    Ui::NewContact *ui;
};

#endif // NEWCONTACT_H
