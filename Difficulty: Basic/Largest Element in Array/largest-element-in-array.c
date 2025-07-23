int largest(int arr[], int n) {
    // Code Here
    int res = arr[0];
    for(int i=1;i<n;i++){
        if(arr[i] > res){
            res = arr[i];
        }
    }
    return res;
}