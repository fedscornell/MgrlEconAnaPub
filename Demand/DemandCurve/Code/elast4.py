import numpy as np
import matplotlib.pyplot as plt

# Define price range
price_range = np.linspace(0.1, 10, 100)

# Demand functions
def perfectly_inelastic_demand(price):
    return np.ones_like(price) * 5  # Constant demand

def constant_elasticity_demand(price, elasticity):
    return 10 * price ** elasticity  # Constant elasticity demand

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot Perfectly Inelastic Demand
axs[0, 0].plot(price_range, perfectly_inelastic_demand(price_range), label='Perfectly Inelastic')
axs[0, 0].set_title('Perfectly Inelastic Demand')
axs[0, 0].set_xlabel('Price')
axs[0, 0].set_ylabel('Quantity')
axs[0, 0].legend()

# Plot Perfectly Elastic Demand
corresponding_range = np.full_like(price_range, 10)
axs[0, 1].plot(corresponding_range,price_range,  label='Perfectly Elastic')
axs[0, 1].set_title('Perfectly Elastic Demand')
axs[0, 1].set_xlabel('Price')
axs[0, 1].set_ylabel('Quantity')
axs[0, 1].legend()

# Plot Constant Elasticity Demand with elasticity = -1
axs[1, 0].plot(price_range, constant_elasticity_demand(price_range, -1), label='Elasticity = -1')
axs[1, 0].set_title('Constant Elasticity Demand (Elasticity = -1)')
axs[1, 0].set_xlabel('Price')
axs[1, 0].set_ylabel('Quantity')
axs[1, 0].legend()

# Plot Constant Elasticity Demand with elasticity = -0.4
axs[1, 1].plot(price_range, constant_elasticity_demand(price_range, -0.4), label='Elasticity = -0.4')
axs[1, 1].set_title('Constant Elasticity Demand (Elasticity = -0.4)')
axs[1, 1].set_xlabel('Price')
axs[1, 1].set_ylabel('Quantity')
axs[1, 1].legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

