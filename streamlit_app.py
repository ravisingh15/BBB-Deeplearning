import selfies as sf
import streamlit as st
import pandas as pd

st.title('BBB Prediction')
st.header('NLP based deep-learning model to predict the Blood-Brain-Barrier Permeability of drugs')

##Taking input 
smiles=st.text_input('Please ender smiles of compounds')
st.write(smiles)