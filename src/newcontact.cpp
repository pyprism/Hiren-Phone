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

QStringList NewContact::getPhoneNumbers() const
{
    return phoneNumbers;
}

void NewContact::setPhoneNumbers(const QStringList &value)
{
    if ( phoneNumbers != value) {
        phoneNumbers = value;
        emit phoneNumbersChanged ();
    }

}

