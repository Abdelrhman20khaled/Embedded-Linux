/********************************************************************************* 
* File Name: Task4.cpp                                                           *
*                                                                                *
* Description: This File include task to get right angle triangle                *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>
#include <cmath>

int main()
{
    float side1_len,side2_len,hypotenuse_len;
    //Ask User to enter two numbers
    std::cout<<"Enter the Length of the Side 1: "<<std::endl;
    std::cin>> side1_len;

    std::cout<<"Enter the Length of the Side 2: "<<std::endl;
    std::cin>> side2_len;

    hypotenuse_len = sqrt(pow(side1_len,2) + pow(side2_len,2));
    //hypotenuse_len = sqrt(side1_len*side1_len + side2_len*side2_len);
    
    std::cout<<"The Length of Hypotenuse is: "<< hypotenuse_len <<std::endl;
}