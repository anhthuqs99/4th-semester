#ifndef DRAWING_H
#define DRAWING_H

#include <QGraphicsView>
#include "point.h"
#include "links.h"
#include "graph.h"
#include <math.h>

struct draw
{
    QGraphicsView *gV;
    int w;
    int h;
};

struct coord_point
{
    int x;
    int y;
};

coord_point get_dot(point* dots, int n);
coord_point point_transform(coord_point dot, draw arg);
void draw_line(coord_point p1, coord_point p2, graphics a, draw arg);
void draw_links(points_data pts, links_data links, draw arg, graphics a);

#endif // DRAWING_H
