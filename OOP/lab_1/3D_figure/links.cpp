#include "links.h"

int links_alloc(links_data &connections, int len)
{
    connections.n = len;
    connections.arr = (link*) calloc(len, sizeof(link));
    if (!connections.arr)
        return PTR_ALL_ERR;
    return NONE;
}

void links_free(links_data &connection)
{
    if (connection.arr)
        free(connection.arr);
}

int read_link(link* joints, FILE *f)
{
    if (fscanf(f, "%d%d", &joints->p1, &joints->p2) != 2)
        return FILE_FORMAT_ERR;

    return NONE;
}

int read_n_links(link* joints, int n, FILE *f)
{
    int err = NONE;
    for (int i = 0; i < n; i++)
    {
        if (read_link(&joints[i], f))
            err = FILE_FORMAT_ERR;
    }

    return err;
}

int process_links(links_data& connections, FILE *f)
{
    int n;
    int err = NONE;

    err = read_amount(&n, f);
    if (err != NONE)
    {
        if (n > 0)
            err = links_alloc(connections, n);
        else
            err = NO_LINKS;

        if (err == NONE)
        {
            if ((err = read_n_links(connections.arr, n, f)) == FILE_FORMAT_ERR)
                links_free(connections);
        }
    }

    return err;
}
