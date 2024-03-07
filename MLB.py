"""
Main landing page for streamlit for streamlit app that visualises MLB data as extracted via the api using 
"""

import numpy as np
import pandas as pd
import streamlit as st
import statsapi
import functions

st.set_page_config(
    page_title = "Major League Baseball (MLB)"
)

st.title('Major League Baseball (MLB)')
