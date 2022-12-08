#include <stdio.h>
#include <stdlib.h>

#define N_ROWS 128
#define N_COLS 8

int binsearch(char *p, int n);

int main()
{
    char *buf = NULL;
    size_t dummy = 0;
    int row, col, id_prev, id_curr;
    int ids[N_ROWS * N_COLS] = {0};

    id_prev = id_curr = 0;

    while (getline(&buf, &dummy, stdin) != EOF) {

        row = binsearch(buf, N_ROWS);
        col = binsearch((buf + 7), N_COLS);

        id_curr = row * 8 + col;
        if (id_curr > id_prev)
            id_prev = id_curr;

        ids[id_curr] = 1;             /* seat exists */
    }

    int n = 0;
    while (ids[n++] == 0)            /* skip initial missing seats */
        ;
    while (ids[n++] != 0)
        ;

    printf("highest boarding pass ID: %d\n", id_prev);
    printf("my seat ID: %d\n", n - 1);

    free(buf);

}

int binsearch(char *p, int n)
{
    int low, mid, high;

    low = 0;
    high = n - 1;

    while (low <= high) {
        mid = (high + low) / 2;
        if (*p == 'F' || *p == 'L')
            high = mid;
        else
            low = mid + 1;
        p++;
    }

    return mid;
}
