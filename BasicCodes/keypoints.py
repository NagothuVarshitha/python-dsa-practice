"""
###LOOPS###
✅ Print outside the loop
When you need the final result.
✅ Print inside the loop
When you want to see each step.
✅ List is like a pencil we can erase and rewrite it can be changed(mutable)
✅ Tuple is like pen we cant erase and it cant be changed(Immutable)
✅ ord() : it is a built-in function that returns the ASCII(unicode) value of a char.
✅ Initialisation: to find max: use float(-inf) ,
                    to find min: use float(inf),
                    counting,sum: initialise with 0
                    product: initialise with 1
                    index not found, bfs/visited, dp(depends on sum): use -1
                    boolean flag: use false,..
✅Can we ever modify a list inside a set?
No, because Python doesn't allow a list inside a set in the first place.
A list cannot be stored inside a set because lists are mutable and unhashable.
Attempting to create such a set raises a TypeError, so there is no list to modify.
✅for i in n: Use this when you only need the values.
here "i" is the element.
(Ex: Find maximum,Find min,Sum of elements,Count even numbers)
✅for i in range(len(n)): Use this when you need the index.
here "i" is the index.
Ex: Change an element,Compare neighboring elements,Two-pointer problems,Access n[i+1], n[i-1]...etc
✅Two Sum(Hash Map): Whenever asked to find a pair quickly → Think Hash Map.
✅Sorted array, Remove Duplicates(Two Pointers):Whenever the array is sorted and duplicates
 need to be removed → Think Two Pointers.
✅Matching brackets,Undo,Nested structure(Stack): when they ask Need most recent element
✅Whenever you only need values/characters---for ch in s
    Whenever you only need index.---for i in range(len(s))
✅while n > 0 → Continue until no digits are left.
for i in range(1, n + 1) → Continue until i reaches n.
✅reverse = reverse * 10 + digit
•  Multiply by 10 → Creates an empty place on the right.
•  Add the digit → Fills that empty place.
✅Am I removing digits?-n = n // 10 (we use this 2 line removing and getting last digit only for digits prblm)
Then use---while n > 0: instead of ---for i in range(...)
✅Digits → while
Known range of numbers → for
✅Will I need the original number later?---temp = n
Ex:Palindrome ✔
Armstrong ✔
Reverse ✔
✅digit = len(str(n)) -- counts digits in a num
✅Am I calculating a result?----sum = 0(Then create a separate variable)
✅reverse = reverse * 10 + rem----because we are making another number(reverse of the given number)
✅How do we get the last 2 digits?--625%100
✅"Give me the last N digits."--number % (10 ** N)
Ex:number % 10        # Last 1 digit
number % 100       # Last 2 digits
number % 1000      # Last 3 digits
number % (10**N)   # Last N digits
✅The variable used in the while condition should usually be the same variable that is updated inside the loop.
Condition variable = Update variable ✅
while i <= n: (condition)
    i += 1    (update)
while n > 0:    (condition)
    n = n // 10 (update)
while count > 0:    (condition)
    count -= 1  (update)
✅Question says Contains, Immediately think--n
            Starts with,--startswith()
            Ends with,--endswith()
✅Repeatedly replacing the number...or repeatedly
until
keep doing
again and again---then we need another loop
✅Whenever you don't know how many times something repeats, use: while
✅Before writing any code, ask yourself these 5 questions
--what am I processing?
Digits / Factors / Range / String?
--What operation should I perform on each item?
Add? Square? Factorial? Reverse?
--Am I done after one pass?
Yes → One loop.
No → Repeated process → Another loop.
--What is the stopping condition?
n == 0? n == 1? count == digits? i <= n?
--What should I compare at the end?
Original number? 1? Reverse? Sum?
✅HCF--The number is being divided by i. (if n1%2==0 and n2%2==0)
✅LCM-current number (lcm) is being divided by n1.(if lcm%n1==0 and lcm%n2==0)
✅Diff b/w reverse and rotation
reverse-->197---791
rotation-->Move the first digit to the last.
(Trick:If a number has n digits, then it has n rotations.)
197-->971-->719------->rotation=3
✅for 197--->num[1:] + num[0]
"97" + "1"-->"971"
because strings are joined together (concatenated).
✅When should we use a flag?
Are ALL rotations prime? we dont know so we assume flag =
use only If the question asks only YES / NO type
If the question asks you to largest/smallest,count, don't use a flag.



####PATTERNS####
✅Outer loop → HOW MANY ROWS?
Inner loop → HOW MANY THINGS IN EACH ROW?
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅
✅

"""

