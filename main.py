# Student: Line Lindskou Mogensen

### Scenario
    #In this assignment, you will use Monte Carlo simulation to help a retail company manage its inventory.
    # The company sells a single product, and the daily demand for this product is uncertain.
    # You will simulate the daily demand over a month (30 days) to help the company determine optimal inventory levels.

#### 1. Simulate Daily Demand and Analyze Results
#Write a function that simulates the daily demand for the product over the next n days using a Poisson distribution.
#**Steps:**
    # Assume the average daily demand (`λ`) is 20 units.
    # Use `numpy` to generate Poisson-distributed daily demand for n days.
#**Analyze the Results:**
    # Calculate and print the following statistics from the simulation results:
        #  Mean (average) daily demand
        #  Standard deviation
        #  5th percentile (to understand the lower bound in a worst-case scenario)
        #  95th percentile (to understand the upper bound in a best-case scenario)
    #  Interpret the results in the context of inventory management.

import random
import numpy as np

n = 30 
dailyDemand = 20

def simulate_n_days(n, dailyDemand):
    demands = []
    for i in range(n):
        demand = simulate_one_day(dailyDemand)
        demands.append(demand)
    mean_demand = np.mean(demands)
    std_demand = np.std(demands)
    p5 = np.percentile(demands, 5)
    p95 = np.percentile(demands, 95)
    return mean_demand, std_demand, p5, p95

def simulate_one_day(dailyDemand):
    return np.random.poisson(dailyDemand)

# Simulation
mean_demand, std_demand, p5, p95 = simulate_n_days(n, dailyDemand)

# Results
print(f"Average daily demand: {mean_demand}")
print(f"Standard deviation: {std_demand}")
print(f"5th percentile (low scenario): {p5}")
print(f"95th percentile (high scenario): {p95}")

### 2. Inventory Level Simulation
#Determine the optimal inventory level for one month that minimizes the risk of stockouts (running out of stock). Assume that there is no reordering during a month.
#**Steps:**
    # Assume the company wants to maintain a service level of 95%, meaning they want to meet the demand 95% of the time.
    #  Simulate the total demand for 30 days multiple times (e.g., 1,000 simulations) to understand the distribution of monthly demand.
    #  Determine the inventory level that would be sufficient to meet the demand 95% of the time.
    #  Calculate and print the optimal inventory level.

n_simulations = 1000
dailyDemand = 20
days_per_month = 30

def simulate_monthly_inventory(n_simulations, dailyDemand, days_per_month=30):
    monthly_totals = []
    for _ in range(n_simulations):
        total_demand = simulate_one_month(dailyDemand, days_per_month)
        monthly_totals.append(total_demand)
    
    inventory_level = np.percentile(monthly_totals, 95)
    return inventory_level, monthly_totals

def simulate_one_month(dailyDemand, days_per_month):
    daily_demands = np.random.poisson(dailyDemand, days_per_month)
    return np.sum(daily_demands)

# Simulation
inventory_level, monthly_totals = simulate_monthly_inventory(n_simulations, dailyDemand, days_per_month)

# Result
print(f"Optimal inventory: {inventory_level}")
