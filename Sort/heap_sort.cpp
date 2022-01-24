#include <iostream>
using namespace std;

void print_array(double arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << "\n";
    return;
}

void max_heapify(double arr[], int i, int size)
{

    int largest = i;
    if (2 * i + 1 < size && arr[largest] < arr[2 * i + 1])
        largest = 2 * i + 1;
    if (2 * i + 2 < size && arr[largest] < arr[2 * i + 2])
        largest = 2 * i + 2;
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        max_heapify(arr, largest, size);
    }
    return;
}

void build_heap(double arr[], int size)
{
    for (int i = int(size / 2) - 1; i >= 0; i--)
        max_heapify(arr, i, size);
    return;
}

void heap_sort(double arr[], int size)
{
    build_heap(arr, size);
    for (int i = size - 1; i > 0; i--)
    {
        swap(arr[i], arr[0]);
        max_heapify(arr, 0, i);
    }
    return;
}

int main()
{
    double a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    max_heapify(a, 3, 10);
    print_array(a, 10);
    heap_sort(a, 10);
    print_array(a, 10);
    return 0;
}