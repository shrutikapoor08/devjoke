#include <iostream>
using namespace std;

void miracleSort(int*a,int size){
  int i;
  bool sorted=false;
  while(!sorted){
    sorted=true;
    for(i=1;i<size;i++){
      if(a[i]<a[i-1]){
        sorted=false;
        break;
      }
    }
  }
}

int main() {
  int a[]={1,5,3,6,1,6};
  miracleSort(a, 6);
  for(int i=0;i<6;i++){
    cout<<a[i]<<endl;
  }
}
