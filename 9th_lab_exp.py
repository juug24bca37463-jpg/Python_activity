Aim

To create a dataset of weekly temperatures and display it using a line graph

Algorithm

1. Start
2. Import required libraries (pandas and matplotlib)
3. Create a dictionary with days of the week and corresponding temperatures
4. Convert the dictionary into a DataFrame
5. Plot the graph using days on the x-axis and temperature on the y-axis
6. Add labels for x-axis and y-axis
7. Give a title to the graph
8. Enable grid for better visualization
9. Display the graph
10. Stop

CODE:

# Data dictionary
data = {
    "Days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temperature": [30, 12, 31, 29, 28, 27, 26] # Adjusted to match a 7-day week
}

df = pd.DataFrame(data)

plt.plot(df["Days"], df["Temperature"], marker='o', linestyle='--', color='b')

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature over a week")
plt.grid(True)
plt.show()
Output:
  Days  Temperature
0  Mon           30
1  Tue           12
2  Wed           31
3  Thu           29
4  Fri           28
5  Sat           27
6  Sun           26

