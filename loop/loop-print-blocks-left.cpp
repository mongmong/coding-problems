#include <cstdio>

using namespace std;

int main()
{
    int n = 3;
    printf("n = ");
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i + 1; j++) {
            for (int k = 0; k < i + 1; k++) {
                if (k < i) {
                    printf("0-");
                } else {
                    printf("0\n");
                }
            }
        }
    }
}