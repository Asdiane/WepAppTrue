import streamlit  as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




from checkbox import affiche_data, affiche_missing_values, \
                        affiche_data_types, affiche_stats_describe,\
                        affiche_matrice_corr, affiche_histogramme,affiche_densite,\
                        afficher_scatter_plot



def EDA(data):
        
        
        with st.expander("Choisissez un type et un modèle de transformation dans l’option ci-dessous :"):

            affiche_data(data)

            affiche_missing_values(data)

            affiche_data_types(data)

            affiche_stats_describe(data)
                
            affiche_matrice_corr(data)

            affiche_histogramme(data)

            affiche_densite(data)

            afficher_scatter_plot(data)