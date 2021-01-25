/*
    quicksort implementation
    1. partition function
    2. quicksort function

    Time complexity, Worst-case ==>> O(n^2)
                Average-Expected ==>> O(n*logn)
    Space complexity, Big O ==>> O(1), in-place algorithm
*/ 

#include <bits/stdc++.h>

using namespace std;

int partition(int A[], int p, int r){
    int pivot = A[r];
    int i = p-1;
    for (int j = p; j < r; j++){
        if(A[j]<pivot){
            i++;
            swap(A[j], A[i]);
        }
    }
    swap(A[i+1], A[r]);
    return i+1;
}

void quicksort(int A[], int p, int r){
    if(p<r){
        int q = partition(A, p, r);
        quicksort(A, p, q-1);
        quicksort(A, q+1, r);
    }
}

int main(){
    // example of usage
    // let's take the following an array
    int A[] = {6, 4, 1, 23, 46, -3, 12};
    // calculate its length
    int array_size = sizeof(A)/sizeof(A[0]);
    // apply quicksort
    quicksort(A, 0, array_size - 1);
    // check the result
    for (size_t i = 0; i < array_size; i++){
        cout << A[i] << " ";
    }
    cout << endl;
}
