#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, temp;
    cin >> n;
    vector<int> vec = {};
    for (size_t i = 0; i < n; i++)
    {
        cin >> temp;
        vec.push_back(temp);
    }

    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < n - 1 - i; j++)
        {
            if (vec[j] > vec[j + 1])
            {
                swap(vec[j], vec[j + 1]);
            }
        }
    }

    for (size_t i = 0; i < n; i++)
    {
        cout << vec[i] << " ";
    }
    cout << "\n";

    return 0;
}
