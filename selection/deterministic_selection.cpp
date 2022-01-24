#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

void print_array(double arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << "\n";
    return;
}

double find_median(double arr[], int size, bool do_sort)
{
    if (do_sort)
    {
        sort(arr, arr + size);
    }
    if (size % 2 == 0)
    {
        return (arr[int(size / 2) - 1] + arr[int(size / 2)]) / 2;
    }
    else
    {
        return arr[int(size / 2)];
    }
}

int partition(double arr[], int first, int last, double key)
{
    if (first < last)
    {
        int i = first - 1, j = first;
        for (j; j < last; j++)
        {
            if (arr[j] <= key)
            {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        return i;
    }
    return first;
}

double determin_selection(double arr[], int position, int size)
{
    if (size <= 1)
        return arr[0];

    int med_size = ceil(double(size) / 5);
    double *medians = new double[med_size];
    for (int i = 0; i < med_size; i++)
    {
        medians[i] = find_median(arr + i * 5, min(5, size - 5 * i), true);
    }

    double key = determin_selection(medians, int((med_size - 1) / 2), med_size);

    int q = partition(arr, 0, size, key);
    if (q == position)
    {
        return arr[q];
    }
    else if (q > position)
    {
        determin_selection(arr, position, q);
    }
    else
    {
        determin_selection((arr + q + 1), position - q - 1, size - q - 1);
    }
    return arr[position];
}

int main(int argc, char const *argv[])
{
    int position = 7;
    double a[] = {7, 6, 8, 4, 3, 2, 1, 5};
    determin_selection(a, position, 8);
    print_array(a, 8);
    cout << a[position] << "\n";
    return 0;
}
