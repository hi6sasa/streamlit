import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write sasa!!')

# Example 1

st.write('Hello, <u>***World!***</u> :sunglasses: <span style="color:red">色付け</span>')


st.write('_World!_,:smile:')
smile_face = "\U0001F60A"     
st.write(smile_face)
# Example 2

st.write(1234)

'''
<u>***World!***</u>
- test
- test2
'''

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
print(type(c))
print(df2.head(5))

st.write(c)
