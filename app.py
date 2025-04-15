import pandas as pd, streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from nbconvert import HTMLExporter


# Use README.md to generate the content
with open('README.md', encoding='utf-8') as f:
	md = f.read()
with open('Blinkit Sales Analysis.ipynb', encoding='utf-8') as f:
	nb_html, _ = HTMLExporter().from_file(f)
	nb = f.read()

st.set_page_config(page_title='Blinkit Sales Analysis', page_icon='📊', layout='wide')
st.title('Blinkit Sales Analysis')

# Show user selected table
@st.fragment
def show_dataset():
	table = st.segmented_control(
		'Table:', ['Customers', 'Orders', 'OrderDetails'],
		default='Customers', label_visibility='collapsed')
	if table: st.dataframe(pd.read_csv(f'Dataset/{table}.csv'), hide_index=True)
	
# Button to download the notebook
@st.fragment
def download_notebook():
	st.download_button(
		'Download notebook', nb, file_name='Blinkit Sales Analysis.ipynb',
		icon=':material/download:')


# Add 2 tabs: Overview, Notebook
overview, notebook = st.tabs([':material/description: Overview', ':material/code: Notebook'])
with notebook:
	components.html(nb_html, height=12_470, scrolling=True)

with overview:
	col1, col2 = st.columns((.7, .3))
	with col2:  # Add a lottie animation
		st_lottie('https://lottie.host/918af46f-def8-4671-b923-6fcf2cbf4ec4/ymGhlawoWY.json')
	# Project overview, Objective
	col1.markdown(md[md.find('## Project') : md.find('## Methodology')])
	
	# Expander to show the dataset
	with st.expander('See the dataset', icon=':material/table:'):
		st.caption('''
		The dataset simulates Blinkit's sales operations and consists of three tables capturing
		customer demographics, order transactions with timestamps and statuses, purchase details.
		''')
		show_dataset()
	
	# Methodology, Key Takeaways, Conclusion
	st.markdown(md[md.find('## Methodology'):])
	st.divider()
	download_notebook()