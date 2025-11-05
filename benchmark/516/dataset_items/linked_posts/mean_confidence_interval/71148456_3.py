"""
Review for confidence intervals. Confidence intervals say that the true mean is inside the estimated confidence interval
(the r.v. the user generates). In particular it says:
    Pr[mu^* \in [mu_n +- t.val(p) * std_n / sqrt(n) ] ] >= p
e.g. p = 0.95
This does not say that for a specific CI you compute the true mean is in that interval with prob 0.95. Instead it means
that if you surveyed/sampled 100 data sets D_n = {x_i}^n_{i=1} of size n (where n is ideally >=30) then for 95 of those
you'd expect to have the truee mean inside the CI compute for that current data set. Note you can never check for which
ones mu^* is in the CI since mu^* is unknown. If you knew mu^* you wouldn't need to estimate it. This analysis assumes
that the the estimator/value your estimating is the true mean using the sample mean (estimator). Since it usually uses
the t.val or z.val (second for the standardozed r.v. of a normal) then it means the approximation that mu_n ~ gaussian
must hold. This is most likely true if n >= 0. Note this is similar to statistical learning theory where we use
the MLE/ERM estimator to choose a function with delta, gamma etc reasoning. Note that if you do algebra you can also
say that the sample mean is in that interval but wrt mu^* but that is borning, no one cares since you do not know mu^*
so it's not helpful.

An example use could be for computing the CI of the loss (e.g. 0-1, CE loss, etc). The mu^* you want is the expected
risk. So x_i = loss(f(x_i), y_i) and you are computing the CI for what is the true expected risk for that specific loss
function you choose. So mu_n = emperical mean of the loss and std_n = (unbiased) estimate of the std and then you can
simply plug in the values.

Assumptions for p-CI:
    - we are making a statement that mu^* is in mu+-pCI = mu+-t_p * sig_n / sqrt n, sig_n ~ Var[x] is inside the CI
    p% of the time.
    - we are estimating mu^, a mean
    - since the quantity of interest is mu^, then the z_p value (or p-value, depending which one is the unknown), is
    computed using the normal distribution.
    - p(mu) ~ N(mu; mu_n, sig_n/ sqrt n), vial CTL which holds for sample means. Ideally n >= 30.
    - x ~ p^*(x) are iid.

Std_n vs t_p*std_n/ sqrt(n)
    - std_n = var(x) is more pessimistic but holds always. Never shrinks as n->infity
    - but if n is small then pCI might be too small and your "lying to yourself". So if you have very small data
    perhaps doing std_n for the CI is better. That holds with prob 99.9%. Hopefuly std is not too large for your
    experiments to be invalidated.

ref:
    - https://stats.stackexchange.com/questions/554332/confidence-interval-given-the-population-mean-and-standard-deviation?noredirect=1&lq=1
    - https://stackoverflow.com/questions/70356922/what-is-the-proper-way-to-compute-95-confidence-intervals-with-pytorch-for-clas
    - https://www.youtube.com/watch?v=MzvRQFYUEFU&list=PLUl4u3cNGP60hI9ATjSFgLZpbNJ7myAg6&index=205
"""
