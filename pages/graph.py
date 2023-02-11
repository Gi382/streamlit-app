import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("gapminder_with_codes.csv.xls")
st.write("First ten rows of the gapminder dataset")
st.dataframe(data.head(10))

data_x = [x for x in range(100)]
data_y = [x ** 2 for x in data_x]

fig, ax = plt.subplots()
ax.plot(data_x, data_y, label="Squares")
ax.set(xlabel = "x-axis", ylabel = "y-axis", title = "Graph of y = x ** 2")
ax.legend()

st.pyplot(fig)


