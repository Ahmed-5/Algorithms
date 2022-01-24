#include <iostream>
#include <math.h>
using namespace std;

struct point
{
    int x, y;
};

void print_point(point p)
{
    cout << p.x << " " << p.y << "\n";
    return;
}

void print_points(point arr[], int size)
{
    for (int i = 0; i < size; i++)
        print_point(arr[i]);
    return;
}

void merge(point left[], int size_l, point right[], int size_r)
{
    point *temp = new point[size_l + size_r];
    int index_l = 0, index_r = 0, index_temp = 0;
    while (index_l < size_l || index_r < size_r)
    {
        if (index_l < size_l && index_r < size_r)
        {
            if (left[index_l].x > right[index_r].x)
            {
                temp[index_temp] = right[index_r];
                index_r++;
                index_temp++;
            }
            else if (((left[index_l].x == right[index_r].x) && (left[index_l].y > right[index_r].y)))
            {
                temp[index_temp] = right[index_r];
                index_r++;
                index_temp++;
            }
            else
            {
                temp[index_temp] = left[index_l];
                index_l++;
                index_temp++;
            }
        }
        else if (index_l >= size_l)
        {
            for (index_r; index_r < size_r; index_r++)
            {
                temp[index_temp] = right[index_r];
                index_temp++;
            }
        }
        else
        {
            for (index_l; index_l < size_l; index_l++)
            {
                temp[index_temp] = left[index_l];
                index_temp++;
            }
        }
    }
    // copies the temp sorted array to the original array
    index_temp = 0;
    for (index_l = 0; index_l < size_l; index_l++)
    {
        left[index_l] = temp[index_temp];
        index_temp++;
    }
    for (index_r = 0; index_r < size_r; index_r++)
    {
        right[index_r] = temp[index_temp];
        index_temp++;
    }
    return;
}

void merge_sort(point arr[], int size)
{
    if (size == 1)
        return;
    merge_sort(arr, int(size / 2));
    merge_sort((arr + int(size / 2)), size - int(size / 2));
    merge(arr, int(size / 2), (arr + int(size / 2)), size - int(size / 2));
    return;
}

double euclidean_dist(point a, point b)
{
    return sqrt(pow((a.x - b.x), 2) + pow((a.y - b.y), 2));
}

point *closest_pairs_2d(point *arr, int size)
{
    if (size < 2)
    {
        return nullptr;
    }

    if (size == 2)
    {
        return arr;
    }
    point *closest = new point[2];
    double dist = INFINITY, temp;
    if (size == 3)
    {
        for (int i = 0; i < size - 1; i++)
        {
            for (int j = i + 1; j < size; j++)
            {
                temp = euclidean_dist(arr[i], arr[j]);
                if (temp < dist)
                {
                    dist = temp;
                    closest[0] = arr[i];
                    closest[1] = arr[j];
                }
            }
        }
        return closest;
    }

    point *pair_left = closest_pairs_2d(arr, int(size / 2));
    point *pair_right = closest_pairs_2d((arr + int(size / 2)), size - int(size / 2));
    dist = euclidean_dist(pair_left[0], pair_left[1]);
    closest = pair_left;
    temp = euclidean_dist(pair_right[0], pair_right[1]);
    if (temp < dist)
    {
        dist = temp;
        closest = pair_right;
    }
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < min(8, size - i); j++)
        {
            temp = euclidean_dist(arr[i], arr[j + i + 1]);
            if (temp < dist)
            {
                dist = temp;
                closest[0] = arr[i];
                closest[1] = arr[j + i + 1];
            }
        }
    }
    return closest;
}

int main()
{
    int n = 6;
    point *a = new point[n];
    for (int i = 0; i < n; i++)
    {
        point p = {i * i - 6 * i + 9, i * i};
        a[i] = p;
    }
    merge_sort(a, n);
    print_points(a, n);
    cout << "\n";

    point *c = new point[2];
    c = closest_pairs_2d(a, n);
    print_points(c, 2);
    cout << euclidean_dist(c[0], c[1]) << "\n";

    return 0;
}