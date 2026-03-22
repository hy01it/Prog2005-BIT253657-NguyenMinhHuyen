import pandas as pd
import matplotlib.pyplot as plt
cities = pd.read_csv("california_cities.csv")
top10 = cities.sort_values(by="area_total_km2", ascending=False).head(10)
plt.barh(top10["city"], top10["area_total_km2"])
plt.xlabel("Diện tích (km2)")
plt.ylabel("Thành phố")
plt.title("Top 10 thành phố lớn nhất California")
plt.gca().invert_yaxis()  # đảo ngược để lớn nhất ở trên
plt.show()
