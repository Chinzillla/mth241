## Independent Events:

### Def 1. 
If P(EF) = P(E) * P(F), then E and F are independent

### Def 2.
If E is independent from F then E is also independent from F-complement

#### Proof:

Assume E and F are independent. E = EF Union EF-complement and EF and EF-complement are mutually exclusive
```
E = EF U EF-complement
P(E) = P(EF) + P(EF-complement)

P(EF-complement) = P(E) * (1 - P(F))
P(EF-complement) = P(E) - P(E)P(F)

P(EF) = P(E) * P(F) given that E and F are independent

Subsitute
P(E) = P(EF) + P(E) - P(E)P(F)
P(E) = P(E)P(F) + P(E) - P(E)P(F)
P(E) = P(E)

Therefore if E and F are independent then E and F-complement is also independent
```

### Def 3.
Do not assume E independent from FG if
- E is independent of F
- E is independent of G

#### Proof:
2 fair dice
```
E sum is 7: {1.6, 6.1, 2.5, 5.2, 3.4, 4.3}
F first die is 4: {4.1, 4.2, 4.3, 4.4, 4.5, 4.6}
G second die is 3: {1.3, 2.3, 3.3, 4.3, 5.3, 6.3}

Independence check for E and F
P(E) = 6/36
P(F) = 6/36
P(EF) = 1/36
1/36 = 1/6 * 1/6
E and F are independent

Independence check for E and G
P(E) = 6/36
P(G) = 6/36
P(EF) = 1/36
1/36 = 1/6 * 1/6
E and G are independent

Independence check for F and G
P(F) = 6/36
P(G) = 6/36
P(FG) = 1/36
1/36 = 1/6 * 1/6
F and G are independent

Independence check for E and FG
P(E) = 6/36
P(FG) = 1/36
P(E FG) = 1/36

P(E FG) = P(E) * P(FG)
1/36 = 1/36 * 6/36
1/36 = 1/36 * 1/6
E is not independent of FG

P(EFG) = P(E)P(F)P(G)
1/36 = 1/6 * 1/6 * 1/6
Which is not independt

```

### Def 4.
E F and G are said to be independent if:
```
P(EFG) = P(E)P(F)P(G)
P(EF) = P(E)P(F)
P(EG) = P(E)P(G)
P(FG) = P(F)P(G)
```