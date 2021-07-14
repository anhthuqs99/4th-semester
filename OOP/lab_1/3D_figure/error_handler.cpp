#include "error_handler.h"

#include <QMessageBox>
#include <QObject>

void error_message(errors err)
{
    if (err == NONE)
        return;
    else if (err == FILE_NOT_FOUND)
        QMessageBox::critical(NULL, "ERROR", "File Not Found!");
    else if (err == FILE_FORMAT_ERR)
        QMessageBox::critical(NULL, "ERROR", "File Format Erorr!");
    else if (err == FILE_CONTENT_ERR)
        QMessageBox::critical(NULL, "ERROR", "File Content Error!");
    else if (err == PTR_ALL_ERR)
        QMessageBox::critical(NULL, "ERROR", "Error Memory allocation!");
    else if (err == NO_DOTS)
        QMessageBox::critical(NULL, "ERROR", "No dots!");
    else if (err == NO_LINKS)
        QMessageBox::critical(NULL, "ERROR", "No Edges!");
    else if (err == UNKNOWN_COMMAND)
        QMessageBox::critical(NULL, "ERROR", "Unknown Command!");
}
