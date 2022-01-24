#include <iostream>
using namespace std;

void print_array(double arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << "\n";
    return;
}

int partition(double arr[], int first, int last)
{
    if (first < last)
    {
        int key = arr[last];
        int i = first - 1, j = first;
        for (j; j < last; j++)
        {
            if (arr[j] < key)
            {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[j]);
        return i + 1;
    }
    return first;
}

void rand_selection(double arr[], int position, int size)
{
    if (size <= 1)
        return;
    int q = partition(arr, 0, size - 1);
    if (q == position)
    {
        return;
    }
    else if (q > position)
    {
        rand_selection(arr, position, q);
    }
    else
    {
        rand_selection((arr + q + 1), position - q - 1, size - q - 1);
    }
    return;
}

int main(int argc, char const *argv[])
{
    int position = 2;
    double a[] = {7, 6, 8, 4, 3, 2, 1, 5};
    rand_selection(a, position, 8);
    print_array(a, 8);
    cout << a[position] << "\n";
    return 0;
}
