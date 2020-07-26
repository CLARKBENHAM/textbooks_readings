import numpy as np

vol = 0.3
vol_of_vol = 1
daily_growth = 1.08**(1/252)
n_trials = 1000

nvov = [[np.random.normal(daily_growth, vol) for _ in range(252)]
                   for _ in range(n_trials)]
lognorm_m = np.exp(0.5*vol_of_vol**2)
yvov = [[np.random.normal(daily_growth,
                         vol*np.random.lognormal(0, vol_of_vol) / lognorm_m)
             for _ in range(252)]
        for _ in range(n_trials)]

#no vol of vol
vol_swap_nvov = np.mean([np.std(l) for l in nvov])
vol_swap_yvov = np.mean([np.std(l) for l in yvov])
print(f"Vol Convexity: {vol_swap_yvov - vol_swap_nvov}")

var_swap_nvov = np.mean([np.var(l) for l in nvov])
var_swap_yvov = np.mean([np.var(l) for l in yvov])
print(f"Var Convexity: {var_swap_yvov - var_swap_nvov}")
print(f"Realized Price of Vol-of-Vol: {np.sqrt(var_swap_yvov) - vol_swap_yvov}")
#Via Jensen's criteria

