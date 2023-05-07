#include <iostream>

int main() {
    long double input;
    long double initial = 1;
    long double up, down;
    std::cout << "Enter the number to calculate square root : "<< std::endl;
    std::cin >> input ;
    for(int i = 1; i < 11; i++){
        up = (initial * initial) - input;
        down = 2 * initial;
        initial = initial - (up/down);
        std::cout.precision(63);
        std::cout << "round " << i << " answer = " << initial << std::endl;
    }
    return 0;
}