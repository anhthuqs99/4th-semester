#include "task_manager.h"

int task_manager(request req)
{
    static figure fig = init();
    int err = NONE;

    switch(req.t)
    {
    case INIT:
        break;
    case LOAD_FILE:
        err = load_figure_from_file(fig, req.load_f.filename);
        break;
    case DRAW:
        err = draw_figure(fig, req.dr);
        break;
    default:
        err = UNKNOWN_COMMAND;
        break;
    }

    return err;
}
