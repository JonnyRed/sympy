# Random Variable

* A __random variable__ is a variable whose possible values are
numerical outcomes of a random phenomenon.
* A random variable is discrete if it can take only a countable number
of distinct values and it is continuous if it can take an infinite
number of possible values.
* A probability distribution specifies the probabilities for each of
the values that a random variable may take.
* A probability distribution of a discrete random variable is
called a __probability mass function__ and gives probabilities on
the y-axis.
* A probability distribution of a continuous random variable is
called a __probability density function__ and gives probability
densities on the y-axis, in this case probabilities are given
by the surface area under the curve within a specified interval.
* A probability density function can exist in the form of a table,
a graph and an equation.

# Cumulative Probability

* A __cumulative probability__ of a random variable is the probability
of obtaining a value lower than or equal to a threshold-value.
* Considered in the other direction, a cumulative probability specifies
a quantile of the random variable, for example at the cumulative
probability of oh point five the median of the random variable is found.
* Just like a probability distribution, the cumulative probability
distribution can exist in the form of a table, a graph or an equation.
* It can be obtained by calculating a cumulative sum of the
probabilities from the smallest up to the largest value of the
random variable.
* And it is continuously increasing with an increasing value for the
random variable, starting at zero and incrementing to a probability
of one.

# Sampling

In statistics, there are two main forms of sampling:
__probability sampling__ and __non-probability sampling__.


* **Probability sampling** is a method of sampling where every member of
the population has a known chance of being selected. This is the most
reliable type of sampling, as it minimizes the risk of bias. There are
four main types of probability sampling:
    * **Simple random sampling:** This is the simplest form of
    probability sampling. Every member of the population has an equal
    chance of being selected.

    * **Systematic sampling:** This is a type of probability sampling
    where every kth member of the population is selected. For example,
    if you wanted to select a sample of 100 people from a population of
    1000 people, you would select every 10th person on the list.

    * **Stratified sampling:** This is a type of probability sampling
    where the population is divided into strata, or groups, and then
    a sample is selected from each stratum. This ensures that the
    sample is representative of the population as a whole.

    * **Cluster sampling:** This is a type of probability sampling
    where the population is divided into clusters, or groups, and then
    a sample of clusters is selected. The members of the selected
    clusters are then included in the sample.

* **Non-probability sampling** is a method of sampling where not every
member of the population has a known chance of being selected. This
type of sampling is less reliable than probability sampling, but it
is often used when it is not possible to use probability sampling.
There are several types of non-probability sampling:

    * **Convenience sampling:** This is a type of non-probability
    sampling where the sample is selected based on convenience.
    For example, a researcher might survey the first 100 people they
    see walking down the street.
    * **Voluntary response sampling:** This is a type of
    non-probability sampling where the sample is selected based on
    whether or not people volunteer to participate. For example,
    a researcher might place an ad in the newspaper asking people
    to participate in a survey.

    * **Purposive sampling:** This is a type of non-probability
    sampling where the sample is selected based on the researcher's
    judgment. For example, a researcher might select a sample of
    people who are experts in a particular field.

    * **Quota sampling:** This is a type of non-probability sampling
    where the sample is selected to represent different groups in the
    population. For example, a researcher might select a sample of
    people that is representative of different age groups, genders,
    and income levels.

The best type of sampling method to use depends on the specific
research question being asked. If it is important to have a
representativesample of the population, then probability sampling is the
best option. However, if it is not possible to use probability
sampling, then non-probability sampling may be the only option.

# p-value

The p-value is a statistical measure that provides evidence against the
null hypothesis in a hypothesis test. In the context of correlation
analysis, the p-value associated with the correlation coefficient
indicates the statistical significance of the observed correlation.

Here's what the p-value signifies:

1. Null Hypothesis (H0): The null hypothesis in correlation analysis
states that there is no significant correlation between the variables
in the population.

2. Alternative Hypothesis (H1): The alternative hypothesis suggests
that there is a significant correlation between the variables in the
population.

3. Significance Level ($\alpha$): The significance level, commonly
denoted as $\alpha$, is a pre-defined threshold used to determine
statistical significance. It represents the probability of rejecting
the null hypothesis when it is true. The most common significance
levels are 0.05 (5%) and 0.01 (1%).

4. Interpreting the p-value:
* If the p-value is less than the chosen significance level
($p-value < \alpha$), it provides evidence to reject the null hypothesis.
This suggests that the observed correlation is statistically significant,
and there is a strong likelihood that a true correlation exists in
the population.
* If the p-value is greater than or equal to the chosen significance
level (p-value \ge \alpha$), it does not provide sufficient evidence
to reject the null hypothesis. This suggests that the observed
correlation is not statistically significant, and there is
insufficient evidence to conclude that a true correlation exists in
the population.

In summary, the p-value helps determine whether the observed
correlation is statistically significant or if it could be due to
random chance. A low p-value (typically below the chosen
significance level) indicates a significant correlation, while a
high p-value suggests that the observed correlation could be due to
sampling variability or chance.

It's important to note that the p-value is not a measure of the strength
or magnitude of the correlation itself. It only assesses the
statistical significance of the observed correlation based on the
given data and the chosen significance level.

# Product Moment Correlation Coefficient

The product moment correlation coefficient, also known as the __Pearson
correlation coefficient__, is a measure of the strength and direction
of the linear relationship between two continuous variables.
It quantifies how closely the data points of the two variables
align around a straight line.

The Pearson correlation coefficient is a value between -1 and 1.
Here's what different values of the correlation coefficient indicate:

* A correlation coefficient of 1: It represents a perfect positive
linear relationship. This means that as one variable increases,
the other variable also increases in a proportional manner.
* A correlation coefficient close to 1: It indicates a strong positive
linear relationship. The variables tend to move in the same direction,
but there may be some variability.
* A correlation coefficient close to 0: It suggests little to no
linear relationship between the variables. The variables are not
significantly related to each other.
* A correlation coefficient close to -1: It suggests a strong negative
linear relationship. As one variable increases, the other variable
decreases in a proportional manner.
* A correlation coefficient of -1: It represents a perfect negative
linear relationship. The variables have a perfect inverse relationship,
meaning that as one variable increases, the other variable decreases
in a perfectly predictable manner.

It's important to note that the correlation coefficient only measures
the linear relationship between variables. It may not capture
non-linear relationships or other complex patterns in the data.
Additionally, correlation does not imply causation, meaning that
a high correlation does not necessarily imply a cause-and-effect
relationship between the variables.

Overall, the product moment correlation coefficient is a valuable statistic that helps quantify and interpret the linear relationship between two continuous variables.

## Interpreting the p-value in Pearson

Interpreting the p-value:

The p-value represents the probability of observing a correlation
coefficient as extreme as the one calculated (or even more extreme)
under the null hypothesis that there is no correlation between the
two variables. A smaller p-value indicates stronger evidence
against the null hypothesis.


# Distributions

## Normal Distribution

In statistics, a normal distribution is a type of continuous probability
distribution that is symmetrical around its mean, most of the
observations cluster around the central peak, and the probabilities
for values further away from the mean taper off equally in both
directions. It is also known as the Gaussian distribution or the
bell curve.

The normal distribution is one of the most important distributions
in statistics because it is used to model a wide variety of
real-world phenomena, such as heights, weights, IQ scores, and
test scores. It is also used in many statistical tests, such as the
t-test and the z-test.

The normal distribution is defined by two parameters: the mean and
the standard deviation. The mean is the average value of the
distribution, and the standard deviation is a measure of how spread
out the values are.

A normal distribution with a mean of 0 and a standard deviation of 1
is called a standard normal distribution. This distribution is often
used as a reference point for other normal distributions.

Here are some examples of variables that are normally distributed:

* Height
* Weight
* IQ scores
* Blood pressure
* Temperature
* Reaction time

The normal distribution is a powerful tool for understanding and
analyzing data. It is used in a wide variety of fields, including
statistics, engineering, finance, and medicine.

Here are some of the uses of the normal distribution:

* To model the distribution of continuous variables in nature.
* To construct confidence intervals and hypothesis tests.
* To compare different populations.
* To make predictions about future events.
* To optimize systems.

### erf function

The error function, often denoted by $\mathrm{erf}$, is a mathematical
function that describes the probability that a
__standard normal variable__ will be less than a certain value.
It is defined as:

$$ {erf} (x) = \frac{2} {\sqrt \pi} \int_0^x e^{-t^2} dt $$


where $x$ is a real number.

The error function has a number of important properties, including:

* It is an odd function, meaning that erf(-x) = -erf(x).
* It is asymptotic to 0 as x approaches positive or negative infinity.
* It reaches a maximum value of 1 at x = 0.
* It is used in a variety of statistical applications, such as
calculating the probability that a standard normal variable will be
within a certain range.

For python an $x$ value of $0.5$ $erf_x = \mathrm{math.erf} (0.5)$ ,
calculates the error function for the value $x = 0.5$. The output of
this code,  0.5204998778130465, is the probability that a
standard normal variable  will be less than 0.5.

In other words, if you take a large number of standard normal variables,
about 52.05% of them will be less than 0.5.

The error function is a useful tool for understanding and analyzing
data that is normally distributed. It can be used to calculate the
probability that a variable will fall within a certain range, to
compare different populations, and to make predictions about
future events.

### Standard normal variable

A __standard normal variable__, also known as a
__standard normal random variable__ or a __Z-score__, is a random variable
that has been standardized to have a mean of 0 and a standard deviation
of 1. It is derived from a normal distribution by transforming the
original data into a new variable with these standard characteristics.

Given a normally distributed random variable $X$ with mean $mu$ and
standard deviation $\sigma$ the standard normal variable $Z$ is obtained
by applying the following transformation:

$$ Z = \frac{X - \mu}{\sigma} $$

Here, $Z$ follows a standard normal distribution, which is also called
the Z-distribution or the standard Gaussian distribution. This
distribution has a bell-shaped curve like the regular
normal distribution, but it has a mean of 0 and a standard deviation
of 1. The probability density function (PDF) of the standard normal
distribution is denoted by $\phi(z)$:

$$ \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}$$

The standard normal distribution is widely used in statistics and
hypothesis testing. It allows us to standardize data from different
normal distributions, making it easier to compare and analyze values
across different scales. The concept of Z-scores is particularly useful
in determining how many standard deviations a data point is away from
the mean. This information can be used to calculate probabilities,
identify outliers, and perform various statistical analyses.
