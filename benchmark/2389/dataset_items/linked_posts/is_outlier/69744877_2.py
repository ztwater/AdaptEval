# Imports
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

# Plot Original Series
time_series.plot(style = 'k-')
plt.title('Original Series')
plt.show()
    
# Plot Cleaned Series
filtered_d.plot(style = 'k-')
plt.title('Cleaned Series (Without detected Outliers)')
plt.show()
