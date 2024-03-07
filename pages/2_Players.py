"""
Page on streamlit which focuses on team performance, rosters, etc.
"""
import numpy as np
import pandas as pd
import streamlit as st
import statsapi
import functions

st.set_page_config(
    page_title = "MLB Players"
)

st.title('MLB Players')
