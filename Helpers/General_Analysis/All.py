import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data.index import t20
from data.index import t20 , matches , top_countries

from Components.General_Analysis.Statistics import Statistics
from Helper import Detailed_Analysis


def all():
    Detailed_Analysis(t20=t20  , match=matches , top_countries=top_countries , gender_name='"Overall Statistics"')