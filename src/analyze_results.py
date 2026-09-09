import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../results/simulation_output.csv')

fig, axs = plt.subplots(2, 1, figsize=(10,8))
axs[0].plot(df['time'], df['velocity'])
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Velocity (m/s)')
axs[0].set_title('Vehicle Speed vs Drive Cycle')

axs[1].plot(df['time'], df['fuel'])
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Cumulative Fuel Used')
axs[1].set_title('Fuel Consumption Over Time')

plt.tight_layout()
plt.savefig('../results/summary_plot.png')
plt.show()

distance_km = (df['velocity'].sum() * df['time'].diff().mean()) / 1000
total_fuel = df['fuel'].iloc[-1]
print(f"Approx distance: {distance_km:.2f} km")
print(f"Total fuel used: {total_fuel:.2f} units")
print(f"Fuel per km: {total_fuel/distance_km:.2f} units/km")