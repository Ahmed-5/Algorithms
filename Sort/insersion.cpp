#include <iostream>
using namespace std;

void insersion(double arr[], int size)
{
    double key;
    int j;
    for (int i = 1; i < size; i++)
    {
        key = arr[i];
        for (j = i - 1; j >= 0; j--)
        {
            if (key < arr[j])
            {
                arr[j + 1] = arr[j];
            }
            else
                break;
        }
        arr[j + 1] = key;
    }

    return;
}

int main()
{
    double a[] = {7, 6, 7, 4, 3, 2, 1};
    insersion(a, 7);
    for (int i = 0; i < 7; i++)
        cout << a[i];

    return 0;
}