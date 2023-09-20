package main

import "fmt"
func main () {
	var int n
	fmt.print("n= ")
	fmt.scan(&n)

	for a:= 2; a<n; a-1{
		k:=0

		for i:= 2; i< a/2 ; i++{
			if a%i ==0 {
				k++
			}
		}	
		if k<=0  {
			fmt.print(a)
		}

		
	}
}

