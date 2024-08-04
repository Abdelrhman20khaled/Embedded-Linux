/********************************************************************************* 
* File Name: Task7.cpp                                                           *
*                                                                                *
* Description: This File include task to get summation the digits of integer     *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

int main() 
{
    int number,sum = 0;

    /*Ask User to enter a number*/
    std::cout<<"Enter The Number"<<std::endl;
    std::cin>>number;
    
    /*Divide a number and calculate the sum of digits*/
    while (number != 0)
    {
        int in_num=0;
        in_num =  number % 10;
        sum+= in_num;
        number /= 10;
    }

    std::cout << "Sum of Digits in " << number <<" is = " <<sum << std::endl;
}