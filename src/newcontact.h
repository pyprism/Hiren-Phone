#ifndef NEWCONTACT_H
#define NEWCONTACT_H

#include <QDialog>
#include <QString>
#include <QStringList>

namespace Ui {
class NewContact;
}

class NewContact : public QDialog
{
    Q_OBJECT

public:
    explicit NewContact(QWidget *parent = 0);
    ~NewContact();

    QString getName() const;
    void setName(const QString &value);

    QString getNumber() const;
    void setNumber(const QString &value);

    QString getNote() const;
    void setNote(const QString &value);

    QStringList getPhonebook() const;
    void setPhonebook(const QStringList &value);

signals:
    void nameChanged();
    void numberChanged();
    void noteChanged();
    void phonebookChanged();

private:
    Ui::NewContact *ui;

    QString name;
    QString number;
    QString note;
    QStringList phonebook;
};

#endif // NEWCONTACT_H
