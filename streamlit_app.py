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
with st.form(key='input_form'):
	smiles = st.text_input(label='Please ender smiles of compounds')
	submit_button = st.form_submit_button(label='Submit')

m = Chem.MolFromSmiles(smiles)
#st.write(m)
#st.write("Checking the structure")
#st.write(Draw.MolToImage(m))
im=Draw.MolToImage(m)
st.image(im)