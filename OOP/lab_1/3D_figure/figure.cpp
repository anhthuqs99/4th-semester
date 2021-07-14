#include "figure.h"
#include "drawing.h"
#include "error_handler.h"
#include "point.h"
#include "links.h"
#include "graph.h"
#include "operation.h"

figure& init()
{
    static figure fig;

    fig.points.n = 0;
    fig.points.arr = NULL;

    fig.links.n = 0;
    fig.links.arr = NULL;

    return fig;
}

void empty_figure(figure& fig)
{
    fig.points.n = 0;
    points_free(fig.points);

    fig.links.n = 0;
    links_free(fig.links);
}

void copy_figure(figure& fig, figure& tmp)
{
    fig.points.n = tmp.points.n;
    fig.points.arr = tmp.points.arr;

    fig.links.n = tmp.links.n;
    fig.links.arr = tmp.links.arr;
}

int load_figure_from_file(figure& fig, const char *filename)
{
    FILE *f = fopen(filename, "r");
    if (!f)
        return FILE_NOT_FOUND;

    figure fig_tmp = init();

    int err = process_points(fig_tmp.points, f);

    if (err == NONE)
    {
        err = process_links(fig_tmp.links, f);
        if (err != NONE)
            points_free(fig_tmp.points);
    }

    if (err == NONE)
    {
        empty_figure(fig);
        copy_figure(fig, fig_tmp);
    }
    fclose(f);

    return err;
}

int draw_figure(figure &fig, draw arg)
{
    graphics a;
    int err = init_graph(a, arg.gV);

    if (err == NONE)
    {
        draw_links(fig.points, fig.links, arg, a);
        a.scene->setSceneRect(QRectF(QPointF(0, 0), QSizeF(arg.w, arg.h)));
        set(arg.gV, a);
    }

    return err;
}

