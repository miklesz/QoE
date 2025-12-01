import matplotlib.pyplot as plt

# Data for the bar chart
labels = ['HD', 'SD', 'SD + 200ms delay']
scores = [4.2, 3.0, 2.4]

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the bars with gray color
bars = ax.bar(labels, scores, color='gray')

# Add numerical labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}',               # formatted value (1 decimal place)
                xy=(bar.get_x() + bar.get_width() / 2, height),  # x, y position of label
                xytext=(0, 3),                 # vertical offset
                textcoords="offset points",
                ha='center', va='bottom')      # center alignment

# Set axis limits and labels
ax.set_ylim(1, 5)
ax.set_ylabel('Average QoE score (1–5)')
ax.set_title('User-perceived Quality of Experience (QoE)')

# Add horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure layout fits all elements
plt.tight_layout()

# Save the chart as a PNG image with high resolution
plt.savefig('qoe_bar_chart.png', dpi=300)

# Display the plot
plt.show()