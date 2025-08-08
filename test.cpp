#include <iostream>
using namespace std;
int main()
{
    int arr[5] = {4, 3, 1, 5, 5};

    int largest = arr[0], s_largest = -22;

    for (int i = 0; i < 5; i++)
    {
        if (largest < arr[i])
        {
            s_largest = largest;
            largest = arr[i];
        }
        else if (s_largest > arr[i])
        {
            s_largest = arr[i];
        }
    }

    cout << "The largest element is : " << largest << endl;
    cout << "The Second largest element is : " << s_largest << endl;

    return 0;
}