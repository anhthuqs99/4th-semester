#ifndef OPERATION_H
#define OPERATION_H

#include "point.h"
#include "links.h"
#include "drawing.h"
#include "figure.h"

struct move
{
    int dx;
    int dy;
    int dz;
};

struct scale
{
    double kx;
    double ky;
    double kz;
};

struct turn
{
    int ox;
    int oy;
    int oz;
};

#endif // OPERATION_H
