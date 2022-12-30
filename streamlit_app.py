#importing all the necessary libraries
import selfies as sf
import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import tensorflow as tf
#from tensorflow.keras.preprocessing.text import Tokenizer



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
#pre-processing the selfies
sel_pre_proc=selfie.replace('][',' ').replace(']','').replace('[','')
a=tf.convert_to_tensor(sel_pre_proc)
st.write(a)
#sel_list=[sel_pre_proc]
##st.write(sel_list)
#load tensorflow text vectorization model
st.write(tf.__version__)
preprocess = tf.keras.models.load_model('my_model', options=tf.saved_model.LoadOptions(allow_partial_checkpoint=True))
st.write(preprocess)
#text_preprocess= preprocess.predict(sel_list)
#st.write(text_preprocess)

#st.write(sel_list)		
#with st.container():