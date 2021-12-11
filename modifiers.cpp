#include <iostream>
using namespace std;

int main()
{

    unsigned int a = 2147483645;

    for (int i = 0; i < 5; i++, a++)
        cout << a << endl;

    return 0;
}