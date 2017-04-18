#include "newcontact.h"
#include "ui_newcontact.h"

NewContact::NewContact(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::NewContact)
{
    ui->setupUi(this);
}

NewContact::~NewContact()
{
    delete ui;
}

QString NewContact::getName() const
{
    return name;
}

void NewContact::setName(const QString &value)
{
    if (name != value) {
        name = value;
        emit nameChanged();
    }

}

QString NewContact::getNumber() const
{
    return number;
}

void NewContact::setNumber(const QString &value)
{
    if (number != value ) {
        number = value;
        emit numberChanged ();
    }
}

QString NewContact::getNote() const
{
    return note;
}

void NewContact::setNote(const QString &value)
{
    if ( note != value){
        note = value;
        emit noteChanged ();
    }

}

QStringList NewContact::getPhonebook() const
{
    return phonebook;
}

void NewContact::setPhonebook(const QStringList &value)
{
    if (phonebook != value){
        phonebook = value;
        emit phonebookChanged ();
    }

}
