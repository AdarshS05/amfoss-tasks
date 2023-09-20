package main

import "fmt"

func main () {
	var n int 
	fmt.Print("n= ")
	fmt.Scan(&n)
	
	for a:= 2; a<n; a++{
		k:=0
		for i:=2; i<a/2; i++ {
			if a%i==0{
				k++
			}
		}
		if k<=0{
			fmt.Println(a)
		}
	}
}
			
	
