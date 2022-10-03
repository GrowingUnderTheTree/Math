program hello
! Prints out the area of circle
implicit none
real :: pi
real :: radius
real :: answer
print *, 'Enter the radius of circle (in cm)'
read(*,*) radius
pi = 3.141592654
answer = 2 * pi * radius
print *, 'The area of the circle is : ', answer , ' cm'
end program hello
