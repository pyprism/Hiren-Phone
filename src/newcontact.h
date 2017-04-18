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

    Q_PROPERTY(QString name READ name WRITE setName NOTIFY nameChanged)
    Q_PROPERTY(QString note READ note WRITE setnote NOTIFY noteChanged)
    Q_PROPERTY(QStringList phoneNumbers READ phoneNumbers WRITE setPhoneNumbers NOTIFY phoneNumbersChanged)

public:
    explicit NewContact(QWidget *parent = 0);
    ~NewContact();

    QString getName() const;
    void setName(const QString &value);

    QString getNote() const;
    void setNote(const QString &value);

    QStringList getPhoneNumbers() const;
    void setPhoneNumbers(const QStringList &value);

signals:
    void nameChanged();
    void noteChanged();
    void phoneNumbersChanged();

private:
    Ui::NewContact *ui;

    QString name;
    QString note;
    QStringList phoneNumbers;
};

#endif // NEWCONTACT_H
