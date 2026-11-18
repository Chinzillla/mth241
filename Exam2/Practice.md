1. Bag of Marbles
```
A bag contains 6 red and 4 blue marbles. You draw 3 without replacement. What’s the probability of exactly 2 reds?

Ways to choose 2 reds from 6 = 6 choose 2
Ways to choose 1 blue from 4 = 4 choose 1
Ways to choose any 3 marbles from 10 = 10 choose 3

So we get P(X=2,Y=1)[where X = red and Y = blue] = (6 choose 2 * 4 choose 1) / (10 choose 3)
```

2. Scoring attempt
```
Probability is 25% chance to score on each independent attempt
P(Score) = .25
P(No Score) = .75

P(X=3) = P.1(No Score) * P.2(No Score) * P*3(Score)
Answer: .75 * .75 * .25

P(First score on attempt 3) = (1-p) * (1-p) * p = p * (1-p)^2
```

3. Practice question: What is the probability of rolling a 6 on the fourth attempt?
```
P(First 6 on attempt 4) = 1/6 * (1-1/6)^3
```

4. Practice question: What is the probability of rolling atleast one 6 in four rolls?
```
- Or
- Atleast one 6

6 _ _ _
_ 6 _ _
_ _ 6 _
_ _ _ 6

So would we do
(1/6) + (1/6 * (1-1/6)) + (1/6 * (1-1/6)^2) + (1/6 * (1-1/6)^3)
```

5. Practice question: What is the probability of rolling exactly one 6 in four rolls? 
```
- Or
- exactly 1 6

6 _ _ _ = 1/6 * 5/6 * 5/6 * 5/6
_ 6 _ _ = 5/6 * 1/6 * 5/6 * 5/6
_ _ 6 _ = 5/6 * 5/6 * 1/6 * 5/6
_ _ _ 6 = 5/6 * 5/6 * 5/6 * 1/6

Answer: (1/6 * 5/6 * 5/6 * 5/6) + (5/6 * 1/6 * 5/6 * 5/6) + (5/6 * 5/6 * 1/6 * 5/6) + (5/6 * 5/6 * 5/6 * 1/6)
```

6. The city plans on building a road from your house to Walmart or Target or something. The probability they build road A is 1/3, while the probability they build road B is 2/3. If road A is built, then every 5 times you drive on that road,you will get 2 speeding tickets. If road B is built, then every 7 times you drive on that road, you will get 3 speeding tickets.

a. You drive on the road 100 times. What is the probability you will get 50 tickets?
```
P(A) = 1/3
P(B) = 2/3

P(T|A) = ?
P(T|B) = ?

Goal is to find P(T) = 1/3(P(T|A)) + 2/3(P(T|B))

P(T|A) = P(T intersect A) / P(A)
P(T|B) = P(T intersect B) / P(B)

Probability of getting a ticket = 2/5
2 tickets for 5 drives

(100 choose 50) * (2/5)^50 * (3/5)^50
```