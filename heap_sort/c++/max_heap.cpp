#include <bits/stdc++.h>

using namespace std;

int HEAP_SIZE = 10;

int left_child(int index){
    return (index<<1);
}

int right_child(int index){
    return (index<<1)+1;
}

int parent(int index){
    return index>>1;
}

void max_heapify(int A[], int index){
    int left = left_child(index);
    int right = right_child(index);
    int largest = index;
    if(left<=HEAP_SIZE && A[index]<A[left]){
        largest = left;
    }
    if(right<=HEAP_SIZE && A[largest]<A[right]){
        largest = right;
    }
    if (largest != index){
        swap(A[largest], A[index]);
        max_heapify(A, largest);
    }
}

void build_max_heap(int A[]){
    for (int i = HEAP_SIZE/2; i > 0; i--){
        max_heapify(A, i);
    }
}

void heapsort(int A[]){
    for (int i = 0; i < 10; i++){
        swap(A[HEAP_SIZE], A[1]);
        HEAP_SIZE--;
        max_heapify(A, 1);
    }
}

int main(){
    int A[] = {-999, 4, 9, 1, 2, 0, 5, 7, 3, 8, 6};
    build_max_heap(A);
    heapsort(A);
    for (size_t i = 0; i < 11; i++){
        cout << A[i] << " ";
    }
    cout << endl;
}