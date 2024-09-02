/********************************************************************************* 
* File Name: Task4.cpp                                                           *
*                                                                                *
* Description: This File ﬁnd the even and odd numbers in the array               *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>
#include <ostream>

void Even_Odd_inArray(int *arr, int size)
{
    int EvenArr[size];
    int OddArr[size];
    int EvenCounter = 0;
    int OddCounter = 0;
    int i;

    for( i = 0; i<size; i++)
    {
        if(arr[i]%2 ==0)
        {
            EvenArr[EvenCounter] = arr[i];
            EvenCounter++;
        }
        else if (arr[i]%2 != 0) 
        {
            OddArr[OddCounter] = arr[i];
            OddCounter++;
        }
        else if (arr[i] == 0)
        {
            //Do No Thing
        }
    }

    std::cout<<"Array has "<<EvenCounter<<" Even Numbers ";
    
    for (i = 0; i < EvenCounter; i++)
    {        
         std::cout<<EvenArr[i]<< " ";
    }

    std::cout<<std::endl;

    std::cout<<"Array has "<<OddCounter<<" Odd Numbers ";

    for (i = 0; i < OddCounter; i++)
    {        
          std::cout<<OddArr[i]<< " ";
    }

    std::cout<<std::endl;
}

int main()
{
   int array_of_num[10]={1,2,3,4,5,6,7,8,9,10};
   Even_Odd_inArray(array_of_num,10);
}