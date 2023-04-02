
#include <stdio.h>


int min(int a, int b){
	return a>b?b:a;
}

int main(){
	int a,b;
//	int night;
//	int count = 1;
	scanf("%d%d", &a,&b);
	
	if(a==1){
		printf("1");
	}
	else if(a==2){
		printf("%d", min(4,(b+1)/2));
	}
	else if(b<7){
		printf("%d", min(4,b));
	}
	else{
		printf("%d", b-2);
	}
	
	
	
	
	return 0;
}
