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

}

void build_max_heap(int A[]){
    for (int i = HEAP_SIZE/2; i > 0; i--){
        
    }
    
}

int main(){

}