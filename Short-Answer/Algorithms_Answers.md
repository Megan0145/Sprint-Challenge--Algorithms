#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n):
    As n increases, so too does the number of iterations of the while loop
    Continues iterating until it reaches the base case where n^3 is less than or equal to a,
    increasing a by the value of n^2 each time

b) O(n log n)
    Outer loop executes n number of times. 
    Inner loop executes log(n) times:
    eg n = 4
        n = 4, j = 1 on first pass
        while j < n:
            j*= 2
        n = 4, j = 2 on second pass
        while j < n:
            j*= 2    
        n = 4, j = 4 on third pass    
        -> won't execute while loop (4 !< 4)
        -> total number of executions = 2
    
    eg n = 5:
        executes 2 times
    eg n = 6:
        executes 3 times    
    Therefore time goes up linearly while n goes up exponentialy 
    inner loop * outer loop = n * log n
    = O(n log n)    

c) Linear O(n):
   This is because the function will be called recursively 'bunnies' times before it reaches the base case of bunnies == 0.
   eg bunnyEars(4):
      2 + bunnyears(3)
      2 + 2 + bunnyEars(2)
      2 + 2 + 2 + bunnyEars(1)
      2 + 2 + 2 + 2 + bunnyEars(0) -> will break out of loop 
    Therefore the depth of the recursion tree directly correlates to the value of bunnies -> linear 


## Exercise II
The best way to think about this for me was in terms of a simple binary search algorithm.
Given the number of floors = 20
Get the middle floor = 10
Drop the egg from the middle floor
 -> If it breaks, we know that f is not going to be a higher floor, it has to be lower
        -> Repeat all above steps from floors 0 - 10 dropping the egg from the middle each time til we get to the highest floor that the egg doesn't break, (f is determined)
 -> Else if it doesn't break, we know that f is not going to be a lower floor, it has to be higher   
       -> Repeat all above steps from floors 10 - 20, dropping the egg from the middle each time til we get to the highest floor that the egg doesn't break (f is determined)

This is efficient because the number of remaining floors to search on each iteration is halved. Ratehr than iterating over every floor, one by one from the ground floor to the 20th floor

Runtime complexity of binary search algorithm is O(log n) because as mentioned above, the length of the input gets halved on each iteration (you either discard the lhs or the rhs)