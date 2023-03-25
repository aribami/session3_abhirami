#include <iostream>
float dayRate(int hour_rate){
    int res1 = hour_rate * 8;
    return res1;
}
float monthRate(int hour_rate, float discount){
    int res2 = hour_rate * 8 * 22 * (1-discount);
    return res2; 
}
float daysInBudget(int budget,int hour_rate, float discount ){
    int temp = 8* hour_rate * (1- discount);
    int res3 = budget/temp;
    return res3;
}
int main(){
 std::cout<<"the day rate given an hourly rate is =  "<<dayRate(89)<<"\n";
 std::cout<<"the month rate at a discount is = "<<monthRate(89, 0.42)<<"\n";
 std::cout<<"number of days of work that covers is = "<<daysInBudget(20000, 89, 0.2002)<<"\n";
 return 0;
}