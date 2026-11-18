# MTH 241 Exam 2 Practice Question Bank

## Independent trials

For each question, write what the event requires on each trial. Use `M` for a required miss and `?` when any outcome is allowed. If several mutually exclusive patterns qualify, find the probability of each pattern or count how many share the same probability.

### Die rolls

Use a fair six-sided die. All rolls are independent.

1. **Q1.** You roll the die four times. What is the probability the fourth roll is a 6?
2. **Q2.** You roll the die four times. What is the probability your first 6 occurs on the fourth roll?
3. **Q3.** What is the probability of at least one 6 in four rolls? Try writing a pattern for each possible position of the first 6. Mark what the later rolls are allowed to be.
4. **Q4.** What is the probability of exactly one 6 in four rolls? List all qualifying patterns and find the probability of one pattern before combining them.
5. **Q5.** What is the probability of exactly two 6s in four rolls? Write the probability of one qualifying pattern, then count how many patterns qualify.

### New settings

6. **Q6.** A player makes each free throw with probability .30, independently of the other throws. What is the probability they make exactly one of three free throws?
7. **Q7.** A biased coin lands on heads with probability .20. You flip it independently three times. What is the probability of at least one head?
8. **Q8.** Each independent trial has the same success probability `p`. Give expressions in terms of `p` for (a) a success on trial 5, (b) the first success on trial 5, and (c) exactly one success in five trials.

### Tickets and clear drives

A clear drive means a drive without a ticket. On a fixed road, assume drives are independent and the ticket probability is the same on each drive.

9. **Q9.** On road B, the ticket rate is 3 in 7. What is the chance of a ticket on one drive? What is the chance of a clear drive? Start by filling in these counts. Out of seven slips, three say “ticket” and ___ say “clear.”
10. **Q10.** You take three drives on road B. What is the probability of the specific sequence `ticket, clear, clear`? Write one fraction for each drive, then combine matching factors using exponents.
11. **Q11.** On those three drives on road B, what is the probability of exactly one ticket? List the positions that can hold the ticket. Use your answer to Q10 to find the total probability.
12. **Q12.** A city picks road A with probability `1/3` and road B with probability `2/3`. Road A has a ticket rate of 2 in 5 and road B has a rate of 3 in 7. You drive on the one road that was picked three times. What is the probability of exactly one ticket? First find the probability on each road, then weight the two results by the chances of picking their roads.

[Check Q1–Q12](#answer-key) after trying a setup.

## Exam-style practice

Before calculating, write one sentence saying **what must happen** or **what quantity you need**. For a probability, mark each outcome that is required and each one that can vary. If the question says “given,” write what you already know. Then write the setup and justify why it fits.

Start with **Q13, Q15, and Q16** to practice reading the event. For a mixed review, add **Q14, Q20, Q21, and Q22**. For longer problems that combine several steps, use **Q17, Q18, Q19, Q23, and Q26**.

### Q13 Late deliveries

Three deliveries are made. Each delivery is late with probability `.20`, independently of the others. For each part, write what is required of deliveries 1, 2, and 3 before finding the probability.

a. The third delivery is late.  
b. The first late delivery is the third delivery.  
c. Exactly one delivery is late.  
d. At least one delivery is late.

### Q14 Selecting from a roster

Twelve volunteers have badges numbered 1 through 12. Five of the volunteers are certified. For each part, select the stated number of volunteers uniformly at random without replacement.

a. What is the probability exactly two of the four volunteers selected are certified?  
b. Two volunteers are selected. What is the probability their badge numbers sum to 9?

### Q15 Choosing an oven

A bakery chooses oven A with probability `3/4` or oven B with probability `1/4`. It uses the chosen oven for all three batches. A batch is overdone with probability `1/5` on A or `1/2` on B. The batches are independent once the oven is known.

a. What is the probability exactly two batches are overdone?  
b. You learn that exactly two batches were overdone. What is the probability the bakery used B?

### Q16 Stopping at the third success

Each independent attempt opens a lock with probability `1/4`. The experiment ends as soon as the lock has been opened three times. Let `N` be the total number of attempts.

a. Find `P(N = 5)`.  
b. Find `P(N ≥ 5)`. Which outcomes in the first four attempts make the experiment continue?

### Q17 A best-of-five series

Teams A and B play until one team has won three games. Games are independent and A wins each game with probability `.60`.

a. What is the probability **B wins the series in exactly four games**?  
b. What is the probability **the series lasts exactly four games**?  
c. Find the distribution and expected value of the number of games played.

### Q18 A game with an entry fee

You pay 11 dollars to play. You take up to three independent shots, each with a `1/3` chance of hitting. Play stops at the first hit. A first hit on shot 1, 2, or 3 pays 18, 12, or 3 dollars, respectively. Three misses pay zero.

a. What is the probability you finish with a strictly positive net gain?  
b. What is your expected net gain? Explain what your two answers say about the game.

### Q19 Failures in two samples

In a batch of 200 independent requests, each request fails with the same small probability `p`. Under a Poisson approximation, exactly two failures are 1.5 times as likely as exactly one failure.

a. Find the Poisson mean `λ` and estimate the per-request failure probability `p`.  
b. Use the Poisson model to estimate the probability of at least three failures in a batch of 200 requests.  
c. A new batch has only eight requests with the same failure rate. Use your estimated `p` to write the binomial expression for exactly one failure in this batch.

### Q20 A discrete wait time

The CDF of a wait time `X` is given below.

| Interval for x | F(x) |
| --- | ---: |
| x < 0 | 0 |
| 0 ≤ x < 1 | .15 |
| 1 ≤ x < 3 | .55 |
| 3 ≤ x < 4 | .90 |
| x ≥ 4 | 1 |

a. List the possible wait times and the probability of each.  
b. Find both `P(X ≥ 3)` and `P(X > 3)`.  
c. Find `E(X)`.

### Q21 A continuous wait time

The density of `X` is `f(x) = kx(2−x)` on `[0,2]` and zero elsewhere.

a. Find `k` and check that the resulting function is a valid density.  
b. Find `P(1.5 ≤ X < 3)`.  
c. Find `P(X ∈ {0.5, 1, 1.5})` and `E(X)`.

### Q22 Expressions built from the same variable

Let `Y = 3X−2` and `Z = 5−X`. You are told that `E(Y+Z) = 11` and `Var(Y−Z) = 48`.

a. Find `E(X²)`.  
b. Now let `W` be an independent copy of `X`. Find `Var(3X−W)`. Explain where independence enters your calculation.

### Q23 One machine for five runs

A lab selects machine A with probability `1/4` or machine B with probability `3/4` and uses it for all five runs. The per-run success probabilities are `.20` on A and `.60` on B. The runs are independent given the machine. Let `X` count successes across the five runs.

a. Find `E(X)` before you learn which machine was selected.  
b. Find `Var(X)`. Try finding `E(X²)` on each machine first.  
c. You see that the first run succeeds. What is the probability the second run also succeeds?

### Q24 Proving the variance rule

Assume `X` has a finite second moment.

a. Starting with `Var(X) = E[(X−E(X))²]`, prove `Var(3X−2) = 9Var(X)`.  
b. Explain why `E(X²) ≥ [E(X)]²`. When does equality hold?

### Q25 Checking a proposed distribution

a. A table lists `.28, .45, .35` as the probabilities of `X = 0, 1, 2`, respectively, with zero elsewhere. Check that claim. If the entries are intended as proportional weights, turn them into probabilities and find `P(X ≥ 1)`.  
b. Can `f(x) = k(1−x)` on `[0,2]` and zero elsewhere be a density for any real value of `k`? Justify your answer.

### Q26 Two students on the same quiz

Five questions are scored separately for each student. On each question, Mia answers correctly with probability `.80` and Jay answers correctly with probability `.50`. Assume all ten student responses are independent.

a. What is the expected number of questions **both** students get right?  
b. What are the mean and variance of the **total number of correct responses** across both students? A question that both students get right contributes two responses.  
c. What is the probability that on exactly four of the five questions, **at least one** student answers correctly?

[Check Q13–Q26](#exam-style-answers) after writing your setups.

## Answer key

### Independent trials

1. **Q1.** The event looks like `? ? ? 6`. Only roll 4 is specified, so the probability is **1/6**.
2. **Q2.** The event looks like `M M M 6`. Multiply the four required outcomes to get **`(5/6)³(1/6) = 125/1296`**.
3. **Q3.** Sort the outcomes by where the first 6 occurs. The four patterns are `6 ? ? ?`, `M 6 ? ?`, `M M 6 ?`, and `M M M 6`. Each set of rolls with a 6 belongs to exactly one of these patterns, so add `(1/6) + (5/6)(1/6) + (5/6)²(1/6) + (5/6)³(1/6)`. This is **`671/1296`**, which you can also get from `1 − (5/6)⁴`.
4. **Q4.** The four patterns are `6 M M M`, `M 6 M M`, `M M 6 M`, and `M M M 6`. Multiply within each row to get `(1/6)(5/6)³`. Add the four row probabilities to get **`4(1/6)(5/6)³ = 125/324`**.
5. **Q5.** An example is `6 M 6 M`, with probability `(1/6)²(5/6)²`. Choose two of the four positions for the 6s. There are `C(4,2) = 6` choices, so the answer is **`6(1/6)²(5/6)² = 25/216`**.
6. **Q6.** The made shot can occupy any of the three positions. Each pattern has probability `.30(.70)²`, so the answer is **`3(.30)(.70)² = .441`**.
7. **Q7.** No heads means three tails, with probability `.80³`. Subtract from 1 to get **`1 − .80³ = .488`**.
8. **Q8.** (a) Trial 5 is the only specified trial, so the answer is **`p`**. (b) Four misses followed by success gives **`(1−p)⁴p`**. (c) The success can occupy any of five positions, each with four misses, so the answer is **`5p(1−p)⁴`**.

### Tickets and clear drives

9. **Q9.** Three slips say “ticket” and `7−3 = 4` say “clear.” The probabilities are **`3/7` for a ticket** and **`4/7` for a clear drive**.
10. **Q10.** Multiply the factors in order. **`(3/7)(4/7)(4/7) = (3/7)¹(4/7)² = 48/343`**. There is one ticket factor and two clear factors.
11. **Q11.** The ticket can appear on drive 1, 2, or 3. Each of those three patterns has the probability from Q10. Add them to get **`3(48/343) = 144/343`**.
12. **Q12.** On road A, one pattern has probability `(2/5)(3/5)²`, and there are three places for the ticket. This gives `3(2/5)(3/5)² = 54/125`. On road B, Q11 gives `144/343`. Multiply each by the chance of picking its road, then add. The total is **`(1/3)(54/125) + (2/3)(144/343) = 18174/42875`**.

## Exam-style answers

When checking your work, mark where the first difference occurred. If you chose a different event or model, redo that first line before checking the arithmetic.

### Q13 Late deliveries

Use `L` for late, `C` for on time, and `?` for either outcome.

- **(a)** `? ? L` gives **`.20`**.
- **(b)** `C C L` gives **`.80²(.20) = .128`**.
- **(c)** The qualifying patterns are `L C C`, `C L C`, and `C C L`. Add their equal probabilities to get **`3(.128) = .384`**.
- **(d)** The only pattern with zero late deliveries is `C C C`. The complement gives **`1 − .80³ = .488`**.

### Q14 Selecting from a roster

- **(a)** Count groups with two certified and two other volunteers. The probability is **`C(5,2)C(7,2)/C(12,4) = 14/33`**.
- **(b)** The qualifying unordered pairs are `(1,8), (2,7), (3,6), (4,5)`. Divide by the number of equally likely pairs to get **`4/C(12,2) = 2/33`**.

### Q15 Choosing an oven

Let `D` be the event that exactly two batches are overdone. In each oven branch, two of the three batch positions must be overdone. Then multiply by the chance of choosing the oven.

| Oven | P(D given oven) | P(oven and D) |
| --- | ---: | ---: |
| A | `C(3,2)(1/5)²(4/5) = 12/125` | `(3/4)(12/125) = 9/125` |
| B | `C(3,2)(1/2)²(1/2) = 3/8` | `(1/4)(3/8) = 3/32` |

- **(a)** Add the joint probabilities. **`P(D) = 9/125 + 3/32 = 663/4000`**.
- **(b)** Among outcomes in `D`, use B's share. **`P(B given D) = (3/32)/(663/4000) = 125/221`**.

### Q16 Stopping at the third success

- **(a)** Attempt 5 must succeed, with exactly two successes among the first four attempts. The probability is **`C(4,2)(1/4)³(3/4)² = 27/512`**.
- **(b)** To need at least five attempts, there can be at most two successes in the first four. The complement is at least three successes in four trials, which includes either three successes or four. Imagine the first four trial outcomes being generated even if the experiment stops early. The answer is **`1 − [C(4,3)(1/4)³(3/4) + (1/4)⁴] = 243/256`**.

### Q17 A best-of-five series

- **(a)** B wins game 4 and exactly two of the first three games. **`C(3,2)(.40)³(.60) = .1152`**.
- **(b)** Either team can win in four. A's branch is `C(3,2)(.60)³(.40) = .2592`. The total is **`.1152 + .2592 = .3744`**.
- **(c)** The series lasts three games if one team sweeps, with probability `.60³ + .40³ = .28`. It lasts five games if the first four are split 2–2, with probability `C(4,2)(.60)²(.40)² = .3456`. So the probabilities of 3, 4, and 5 games are `.28, .3744, .3456`, respectively. The expected number is **`3(.28) + 4(.3744) + 5(.3456) = 4.0656`**.

### Q18 A game with an entry fee

The probabilities of a first hit on shots 1, 2, and 3 are `1/3, 2/9, 4/27`. Three misses have probability `8/27`.

- **(a)** The 18- and 12-dollar payouts cover the 11-dollar fee and leave a profit. **`P(net gain > 0) = 1/3 + 2/9 = 5/9`**.
- **(b)** Weight the payouts and then subtract the fee. **`E(net gain) = 18(1/3) + 12(2/9) + 3(4/27) − 11 = −17/9` dollars**. You finish ahead a little more than half the time. Losing outcomes are costly enough to make the average net gain negative.

### Q19 Failures in two samples

- **(a)** Dividing the two-failure Poisson mass by the one-failure mass gives `λ/2`. Set that equal to `1.5` to get **`λ = 3`**. Using `λ = 200p` gives **`p ≈ 3/200 = .015`**.
- **(b)** Subtract the probabilities of zero, one, and two failures. **`1 − exp(−3)(1 + 3 + 3²/2!) ≈ .57681`**.
- **(c)** Choose one of the eight request positions for the failure. With the estimated rate, the binomial expression is **`C(8,1)(.015)(.985)⁷`**.

### Q20 A discrete wait time

- **(a)** Masses are the sizes of the jumps. At `0, 1, 3, 4`, they are **`.15, .40, .35, .10`**, respectively.
- **(b)** The inclusive tail includes the jump at 3, so **`P(X ≥ 3) = 1 − .55 = .45`**. The strict tail begins after that jump, so **`P(X > 3) = 1 − .90 = .10`**.
- **(c)** Weight each value by its mass. **`E(X) = 0(.15) + 1(.40) + 3(.35) + 4(.10) = 1.85`**.

### Q21 A continuous wait time

- **(a)** The integral of `x(2−x)` from 0 to 2 is `[x² − x³/3]₀² = 4/3`. Set `k(4/3) = 1` to get **`k = 3/4`**. Both `x` and `2−x` are nonnegative on the support.
- **(b)** Only the interval from 1.5 to 2 lies inside the support. Integrating gives **`(3/4)[x² − x³/3]₁.₅² = 5/32`**.
- **(c)** A finite set of points has probability **`0`**. The mean is the integral of `xf(x)`. It equals **`(3/4)[2x³/3 − x⁴/4]₀² = 1`**.

### Q22 Expressions built from the same variable

- **(a)** Simplify first to get `Y+Z = 2X+3` and `Y−Z = 4X−7`. Then `E(X) = (11−3)/2 = 4` and `Var(X) = 48/4² = 3`. So **`E(X²) = 3 + 4² = 19`**.
- **(b)** Independence makes the covariance of `X` and `W` zero, so the variances of the scaled terms add. The answer is **`3²Var(X) + (−1)²Var(W) = 27 + 3 = 30`**.

### Q23 One machine for five runs

Each machine gives a binomial count conditional on its selection. Work out the two conditional means and second moments before averaging.

| Machine | E(X given machine) | Var(X given machine) | E(X² given machine) |
| --- | ---: | ---: | ---: |
| A | 1 | .80 | `.80 + 1² = 1.80` |
| B | 3 | 1.20 | `1.20 + 3² = 10.20` |

- **(a)** **`E(X) = (1/4)(1) + (3/4)(3) = 2.5`**.
- **(b)** `E(X²) = (1/4)(1.80) + (3/4)(10.20) = 8.10`. Then **`Var(X) = 8.10 − 2.5² = 1.85`**.
- **(c)** A first success is more likely on B. By Bayes, the probability of B given that first success is `[(3/4)(.60)]/[(1/4)(.20) + (3/4)(.60)] = .90`. Weight the second-run probabilities using these updated chances for A and B. The probability is **`.10(.20) + .90(.60) = .56`**.

### Q24 Proving the variance rule

- **(a)** Put `μ = E(X)`. The mean of `3X−2` is `3μ−2`, so the centered value is `(3X−2) − (3μ−2) = 3(X−μ)`. Squaring and taking the expectation gives **`E[9(X−μ)²] = 9Var(X)`**.
- **(b)** Expanding the centered square gives `E(X²) − [E(X)]² = E[(X−μ)²]`. This is nonnegative because every squared term is nonnegative. Equality holds exactly when **`X = μ` with probability 1**.

### Q25 Checking a proposed distribution

- **(a)** The three entries sum to `1.08`. Probabilities over all possible values must sum to 1. As weights, divide each by `1.08`. The last two then give **`P(X ≥ 1) = (.45 + .35)/1.08 = 20/27`**.
- **(b)** `1−x` is positive below 1 and negative above 1 on the support, so any nonzero `k` makes the proposed density negative somewhere. For `k = 0`, the total area is zero. **There is no valid value of `k`.**

### Q26 Two students on the same quiz

- **(a)** Each question has probability `.80(.50) = .40` of both students getting it right. The expected count is **`5(.40) = 2`**.
- **(b)** Add the two students' counts. Their means add to **`5(.80) + 5(.50) = 6.5`**. Since the counts are independent, the variances add to **`5(.80)(.20) + 5(.50)(.50) = 2.05`**.
- **(c)** On one question, the chance at least one is correct is `1 − (.20)(.50) = .90`. Choose the four questions with this outcome to get **`C(5,4)(.90)⁴(.10) = .32805`**.

### Past paper connections

Fall Q1–Q4 cover model selection, stopping times, Poisson, and counting successes. Fall Q5 covers expectation and variance with expressions built from one variable. [Fall 2022 Test 2](<241 Fall 2022 Test 2.pdf>)

Spring Q1 and Q3 cover continuous and discrete distributions. Spring Q2 and Q4 combine probability with stopping rules or a choice made once for the whole experiment. [Spring 2022 Test 2](<241 Spring 2022 Test 2.pdf>)
