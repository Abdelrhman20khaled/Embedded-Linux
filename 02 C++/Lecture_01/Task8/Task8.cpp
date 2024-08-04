/********************************************************************************* 
* File Name: Task8.cpp                                                           *
*                                                                                *
* Description: This File include task to change decimal - binary and vice versa  *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>
#include <bitset>

int main()
{
    // Convert decimal to binary
    char choise;
    int decimalNumber;
    std::string binaryNumber;

    /* Ask User to enter a number*/
    std::cout << "1. Convert decimal to binary" << std::endl;
    std::cout << "2. Convert binary to decimal" << std::endl;
    std::cin >> choise;
    
    /*Check if the number is one of (1,2) then implement the case match*/
    switch (choise) 
    {
        case '1':
            std::cout << "Enter a decimal number: " << std::endl;
            std::cin >> decimalNumber;
            std::cout << "Binary number: " << std::bitset<32>(decimalNumber) << std::endl;
        break;

        case '2':
            std::cout << "Enter a binary number: " << std::endl;
            std::cin >> binaryNumber;
            std::cout << "Decimal number: " << std::bitset<32>(binaryNumber).to_ulong() << std::endl;
        break;

        default:
            std::cout << "Invalid choise" << std::endl;
            break;
    }

}