# Imports first:
from pathlib import Path
import streamlit as st
import sys
import os

# Grab the filepath again, just like our image_return.py file:
filepath = os.path.join(Path(__file__).parents[1])

# Insert filepath into system:
sys.path.insert(0, filepath)

# Import the ToMongo class:
from to_mongo import ToMongo

# Instantiate the class:
c = ToMongo()

# Now we query the database

"""
Query the student performance database
"""

answer = st.text_input('GP - Gabriel Pereira or MS - Mousinho da Silveira', value = 'GP')
st.write(list(c.performance.find({'school':answer})))