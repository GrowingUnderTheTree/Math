program factorial
implicit none
integer :: j, n
integer :: fact
fact = 1
print *, 'Enter value of n : '
read(*,*) n
do j = 1, n
fact = fact * j
print *, fact
end do
end program factorial
