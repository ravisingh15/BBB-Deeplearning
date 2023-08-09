#importing all the necessary libraries
import joblib
import selfies as sf
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import tensorflow as tf
import pandas as pd
#Title of the project 
st.title('BBB Prediction')
st.header('NLP based deep-learning model to predict the Blood-Brain-Barrier Permeability of drugs')
#Cc1ccccc1
##Taking input
with st.form(key='input_form'):
	smiles = st.text_input(label='Please enter CANONICAL SMILES')
	submit_button = st.form_submit_button(label='Submit')
	if not smiles:
		st.stop()
	m = Chem.MolFromSmiles(smiles)
	im=Draw.MolToImage(m)
	st.image(im)
	st.write('Generated structure')

selfie=sf.encoder(smiles)
#st.write(selfie)
#pre-processing the selfies
sel_pre_proc=selfie.replace('][',' ').replace(']','').replace('[','')
a=[sel_pre_proc]
b=tf.convert_to_tensor(a)
#st.write(a)
#sel_list=[sel_pre_proc]
##st.write(sel_list)
#load tensorflow text vectorization model
text_preprocessing=tf.keras.layers.TextVectorization(
    standardize=None,
    split='whitespace',
    ngrams=6,
    output_mode='tf-idf',
    output_sequence_length=None)
#st.write('ye theek hai ')
#vocab = joblib.load('vocab1.sav')  #This is causing error due to pandas uncompatibility
vocab_file=pd.read_csv('vocab.csv')
vocab=vocab_file.Selfies
#st.write('kya ye theek hai')
text_preprocessing.adapt(vocab)
processed_input=text_preprocessing(b)
#st.write(processed_input)
#st.write(predict)
model = tf.keras.models.load_model('my_model') #options=tf.saved_model.LoadOptions(allow_partial_checkpoint=True))
pred=model.predict(processed_input)
if pred[0]<0.5:
    st.markdown(':red[The given molecule is BBB **Impermeable**]')
else: st.write(':blue[The given molecule is BBB **Permeable**]')
