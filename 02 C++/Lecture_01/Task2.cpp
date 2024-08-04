/********************************************************************************* 
* File Name: Task2.cpp                                                           *
*                                                                                *
* Description: This File include Task to create a table for AscII code.          *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

int main() 
{
    std::cout << "Ascii Table" << std::endl;
    std::cout<<"------------------------"<<std::endl;
    std::cout<<"|    Char   |   Value  |"<<std::endl;
    std::cout<<"------------------------"<<std::endl;
    /*
     * This loop will itrate from 0 to 255 and print each value then by
     * using casting to print the char of the value. 
    */
    for (int i = 0; i < 256; i++)
    {
        std::cout << "     "<< i << "          " <<  (char) i  << std::endl;
    }
}