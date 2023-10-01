#include <stdio.h>


int main() {

int n;
scanf("%d", &n);
int resx=0, resy=0, resz=0;
for (int i = 0; i < n; i++) {
    int xi, yi, zi;
    scanf("%d %d %d", &xi, &yi, &zi);

    resx +=xi;
    resy +=yi;
    resz +=zi;
 }    
    if (resx==0 && resy==0 && resz==0){
    printf("YES");
    } else {
    printf("NO");
    }        
    return 0;
}

