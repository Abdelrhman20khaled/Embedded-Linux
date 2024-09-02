/********************************************************************************* 
* File Name: Task2.cpp                                                           *
*                                                                                *
* Description: This File search to the number in the array which number is taken *
*              from user                                                         *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

void MatchNunberWithUser(int * arr, int size, int ch_num)
{
    int i, flag;

    flag = 0;

    for (i = 0; i < size; i++)
    {
        if(arr[i] == ch_num)
        {
            std::cout<<"You Chosed Number "<<arr[i]<<std::endl;
            flag =1;
        }
    }  

    if(flag == 0)
    {
        std::cout<<"The Number is not in this Array"<<std::endl;
    }  
}

int main()
{
    int i,ch_num;
    int array_of_num [6] = {12,3,5,6,7,4};

    std::cout<<"Chose Number from This List : ";
    for( i = 0; i<6; i++)
    {
        std::cout<< array_of_num[i] <<" ";
    }
    std::cout<<std::endl;
    std::cin>> ch_num;
    std::cout<<std::endl;
    MatchNunberWithUser(array_of_num,6,ch_num);
}