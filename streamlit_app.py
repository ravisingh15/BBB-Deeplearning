#importing all the necessary libraries
import selfies as sf
import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer



#Title of the project 
st.title('BBB Prediction')
st.header('NLP based deep-learning model to predict the Blood-Brain-Barrier Permeability of drugs')
#Cc1ccccc1
##Taking input
with st.form(key='input_form'):
	smiles = st.text_input(label='Please enter SMILES')
	submit_button = st.form_submit_button(label='Submit')
	m = Chem.MolFromSmiles(smiles)
	im=Draw.MolToImage(m)
	st.image(im)
	st.write('Generated structure')
selfie=sf.encoder(smiles)
st.write(selfie)	
#with st.container():