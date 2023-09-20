#include <stdio.h>

int main() {
    int n;
    printf("n= ");
    scanf("%d", &n);

    for(int a = 2; a<n-1; a++) {
        int k=0;
        for(int i = 2; i<=a /2; i++){
            if (a%i==0){
                k++;
            }
        }
        if (k==0){
            printf("%d\n", a);
        }
    }    
    return 0;
}
