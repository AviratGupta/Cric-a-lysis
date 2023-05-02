import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data.index import female_cricket , female_matches , female_top_countries
from Components.General_Analysis.Statistics import Statistics
from Helper import Detailed_Analysis


def female():
    Detailed_Analysis(t20=female_cricket  , match=female_matches , top_countries=female_top_countries , gender_name='FeMale')
    # f = Statistics( female_cricket ,'Female')
    # f.stats()