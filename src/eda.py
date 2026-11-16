import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_tickets.csv")

total_tickets = len(df)
print("Total number of tickets:", total_tickets)

category_counts=df["category"].value_counts()
print(category_counts)

priority_counts = df["priority"].value_counts()
print(priority_counts)

status_counts = df["status"].value_counts()
print(status_counts)

category_percentage=(category_counts/total_tickets)*100
print(category_percentage)

# category distribution chart
plt.figure(figsize=(9,5))
plt.bar(category_counts.index,category_counts.values)
plt.title("Customer Support Tickets by Category")
plt.xlabel("Ticket Category")
plt.ylabel("Number of Tickets")
plt.savefig("screenshots/category_distribution.png")
plt.show()

# priority distribution chart
plt.figure(figsize=(7, 5))
plt.bar(priority_counts.index,priority_counts.values)
plt.title("Customer Support Tickets by Priority")
plt.xlabel("Priority")
plt.ylabel("Number of Tickets")
plt.savefig("screenshots/priority_distribution.png")
plt.show()

# important observation
print("Most common category:",category_counts.idxmax(),"with",category_counts.max(),"tickets")
print("Least common category:",category_counts.idxmin(),"with",category_counts.min(),"tickets")
print("Most common priority:",priority_counts.idxmax(),"with",priority_counts.max(),"tickets")
print("Most common status:",status_counts.idxmax(),"with",status_counts.max(),"tickets")