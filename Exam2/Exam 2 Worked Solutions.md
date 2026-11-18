# MTH 241 Exam 2 Worked Solutions

Attempt the questions on paper before checking the work. The [study guide](<Exam 2 Study Guide.md>) gives a practice order and a short diagnostic.

## Fall 2022 Test 2

[Open the Fall 2022 paper](<241 Fall 2022 Test 2.pdf>)

### Q1 Choosing a distribution

**(a)** If a population of `N` items contains `K` designated successes and `n` items are sampled uniformly without replacement, the number `X` of successes drawn is hypergeometric. Its probability mass is `C(K,k)C(N−K,n−k)/C(N,n)` for integer `k` from `max(0,n−(N−K))` through `min(n,K)`, and zero elsewhere. The top counts samples with exactly `k` successes. The bottom counts all possible samples of size `n`.

**(b)(i)** Model the grade sum by counting unordered pairs of distinct students. If there are `N` students, divide the number of pairs whose grades sum to the requested value by `C(N,2)`. A hypergeometric variable would count sampled students in a specified grade category.

**(b)(ii)** Binomial with `n = 8` and `p = 1/10`. Each roll succeeds when it shows the chosen number.

**(b)(iii)** Negative binomial, assuming independent houses with common probability `p` of a bucket. House 100 must contain a bucket, with exactly two buckets among the first 99 houses. The probability is `C(99,2)p³(1−p)⁹⁷`.

### Q2 Wheel choice and geometric payoff

The payout is 32 dollars when `128(1/2)ⁿ = 32`, so the first blue must occur on spin 2. Treat repeated spins as independent conditional on the wheel.

**(a)** Heads selects A. Miss blue once, then hit blue. The probability is `.7(.3) = .21`.

**(b)** Tails selects B, where the corresponding probability is `.6(.4) = .24`. Weight the two branches to get `(2/3)(.21) + (1/3)(.24) = .22`.

**(c)** The largest payout is 64 dollars, and it occurs on the first spin with probability `(2/3)(.3) + (1/3)(.4) = 1/3`. In all other cases the payout is at most 32 dollars. The expected payout is therefore at most `64(1/3) + 32(2/3) = 128/3` dollars, below the 55-dollar entry cost.

For an exact conditional expectation at a wheel with blue probability `p`, sum the geometric series `64p Σⱼ[(1−p)/2]ʲ` over `j = 0, 1, …`. It equals `128p/(1+p)`. Averaging the two wheel means gives an expected payout of about 31.88 dollars.

### Q3 Poisson approximation and a binomial count

**(a)** For the intended Poisson model for the large group, `P(X = 3)/P(X = 2) = λ/3`. Using the supplied ratio `.3/.2` gives `λ = 4.5`.

**(b)** Take the complement of 0 through 3. `P(X ≥ 4) ≈ 1 − exp(−4.5)[1 + 4.5 + 4.5²/2! + 4.5³/3!] ≈ .65770`.

**(c)** The large group's mean is `241p ≈ 4.5`, so the shared success probability is `p ≈ 4.5/241 ≈ .01867`.

**(d)** Use a binomial with 10 trials. `P(Y = 2) ≈ C(10,2)(4.5/241)²(1−4.5/241)⁸ ≈ .01349`.

Treat the printed numbers as inputs to the intended ratio method. At `λ = 4.5`, the Poisson mass at 2 is about `.11248`. Even the exact binomial ratio `(239/3)p/(1−p) = .3/.2` gives `p = 9/487`, for which the mass at 2 is about `.11441`. The two stated masses cannot both be exact under either model.

### Q4 Weighted die

Assume each of the 21 faces is equally likely and the rolls are independent. A single roll satisfies `P(X = j) = j/21` for `j = 1,…,6`.

**(a)** `E(X) = (1² + 2² + … + 6²)/21 = 91/21 = 13/3`. Then `E(X²) = (1³ + 2³ + … + 6³)/21 = 441/21 = 21`, so `Var(X) = 21 − (13/3)² = 20/9`.

**(b)** `Z` counts the 1s in three rolls, so `Z` is binomial with `p = 1/21`. Then `P(Z = 2) = C(3,2)(1/21)²(20/21) = 20/3087`.

**(c)** A sum of 4 requires the values `1, 1, 2`. Any of the three positions can hold the 2, so `P(Y = 4) = 3(1/21)²(2/21) = 2/3087`.

**(d)** `E(2Z−1) = 2E(Z)−1 = 2(3/21)−1 = −5/7`.

### Q5 Variance proof and shared random variable

**(a)** Let `μ = E(X)` and `v = Var(X)`. Both are constants. The first term is `E[vX²] = vE(X²)`. The second is `Var(μX) = μ²v`. Their difference is `v[E(X²)−μ²] = v²`.

**(b)** Combine the expressions to get `Y+Z = X+13` and `Y−Z = 3X+5`. Thus `E(X) = 27−13 = 14` and `Var(X) = 48/9 = 16/3`. Then `E(X²) = 16/3 + 14² = 604/3`.

### Bonus First and second successes

For independent trials with `0 < p < 1` and `n ≥ 2`, the second success occurs on trial `n` with probability `(n−1)p²(1−p)ⁿ⁻²`. The first success occurs on trial `n` with probability `p(1−p)ⁿ⁻¹`. Equate and divide by `p(1−p)ⁿ⁻²` to get `(n−1)p = 1−p`, hence `p = 1/n`.

## Spring 2022 Test 2

[Open the Spring 2022 paper](<241 Spring 2022 Test 2.pdf>)

### Q1 Normalizing and integrating a continuous density

**(a)** The PDF shows the fraction `f(x) = (1−x)³/(k+1)` on `[1,3]`. The integral of the numerator over this interval is `−4`. Set `−4/(k+1) = 1` to get `k = −5`. The resulting density is `(x−1)³/4`, which is nonnegative on the support.

**(b)** Intersect the requested interval with the support. The probability is the integral from 1 to 2 of `(x−1)³/4`, giving `[(x−1)⁴/16]₁² = 1/16`.

**(c)** `P(X ∈ R) = 0`, since `R` is a finite set and each point has probability zero.

**(d)** Use the integral form of expectation for this continuous variable. Substitute `t = x−1` into the integral from 1 to 3 of `x(x−1)³/4`. This gives `(1/4)∫₀² (t⁴+t³) dt = (1/4)(32/5+4) = 13/5`. The printed summation is the discrete version of the formula.

### Q2 Best of seven

Assume independent games with `p = P(A wins a game)` and `q = 1−p`.

**(a)** For A to win in six, A wins game six and three of the first five. The probability is `C(5,3)p⁴q²`. For B to win in seven, B wins game seven and three of the first six, with probability `C(6,3)q⁴p³`. For `0 < p < 1`, cancel `10p³q²` in the equality to obtain `p = 2(1−p)²`. This factors as `(2p−1)(p−2) = 0`, so the nondegenerate probability is `p = 1/2`. At `p = 0` or `p = 1`, both specified events have probability zero and the series always ends in four games.

**(b)** For the fair case, either team can win. For series length `s`, the winner takes game `s` and exactly three earlier games. Hence `P(X = s) = 2C(s−1,3)(1/2)ˢ` for `s = 4,5,6,7`.

| Games | 4 | 5 | 6 | 7 |
| --- | ---: | ---: | ---: | ---: |
| Probability | `2/16` | `4/16` | `5/16` | `5/16` |

The weighted sums give `E(X) = 93/16` and `E(X²) = 557/16`. Therefore `Var(X) = 557/16 − (93/16)² = 263/256`.

### Q3 Discrete CDF with a corrected PMF

**(a)** The proper positive divisors of 28 are `1, 2, 4, 7, 14`. The printed weights `1/s` sum to `1 + 1/2 + 1/4 + 1/7 + 1/14 = 55/28`. A valid PMF must sum to 1. This makes the printed PMF invalid and leaves parts (b)–(d) without a probability distribution as written.

**(b)** To practice the remaining parts, divide each weight by `55/28`. In increasing order, the normalized masses are `28/55, 14/55, 7/55, 4/55, 2/55`. Add the masses up through `x` to get the CDF.

| Interval | `F(x)` |
| --- | ---: |
| `x < 1` | `0` |
| `1 ≤ x < 2` | `28/55` |
| `2 ≤ x < 4` | `42/55` |
| `4 ≤ x < 7` | `49/55` |
| `7 ≤ x < 14` | `53/55` |
| `x ≥ 14` | `1` |

**(c)** Use an open dot at the old height and a filled dot at the new height. The height labels give the exact values.

```text
F(x)
    1 │                                           ●──────→
53/55 │                      ●────────────────────○
49/55 │             ●────────○
42/55 │       ●─────○
28/55 │    ●──○
    0 │←───○
      └────┬──┬─────┬────────┬────────────────────┬──────→ x
           1  2     4        7                    14
```

**(d)** The event includes the mass at 7, so subtract the CDF just to its left. `P(X ≥ 7) = 1 − 49/55 = 6/55`.

### Q4 One road and two conditional binomials

Interpret the stated frequencies as per-drive ticket probabilities, with independence conditional on the road. Let `B(n,k,p) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ`. Road A is chosen with probability `1/3` and uses `p = 2/5`. Road B is chosen with probability `2/3` and uses `p = 3/7`.

**(a)** Weight the probability of exactly 50 tickets under each road. `P(X = 50) = (1/3)B(100,50,2/5) + (2/3)B(100,50,3/7) ≈ .02237`.

**(b)** For each road, subtract the probabilities of 0, 1, and 2 from 1. This gives about `.91656` for A and `.94288` for B. If you know which road was built, use its branch. Before learning which road was built, `P(X ≥ 3) = (1/3)(.91656…) + (2/3)(.94288…) ≈ .93410`.

**(c)** The variance before learning the road is the weighted average of the within-road variances plus the variance of the road-specific means. The first term measures variability on a fixed road. The second accounts for the two possible means.

- Within-road contribution is `n[(1/3)(2/5)(3/5) + (2/3)(3/7)(4/7)] = n(298/1225)`.
- The conditional means are `2n/5` and `3n/7`. For a two-value variable with weights `1/3` and `2/3`, the variance is the product of the weights times the squared difference. This contributes `(1/3)(2/3)(2n/5−3n/7)² = 2n²/11025`.
- The sum is about `26.14059` for 100 drives and `2.94531` for 12 drives. If the road is known, the variance is simply `np(1−p)` for that road.

**(d)** The binomial calculation for part (b), done within each road and weighted if needed, is exact under the model. A Poisson formula for part (a) is an approximation. The per-drive probabilities near `.4` also make the rare-event approximation a poor fit here. This favors the conditional binomial calculation `s`.

### Q5 Reading a proof and recovering a second moment

**(a)** The printed identity fails, for instance with `a = b = 0`, zero integration constants, and any `X` of positive variance. To see a related identity, let `G(t) = at²/2 + bt`, an antiderivative of `at+b`. Then `E[G(X)] − G(E(X)) = (a/2)(E(X²) − [E(X)]²)`. Taking `a = 2` gives `Var(X)`.

To prove the variance formula directly, let `μ = E(X)`. Expanding gives `E[(X−μ)²] = E(X²) − 2μE(X) + μ² = E(X²) − μ²`.

**(b)** `E(X) = (15−4)/3 = 11/3` and `Var(X) = 32/2² = 8`. Thus `E(X²) = 8 + (11/3)² = 193/9`, and the requested answer is `193/9 − √8 = 193/9 − 2√2`.

## Chapter 3 Homework Checks

[Open the October 20 homework](<HW/10-20-2026.md>)

- **3.34** Pick the family, then a child. The probability of picking the eldest is `Σⱼ pⱼ/j = 5/12`. The two posteriors are `.1/(5/12) = 6/25` and `(.3/4)/(5/12) = 9/50`.
- **3.44** The probability of being in California and over the income threshold is `.12(.033) = .00396`. For (a), the non-California rate is `(.013−.00396)/.88 ≈ 1.0273%`. For (b), the California share among households above the threshold is `.00396/.013 ≈ 30.4615%`.
- **3.51** For prior `π`, the posterior after an elevated result is `.268π/[.268π+.135(1−π)]`. For a result below the elevation threshold, use `.732` and `.865` in the same positions. The elevated and non-elevated posteriors are `.82245` and `.66382` at prior `.7`, and `.45969` and `.26615` at prior `.3`.
- **3.52** The accident probability is `.2(.05)+.5(.15)+.3(.30) = .175`. Given no accident, the good-risk and average-risk probabilities are `.2(.95)/.825 ≈ .23030` and `.5(.85)/.825 ≈ .51515`.
- **3.53** The offer probability is `.65`. Given an offer, the strong, moderate, and weak probabilities are `.56/.65, .08/.65, .01/.65`. Given no offer, they are `.14/.35, .12/.35, .09/.35`.
