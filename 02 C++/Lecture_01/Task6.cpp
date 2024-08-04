/********************************************************************************* 
* File Name: Task6.cpp                                                           *
*                                                                                *
* Description: This File include task to create multiple tables                  *
*                                                                                *
* Author: Abdelrahman Khaled Sobhi                                               *
*                                                                                *
*********************************************************************************/

#include <iostream>

int main()
{
    int table_num,i;
    /* Ask User to enter a number of table */
    std::cout<<"Enter Number of Table: "<<std::endl;
    std::cin>> table_num;
    /* CHeck teh number of table then loop to print the table*/
    switch (table_num) 
    {
        case 1:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 1       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 2:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 2       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 3:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 3       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 4:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 4      |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 5:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 5       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 6:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 6       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 7:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 7       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 8:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 8       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 9:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 9       |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 10:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 10      |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 11:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 11      |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<" "<<i<<" * "<<table_num<<" = "<<i*table_num<<std::endl;
        }
        break;

        case 12:
        std::cout<<"------------------------"<<std::endl;
        std::cout<<"|        Table 12      |"<<std::endl;
        std::cout<<"------------------------"<<std::endl;

        for(i= 0 ;i <= 12 ;i++)
        {
            std::cout<<"   "<<i<<"  * "<<table_num<<"  = "<<i*table_num<<std::endl;
        }
        break;

    }
}