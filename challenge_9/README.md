Square and Sort
=======
Idea
------
You are given a sorted list of integers. These integers go from smallest to largest and contain negative values. An example of a possible list could be this; [-2,-1,0,1,2]. Your job is to square every value in th is list, then return the re-ordered (smallest to largest numbers) version of it. Not too hard right? You could probably just do some simple squaring in a for loop then use quick sort or something right? Nope. You need to re-sort it in O(N) time or better.
 
 Important Notes:
 * The list passed to the function will always be sorted from smallest digits to largest digits.
 * The list may not contain any negatives or it may not contain 0 or it may not contain positives, but it will never be empty.
 
Hint: There is no limit on the space complexity.

Testing
------
The testing for this problem is fairly straight forward.

Test 1: An arbitrary test of a small list with negative and positive values. ex: [-2,-1,0,1,2] should evaluate to [0,1,1,4,4]

Test 2: Tests to see if your program can handle only negatives: [-3,-2,-1] -> [1,4,9]

Test 3: Tests to see if your program can handle only positives: [0,1,2,3] -> [0,1,4,9]

Test 4: Input that does not contain a zero: [-2,-1,1,2] -> [1,1,4,4]

Test 5: Tests to make sure your program can handle a list with a bunch of different values: [-100,-50,-2,-1,80,900,9001] -> [1, 4, 2500, 6400, 10000, 810000, 81018001]