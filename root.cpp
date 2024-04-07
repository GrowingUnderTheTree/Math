#include <iostream>

void cube() {
    long double input;
    long double initial = 1;
    long double up, down;
    std::cout << "Enter number to calculate cube root : " << std::endl;
    std::cin >> input;
    for(int i = 1; i < 11; i++){
        up = (initial * initial * initial) - input;
        down = 3 * (initial * initial);
        initial = initial - (up/down);
        std::cout.precision(50);
        std::cout << "round " << i << " answer = " << initial << std::endl;
}
}
void square() {
  long double input;
    long double initial = 1;
    long double up, down;
    std::cout << "Enter the number to calculate square root : "<< std::endl;
    //newton's method
    std::cin >> input ;
    for(int i = 1; i < 1001; i++){
        up = (initial * initial) - input;
        down = 2 * initial;
        initial = initial - (up/down);
        std::cout.precision(63);
        std::cout << "round " << i << " answer = " << initial << std::endl;
    }
    //to calculate square root
}

int main() {
    long double input;
    long double initial = 1;
    long double up, down;
    std::cout << "Enter number to calculate cube root : " << std::endl;
    std::cin >> input;
    for(int i = 1; i < 1001; i++){
        up = (initial * initial * initial) - input;
        down = 3 * (initial * initial);
        initial = initial - (up/down);
        std::cout.precision(12);
     }
    std::cout <<" answer = " << initial << std::endl;
    return 0;
}