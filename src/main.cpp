#include "mainview.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    app.setOrganizationName("Pyprism");
    app.setApplicationName("Hiren_Contact");
    app.setApplicationDisplayName("Hiren Contact");
    MainView w;
    w.show();

    return app.exec();
}
