#ifndef FIGURE_H
#define FIGURE_H

#include "point.h"
#include "links.h"
#include "error_handler.h"
#include "drawing.h"
#include "operation.h"

struct figure
{
    points_data points;
    links_data links;
};

figure& init();
void empty_figure(figure& fig);
void copy_figure(figure& fig, figure& tmp);
int load_figure_from_file(figure& fig, const char *filename);

int draw_figure(figure &fig, draw arg);

#endif // FIGURE_H
