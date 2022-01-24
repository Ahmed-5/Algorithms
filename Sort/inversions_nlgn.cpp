#include <iostream>
using namespace std;

void print_array(double arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << "\n";
    return;
}

int merge(double left[], int size_l, double right[], int size_r)
{
    int inversions = 0;
    double *temp = new double[size_l + size_r];
    int index_l = 0, index_r = 0, index_temp = 0;
    while (index_l < size_l || index_r < size_r)
    {
        if (index_l < size_l && index_r < size_r)
        {
            if (left[index_l] > right[index_r])
            {
                temp[index_temp] = right[index_r];
                inversions += size_l - index_l;
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
    return inversions;
}

int merge_sort(double arr[], int size)
{
    int inversions = 0;
    if (size <= 1)
        return inversions;
    inversions += merge_sort(arr, int(size / 2));
    inversions += merge_sort((arr + int(size / 2)), size - int(size / 2));
    inversions += merge(arr, int(size / 2), (arr + int(size / 2)), size - int(size / 2));
    return inversions;
}

int main()
{
    double a[] = {73, 91, 63, 4, 2, 1};
    int inversions = merge_sort(a, 6);
    print_array(a, 6);
    cout << "total number of inversions is "
         << inversions << "\n";
    return 0;
}