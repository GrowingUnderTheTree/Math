#include <iostream>
using namespace std;

//Using an Example of dydx = t*y+1
float dydx(float t, float y){
	return ((t*y)+1);
}

float rungekutta(float x_0, float y_0, float t, float h){
	int n = (int)((t-x_0)/h);
	float k1, k2, k3, k4;
	float y = y_0;
	for(int i = 0; i < n; i++){
		k1 = h * dydx(x_0, y);
		k2 = h * dydx(x_0 + 0.5 * h, y + 0.5 * k1);
		k3 = h * dydx(x_0 + 0.5 * h, y + 0.5 * k2);
		k4 = h * dydx(x_0 + h, y + k3);
		y = y + (k1/6) + (k2/3) + (k3/3) + (k4/6);
		x_0 = x_0 + h;
	}
	return y;
}

int main() {
	//x0, initial x value, y, initial y value, t target value, h, step function
	float x0 = 0,y = 1,t = 0.1,h = 0.1;
	cout << rungekutta(x0,y,t,h);
	return 0;
}

