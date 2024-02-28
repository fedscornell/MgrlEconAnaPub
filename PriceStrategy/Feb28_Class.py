from scipy.optimize import minimize_scalar
# Define the profit function to be maximized
def profit(Q):
    return -(-Q**2 + 10*Q - 5)  # Negative because we use a minimization function
# Solve for Q that maximizes the profit
result = minimize_scalar(profit, bounds=(0, 10), method='bounded')
# Display the optimal quantity Q and the maximum profit
optimal_Q = result.x
max_profit = -result.fun

optimal_Q, max_profit
print("Q:",optimal_Q)
print("Profit:",max_profit)
