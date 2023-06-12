package main

import (
	"fmt"
	"gonum.org/v1/gonum/mat"
)

func main() {
	// create a 4 x 4 matrix
	data := []float64{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
	a := mat.NewDense(4, 4, data)

	var svd mat.SVD
	ok := svd.Factorize(a, mat.SVDThin)
	if !ok {
		fmt.Println("SVD factorization failed")
		return
	}

	var u, v mat.Dense
	svd.UTo(&u)
	svd.VTo(&v)
	s := svd.Values(nil)

	fmt.Println("U = ")
	matPrint(&u)

	fmt.Println("\nΣ = ")
	fmt.Printf("%v\n", s)

	fmt.Println("\nV = ")
	matPrint(&v)
}

func matPrint(X mat.Matrix) {
	fa := mat.Formatted(X, mat.Prefix(""), mat.Squeeze())
	fmt.Printf("%v\n", fa)
}
