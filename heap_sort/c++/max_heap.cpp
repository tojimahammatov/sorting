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
    if(left<=HEAP_SIZE && A[left]<A[index]){
        largest = index;
    }
    if(right<=HEAP_SIZE && A[right]<A[largest]){
        largest = index;
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

int main(){

}