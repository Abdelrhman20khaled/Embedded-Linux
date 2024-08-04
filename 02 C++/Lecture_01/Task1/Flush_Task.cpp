/********************************************************************************* 
* File Name: Flush_Task.cpp                                                      *
*                                                                                *
* Description: This File include Flush Task see the documentation in readme file.*
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>
#include <thread>
#include <chrono>

int main() {
    int Age;
    std::cout << "Please Enter Your Age: " << std::flush;
    //This line used for make a delay in the code for 5 seconds
    std::this_thread::sleep_for(std::chrono::seconds(5)); 
    std::cin >> Age;
    std::cout << "You entered: " << Age << std::endl;
    return 0;
}
