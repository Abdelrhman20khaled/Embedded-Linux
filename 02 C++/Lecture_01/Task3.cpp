/********************************************************************************* 
* File Name: Task3.cpp                                                           *
*                                                                                *
* Description: This File include task to get maximum number between three values *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

int main()
{
    int number1,number2,number3, max_num;
    /*declaring max_var equal to number1 at the beginning*/
    max_num = number1;
    /* Ask User to enter three numbers*/
    std::cout<<"Enter First Number: "<<std::endl;
    std::cin>>number1;

    std::cout<<"Enter Second Number: "<<std::endl;
    std::cin>>number2;

    std::cout<<"Enter Third Number: "<<std::endl;
    std::cin>>number3;
    /*Check which number is bigger then assign it to max_num*/
    if(number2 > max_num && number2 > number3)
    {
        max_num = number2;
    }
    else if (number3 > max_num && number3 > number2)
    {
        max_num = number3;
    }
    else
    {
        max_num = number1;
    }

    std::cout<<"The Maximum Number is: "<<max_num<<std::endl;
}