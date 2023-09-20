#include <iostream>

int main() {
    int n;
    std::cout<<"n= ";
    std::cin >> n;

    for(int a = 2; a<n; a++) {
        int k=0;
        for(int i = 2; i<=a /2; i++){
            if (a%i==0){
                k++;
            }
        }
        if (k==0){
	std::cout << a << std::endl;
        }
    }    
    return 0;
}
