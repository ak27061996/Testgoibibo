//Coding: Provide implementation of a circular linked list

#include<bits/stdc++.h>
using namespace std;
typedef struct Node
{
	int info;
	struct Node *next;
}node;

//Global defined
node *front=NULL,*rear=NULL,*temp;

void create(int x)
{
	node *newnode;
	newnode=(node*)malloc(sizeof(node));
	newnode->info=x;
	newnode->next=NULL;
	if(rear==NULL)
	front=rear=newnode;
	else
	{
		rear->next=newnode;
		rear=newnode;
	}
	
	rear->next=front;
}
void display()
{
	temp=front;
	if(front==NULL)
		cout<<("\nEmpty");
	else
	{
		cout<<endl;
		for(;temp!=rear;temp=temp->next)
			cout<<(temp->info)<<" ";
	}
}
int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		create(x);
	}
	display();
}
