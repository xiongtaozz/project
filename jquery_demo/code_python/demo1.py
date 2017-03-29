struct queue { 
int *data; 
int head; 
int tail;
};
int main(){ int num, i; printf("请输出要破译的扣扣号码长度："); scanf("%d", &num); 
struct queue q;
q.data = (int *)malloc(sizeof(int)*(num*2-1)); //总共需要的数组长度为num*2-1
q.head = 0;
q.tail = 0; 
for(i=1;i<=num;i++)
{ scanf("%d", &q.data[q.tail]);
q.tail++;
} 
printf("恭喜你啦，成功获取扣扣号码：");
while(q.head < q.tail)
{ printf("%d", q.data[q.head]);
q.head++;
q.data[q.tail] = q.data[q.head];
q.tail++;
q.head++;
} return 0;
}#下面是这个实验请输出要破译的扣扣号码长度：218916754