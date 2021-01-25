// merge sort implementation

#include <bits/stdc++.h>

using namespace std;

vector<int> merge(vector<int> left, vector<int> right){
    vector<int> merged;
    while (left.size()>0 && right.size()>0){
        if(left[0]<=right[0]){
            merged.push_back(left[0]);
            left.erase(left.begin());
        }else{
            merged.push_back(right[0]);
            right.erase(right.begin());
        }
    }
    if(left.size()>0){
        merged.insert(merged.end(), left.begin(), left.end());
    }
    if(right.size()>0){
        merged.insert(merged.end(), right.begin(), right.end());
    }
    return merged;
}


vector<int> mergesort(vector<int> A){
    int arr_size = A.size();
    if (arr_size == 1){
        return A;
    }
    int middle = (arr_size + 1) / 2;
    vector<int> left;
    left.insert(left.end(), A.begin(), A.begin()+middle);
    
    vector<int> right;
    right.insert(right.end(), A.begin()+middle, A.end());

    left = mergesort(left);
    right = mergesort(right);

    return merge(left, right);
}

int main(){

    vector<int> A = {1, 14, 5, 6, 9, 4, 2};

    vector<int> sorted_A = mergesort(A);

    for (size_t i = 0; i < sorted_A.size(); i++){
        cout << sorted_A[i] << ' ';
    }
    cout << endl;
}