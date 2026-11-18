# MTH 241 Exam 2 Study Guide

**Exam day is Thursday, November 19.** Start with the diagnostic below. Mark any question where you could do the arithmetic but were unsure how to set it up. That tells you what to practice first.

## Eight minute diagnostic

Use scratch paper. Write the model or equation even if you run out of time to calculate.

1. A bag has 5 red and 7 blue marbles. Draw 3 at random without replacement. What model gives the number of red marbles? Find the probability of exactly 2 reds.
2. A player has a 30% chance to score on each independent attempt. What is the probability that their first score comes on attempt 4? What is the probability of exactly one score in four attempts?
3. A fair coin selects machine A or B. Their defect rates are 2% and 8%, respectively. What is the probability a randomly produced item is defective? Given a defect, what is the probability machine B made it?
4. A discrete random variable's CDF jumps only at 0, 1, and 3, where it takes the values 0.2, 0.7, and 1, respectively. Find `P(X = 1)` and `P(X ≥ 1)`.
5. Suppose `E(X) = 3` and `Var(X) = 4`. Find `E(X²)` and `Var(2 − 3X)`.
6. A density is `f(x) = cx` on `[0, 2]` and zero elsewhere. Find `c`, `P(X > 1)`, and `P(X = 1)`.

[Check the diagnostic](#diagnostic-answers) after attempting all six.

## Study plan through Thursday

| Day | Time | Practice |
| --- | --- | --- |
| **Monday, Nov. 16** | 60 minutes | Do the diagnostic. Work through the expectation and variance example, then solve Fall Q4 and Q5. If you miss diagnostic Q3, work Chapter 3 #3.53 with the branch table below. |
| **Tuesday, Nov. 17** | 75 minutes | Drill model selection with Fall Q1–Q3. Then practice CDF jumps and continuous integration with Spring Q1 and the corrected Spring Q3 in the [worked solutions](<Exam 2 Worked Solutions.md>). |
| **Wednesday, Nov. 18** | 75 minutes | Try Spring Q1, Q2, Q4, and Q5 as a timed set. For Q5(a), prove the standard identity `Var(X) = E(X²) − [E(X)]²`. Use 50 minutes for the attempt and 25 to check it and redo missed setups from memory. |
| **Thursday, Nov. 19** | 15 minutes | Recall the five model cues, Bayes' rule, and the two linear transformation formulas. Check discrete tail endpoints and what a finite set means under a continuous density. |

**If you only have 45 minutes**, spend 8 on the diagnostic, 15 fixing your lowest-scoring topic, 15 on Fall Q4 or Spring Q4, and 7 redoing one mistake without the key.

Both 2022 exams ask for four complete questions out of five. Follow Thursday's instructions for question choice and timing. The priorities here come from the available notes, homework, and past exams. The current exam's full topic list is unconfirmed. [Fall 2022 Test 2](<241 Fall 2022 Test 2.pdf>) · [Spring 2022 Test 2](<241 Spring 2022 Test 2.pdf>)

## Choosing a probability model

Before writing a formula, finish the sentence **“X counts …”**. Then state whether the sample size is fixed or determined by a stopping rule.

| What X counts | Model | Probability of the stated outcome |
| --- | --- | --- |
| Successes in a fixed number `n` of independent trials with common success probability `p` | Binomial | `P(X = k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ` |
| Successes in `n` uniformly sampled items without replacement from `N` items containing `K` successes | Hypergeometric | `P(X = k) = C(K,k)C(N−K,n−k)/C(N,n)` |
| Trials through the first success, with independent trials at a common `p` | Geometric | `P(X = t) = (1−p)ᵗ⁻¹p`, for `t ≥ 1` |
| Trials through the `r`th success, with independent trials at a common `p` | Negative binomial | `P(X = t) = C(t−1,r−1)pʳ(1−p)ᵗ⁻ʳ`, for `t ≥ r` |
| Events with a Poisson mean `λ`, or successes approximated from a binomial with large `n` and small `p` | Poisson | `P(X = k) = exp(−λ) λᵏ/k!`. Use `λ = np` for the approximation. |

`C(n,k)` means “n choose k,” the number of ways to choose `k` positions or items from `n`. In a negative binomial problem, reserve the last trial for success. The combination factor chooses the other `r−1` successes among the first `t−1` trials.

**One experiment can produce two different random variables.** Roll a die three times. The number of 1s has a binomial distribution. For the sum to be 4, the rolls must be `(1,1,2)` in some order, so multiply the one-roll probabilities and count the three orders. This distinction is the main step in Fall Q4.

Useful shortcuts are `E(X) = np` and `Var(X) = np(1−p)` for a binomial, `E(X) = 1/p` for a geometric counting trials, and `E(X) = Var(X) = λ` for a Poisson. For “at least `k`,” try `1 − P(X ≤ k−1)`.

## Bayes and conditioning

**Multiply down a branch and add across branches that lead to the observation.** For disjoint, exhaustive cases `Hᵢ`, the total probability of evidence `E` is `P(E) = Σᵢ P(Hᵢ)P(E ∣ Hᵢ)`. Bayes divides the joint probability on the branch you want by that total. `P(Hⱼ ∣ E) = P(Hⱼ)P(E ∣ Hⱼ)/P(E)`.

Chapter 3 #3.53 asks about an offer following a letter of recommendation.

| Letter | P(letter) | P(offer given letter) | P(letter and offer) | P(letter and no offer) |
| --- | ---: | ---: | ---: | ---: |
| Strong | .7 | .8 | .56 | .14 |
| Moderate | .2 | .4 | .08 | .12 |
| Weak | .1 | .1 | .01 | .09 |
| Total | 1 | | **.65** | **.35** |

An offer has probability `.65`. Given an offer, the probability of a strong letter is `.56/.65`. Given no offer, it is `.14/.35`. The evidence after the vertical bar tells you which column to divide by. [October 20 homework](<HW/10-20-2026.md>)

In Fall Q2 and Spring Q4, a wheel or road is selected once. Compute the probability conditional on each choice, then take the weighted sum. A fresh selection for each trial would be a different experiment.

## PMFs, CDFs, and densities

- A discrete PMF gives `p(x) = P(X = x)`. All masses are nonnegative and sum to 1.
- A CDF gives `F(x) = P(X ≤ x)`. Every CDF is nondecreasing and right-continuous. For a discrete variable, the jump at `x` equals `F(x) − F(x⁻) = P(X = x)`, where `F(x⁻)` is the value approached from the left.
- A continuous PDF gives probability through area. Check `f(x) ≥ 0` and total integral 1. Integrate `f(x)` over the portion of the interval inside the support. Every individual point and every finite set have probability zero.

Suppose `X` takes `0, 1, 2` with masses `1/4, 1/2, 1/4`.

| Interval | CDF height |
| --- | ---: |
| `x < 0` | `0` |
| `0 ≤ x < 1` | `1/4` |
| `1 ≤ x < 2` | `3/4` |
| `x ≥ 2` | `1` |

To graph this, draw each level as a horizontal segment with a filled dot at its finite left endpoint and an open dot at its finite right endpoint. At `1`, the jump is `3/4 − 1/4 = 1/2`. The inclusive tail is `P(X ≥ 1) = 1 − F(1⁻) = 3/4`. The strict tail is `P(X > 1) = 1 − F(1) = 1/4`.

## Expectation and variance

For a discrete variable, `E[g(X)] = Σₓ g(x)p(x)`. To find `E(X²)`, square each possible value of `X` and weight it by its original probability. For a continuous variable, use the integral of `g(x)f(x)` over the support.

| Quantity | Formula |
| --- | --- |
| Mean after multiplying and shifting | `E(aX+b) = aE(X)+b` |
| Variance after multiplying and shifting | `Var(aX+b) = a²Var(X)` |
| Variance from the first two moments | `Var(X) = E(X²) − [E(X)]²` |
| Standard deviation | `sd(X) = √Var(X)` |

For the three-value PMF above, `E(X) = 0·(1/4) + 1·(1/2) + 2·(1/4) = 1` and `E(X²) = 0 + 1/2 + 4·(1/4) = 3/2`. This gives `Var(X) = 1/2`. So `E(3X−2) = 1` and `Var(3X−2) = 9/2`.

**When two expressions share the same X, combine them first.** If `Y = 2X+9` and `Z = 4−X`, then `Y−Z = 3X+5` and `Var(Y−Z) = 9Var(X)`. Variances of separate variables add when their covariance is zero, as with independent variables.

**For a proof**, let `μ = E(X)`. Expand the definition to get `E[(X−μ)²] = E(X²) − 2μE(X) + μ² = E(X²) − μ²`. To prove the scaling rule, center `aX+b` by subtracting `aμ+b`. The result is `a(X−μ)`, whose square contributes the factor `a²`. [Linear combinations handout](<241 Linear Combinations.pdf>) · [November 3 notes](<Notes/11-03-2026.md>)

## Corrections to use while studying

- In the October 20 Bayes example, the positive-test numerator is `.00475`. The posterior is `.00475/.0147 ≈ .3231`. In the insurance example, read `.4` and `.2` as probabilities of an accident **given** the driver's risk class. [October 20 notes](<Notes/10-20-2026.md>)
- In the October 22 CDF notes, the step function is **right-continuous**. The jump at a point between support values is zero. In the four-value example, the final interval starts at `x = 4` and extends rightward. [October 22 notes](<Notes/10-22-2026.md>)
- In the November 3 fair die example, keep fractions to avoid rounding drift. `Var(X) = 91/6 − (7/2)² = 35/12`. This gives `Var(E(X)X+1) = (7/2)²(35/12) = 1715/48 ≈ 35.7292`. [November 3 notes](<Notes/11-03-2026.md>)

For extra textbook practice, use Chapter 4 **Problems** #4.17–4.19 for PMFs and CDFs, then #4.21 and #4.38 together for expectation and variance. Try #4.35 for a payoff based on sampling without replacement and #4.42 for a binomial tail. The corresponding PDF pages are 279–284 in the local textbook. [A First Course in Probability](<../tenth_edition_a_first_course_in_probability.pdf>)

## Diagnostic answers

1. Hypergeometric. `C(5,2)C(7,1)/C(12,3) = 7/22 ≈ .3182`.
2. First on the fourth is `.7³(.3) = .1029`. Exactly one in four is `C(4,1)(.3)(.7³) = .4116`. Any one of the four attempts can contain the score in the second event.
3. `P(defect) = .5(.02) + .5(.08) = .05`. `P(B | defect) = .5(.08)/.05 = .80`.
4. The jump at 1 is `.7 − .2 = .5`. The tail including 1 is `1 − .2 = .8`.
5. `E(X²) = 4 + 3² = 13`. `Var(2−3X) = (−3)²(4) = 36`.
6. `1 = ∫₀² cx dx = 2c`, so `c = 1/2`. `P(X > 1) = ∫₁² x/2 dx = 3/4`. `P(X = 1) = 0`.
