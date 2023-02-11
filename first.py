import streamlit as st
import numpy as np
import pandas as pd
import time


left_column, right_column = st.columns(2)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f"col {i}" for i in range(20)]
)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
with left_column:
    st.dataframe(dataframe.style.highlight_max(axis=1))
    st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

with right_column:
    st.map(map_data)
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.text_input("Your name", key="name")


# You can access the value at any point with:
# st.session_state.name

st.write(st.session_state.name)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 4),
       columns=['a', 'b', 'c', 'd'])

    st.line_chart(chart_data)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['second column'])

fav_decimal = st.sidebar.slider("Choose yor favorite decimal.", 0.0, 100.0, (25.0, 75.0), 0.5)

st.write(f'You selected: {option}')
st.write(f"Favourite decimal: {fav_decimal}")


st.write('Starting a long computation...')

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.write('...and now we\'re done!')


with st.spinner("Wait for it"):
    time.sleep(5)

st.write("Done")
