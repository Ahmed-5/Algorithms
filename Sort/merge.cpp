#include <iostream>
using namespace std;

void print_array(double arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << "\n";
    return;
}

void merge(double left[], int size_l, double right[], int size_r)
{
    double *temp = new double[size_l + size_r];
    int index_l = 0, index_r = 0, index_temp = 0;
    while (index_l < size_l || index_r < size_r)
    {
        if (index_l < size_l && index_r < size_r)
        {
            if (left[index_l] > right[index_r])
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

void merge_sort(double arr[], int size)
{
    if (size == 1)
        return;
    merge_sort(arr, int(size / 2));
    merge_sort((arr + int(size / 2)), size - int(size / 2));
    merge(arr, int(size / 2), (arr + int(size / 2)), size - int(size / 2));
    return;
}

int main()
{
    double a[] = {1, 2, 3, 4, 5, 6};
    merge_sort(a, 6);
    print_array(a, 6);
    return 0;
}