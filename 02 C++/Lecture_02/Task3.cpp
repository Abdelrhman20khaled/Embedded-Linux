/********************************************************************************* 
* File Name: Task3.cpp                                                           *
*                                                                                *
* Description: This File delete number in array                                  *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

void DeleteElement(int * arr, int &size, int dElement)
{
    int i,j;

    for (i = 0; i < size; i++)
    {
        if(arr[i] == dElement)
        {
            std::cout<<"The Elemnt Now is Deleted . . ."<<std::endl;
            size-=1;
        }
    }  

     std::cout<<"The Elemnts in Array Now are ";

    for (i = 0; i < size; i++)
    {        
         arr[i] = arr[i+1];
        std::cout<<arr[i]<<" ";
    }
    std::cout<<std::endl;

}

int main()
{
    int Dnum, i;
    int array_of_num [6] = {12,3,5,6,7,4};
    int size = 6;
    std::cout<<"Number in the Array are: ";
    for (i = 0; i < size; i++)
    {        
        std::cout<<array_of_num[i]<<" ";
    }
    std::cout<<std::endl;

    std::cout<<"Enter the Number You need to delete: ";
    std::cin>> Dnum;
    std::cout<<std::endl;

    DeleteElement(array_of_num, size,Dnum);
 

}