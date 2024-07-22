#include <iostream>
using namespace std;

void printTenStars();
int main() {
    // 여기에 코드를 작성해주세요.
    for(int i=0;i<5;i++)
    {
        printTenStars();
    }
    return 0;
}
void printTenStars()
{
    cout << "**********"<<'\n';
}