import matplotlib as plt

fig, ax = plt.subplots()

#Example for Objects

vegies = ["tomato", "brinjal", "capsicum", "carrot"]
counts = [120, 20, 30, 50]
bar_lables = ["red", "blue", "red", "orange"]
bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

ax.bar(vegies, counts, label = bar_lables, color = bar_colors)

ax.set_ylabel("vegies supply")
ax.set_title("Vegies upply by kind & color")
ax.legend(title = "Vegies color")
plt.savefig("bars.png", bbox_inches = "tight")


#Example for Human

man = ["bore", "happy", "happy", "haapy", "bore", "happy"]
women = ["bore", "bore", "bore", "happy", "happy", "bore"]
activity = ["drinking", "feeding", "fasting", "napping", "playing", "washing"]


fig, ax = plt.subplots()
ax.plot(activity, man, label="man")
ax.plot(activity, women, label="women")
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')