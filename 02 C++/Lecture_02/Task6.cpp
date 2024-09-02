/********************************************************************************* 
* File Name: Task4.cpp                                                           *
*                                                                                *
* Description: This File lambda function to calculate the square of a            *
*              given number.                                                     *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <cmath>
#include <iostream>

int main()
{
    int user_num;

    std::cout<<"Enter the Number ";
    std::cin>> user_num;

    auto sq_num = [](int num)
    {
        return num*num;
        //return pow(num,2);
    };

    std::cout<<"The Square of "<<user_num<<" is "<<sq_num(user_num)<<std::endl;
}