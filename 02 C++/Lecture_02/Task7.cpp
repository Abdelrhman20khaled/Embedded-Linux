/********************************************************************************* 
* File Name: Task4.cpp                                                           *
*                                                                                *
* Description: Use lambda functions to sort an array of integers in ascending    *
*              and descending order.                                             *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/
#include <iostream>

int main() 
{
    int i;
    int array_of_nums[5] = {50,60,40,30,20};
    int size = 0;

   [] (int * arr, int size)
   {
    int i, j, temp;
    for (i = 0; i < 5 - 1; i++) {
        for ( j = 0; j < 5 - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

   }(array_of_nums,5); 

    std::cout << "Ascending Sorting: ";
    for (i = 0; i < 5; i++) 
    {
        std::cout << array_of_nums[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Descending Sorting: ";
    for ( i = 4; i >= 0; i--) 
    {
        std::cout << array_of_nums[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
