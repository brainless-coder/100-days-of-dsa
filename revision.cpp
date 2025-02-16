#include<bits/stdc++.h>
using namespace std;

void merge(vector<int> &arr, int start, int mid, int end) {
  // making the 2 array left and right
  int m = mid-start+1, n = end-mid;
  vector<int> left(m);
  for(int j = 0; j < m; ++j) left[j] = arr[start+j]; 
  vector<int> right(n);
  for(int j = 0; j < n; ++j) right[j] = arr[mid+1+j]; 

  // ab apne pas left and right subarray hai, to apan sidhe main arr me changes kar sakte hai
  int i = 0, j = 0, k = start;
  while (i < m && j < n) {
    if (left[i] <= right[j]) 
      arr[k++] = left[i++];
    else 
      arr[k++] = right[j++];
  }

  while (i < m) arr[k++] = left[i++];
  while (j < n) arr[k++] = right[j++];
}

void mergeSort(vector<int> &arr, int n, int start, int end) {
  if (start >= end) {
    return;
  }

  int mid = start + (end-start)/2;
  mergeSort(arr, n, start, mid);
  mergeSort(arr, n, mid+1, end);
  merge(arr, start, mid, end);
}

int main() {
  int n, x;
  cin >> n;
  vector<int> arr;
  for(int i = 0; i < n; ++i) {
    cin >> x;
    arr.push_back(x);
  }  

  mergeSort(arr, n, 0, n-1);

  for(auto x: arr)  cout << x << " ";
  cout << endl;

}