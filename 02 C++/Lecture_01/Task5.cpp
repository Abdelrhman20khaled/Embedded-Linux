/********************************************************************************* 
* File Name: Task5.cpp                                                           *
*                                                                                *
* Description: This File include task to decide the letter is vowel or not       *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/


#include <iostream>


int main()
{
    char user_char;
    /* Ask User to enter a character*/
    std::cout<<"Enter a Character: "<<std::endl;
    std::cin>> user_char;
    /* CHeck if the character is one of (a,e,i,o,u) of (A,E,I,O,U)*/
    if(
        user_char == 'a' || user_char == 'A' || 
        user_char == 'e' || user_char == 'E' ||
        user_char == 'i' || user_char == 'I' ||
        user_char == 'o' || user_char == 'O' ||
        user_char == 'u' || user_char == 'U'
        )
        {
            std::cout<<"The Character is Vowel"<<std::endl;
        }
    else
        {
            std::cout<<"The Character is non Vowel"<<std::endl;
        }
}