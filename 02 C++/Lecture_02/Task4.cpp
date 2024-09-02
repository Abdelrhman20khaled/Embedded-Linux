/********************************************************************************* 
* File Name: Task4.cpp                                                           *
*                                                                                *
* Description: This File merge two arrays together                               *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

void Merge_2_Arrays(int * arr1, int size1, int *arr2, int size2)
{
    int i;
    int size_merged_arr = size1 + size2;
    int final_arr [size_merged_arr];

    for(i = 0; i < size1; i++)
    {
        final_arr[i] = arr1[i];
    }

    for(i = 0; i < size2; i++)
    {
        final_arr[size1+i] = arr2[i];
    }

    for (i = 0; i < size_merged_arr; i++)
    {        
         std::cout<<final_arr[i]<< " ";
    }
    std::cout<<std::endl;
}

int main()
{
    int array1_of_num[6] = {1,2,3,4,5,6};
    int array2_of_num[7] = {7,8,9,10,11,12, 13};
    
    std::cout<<"Two arrays after merged: ";
    Merge_2_Arrays(array1_of_num,6,array2_of_num,7);
}