#importing all the necessary libraries
import selfies as sf
import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

#Title of the project 
st.title('BBB Prediction')
st.header('NLP based deep-learning model to predict the Blood-Brain-Barrier Permeability of drugs')
#Cc1ccccc1
##Taking input 
smiles=st.text_input('Please ender smiles of compounds')
m = Chem.MolFromSmiles(smiles)
st.write("Checking the structure")
st.write(Draw.MolToImage(m))
