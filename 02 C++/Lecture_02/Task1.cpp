/********************************************************************************* 
* File Name: Task1.cpp                                                           *
*                                                                                *
* Description: This File ﬁnd the maximum number of array                         *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

int MaxInArray(int arr[], int size)
{
    int i =0;
    int max = arr[i];

    for( i= 0; i< size; i++)
    {
        if(max < arr[i])
        {
            max = arr[i];
        }
    }

    return max;
}

int main()
{
    int array_of_numbers[6] = {3,6,7,100,4,46};

    std::cout<<"The Maximum Element in Array is "<<MaxInArray(array_of_numbers,6)<<std::endl;
}