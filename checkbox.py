import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def affiche_data(data):
    try:
        checkbox_data_values = st.checkbox('Afficher les données chargées')
        if checkbox_data_values:
            st.write('Données du dataset')
            st.write(data)
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage des données : {e}")


def affiche_missing_values(data):
    try:
        checkbox_missing_values = st.checkbox("Afficher Valeurs manquantes")
        if checkbox_missing_values:
            st.write('Valeurs manquantes')
            null_values = data.isnull().sum()
            st.write(null_values)
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage des valeurs manquantes : {e}")


def affiche_data_types(data):
    try:
        checkbox_data_types = st.checkbox("Afficher les types de données")
        if checkbox_data_types:
            st.subheader('Types des données')
            Colonne_and_values_type = data.dtypes
            st.write(Colonne_and_values_type)
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage des types de données : {e}")


def affiche_stats_describe(data):
    try:
        checkbox_stats_describe = st.checkbox("Afficher Statistiques descriptives")
        if checkbox_stats_describe:
            st.subheader("Description statistique")
            stats_desc = data.describe(include='all').round(2)
            st.write(stats_desc)
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage des statistiques descriptives : {e}")


def affiche_matrice_corr(data):
    try:
        checkbox_matrice_corr = st.checkbox("Afficher la corrélation et la matrice de corrélation")
        if checkbox_matrice_corr:
            correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()
            st.write(correlation_matrix)
            sns.set(rc={'figure.figsize': (12, 8)})
            fig, ax = plt.subplots()
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
            plt.title("Matrice de corrélation")
            st.pyplot(fig)
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage de la matrice de corrélation : {e}")


def affiche_histogramme(data):
    try:
        checkbox_histo = st.checkbox("Afficher l'Histogramme")
        if checkbox_histo:
            st.write("Histogrammes")
            for col in data.columns:
                try:
                    if pd.api.types.is_numeric_dtype(data[col]):
                        st.subheader(f"Histogramme de {col}")
                        fig, ax = plt.subplots(figsize=(9, 6))
                        data[col].plot(kind='hist', bins=30, ax=ax)
                        st.pyplot(fig)
                except Exception as e:
                    st.warning(f"Une erreur s'est produite lors de l'affichage de l'histogramme de {col} : {e}")
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage des histogrammes : {e}")

def affiche_densite(data):
    try:
        checkbox_densite = st.checkbox("Afficher la densité")
        if checkbox_densite:
            st.write('Densité')
            for col in data.columns:
                try:
                    if pd.api.types.is_numeric_dtype(data[col]):
                        st.subheader(f"Densité de {col}")
                        fig, ax = plt.subplots(figsize=(9, 6))
                        data[col].plot(kind='density', ax=ax)
                        st.pyplot(fig)
                except Exception as e:
                    st.warning(f"Une erreur s'est produite lors de l'affichage de la densité de {col} : {e}")
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage de la densité : {e}")

def afficher_scatter_plot1(data):
    try:
        """Affiche un scatter plot entre chaque paire de variables numériques"""
        st.write("Scatter plots")
        cols = list(data.select_dtypes(['float64','int64']).columns)
        selectionnees = st.multiselect("Choisissez les colonnes à afficher sur le Scatter Plot : ",cols)
        if len(selectionnees) > 1:
            with st.expander("Voir plus"):
                fig, axes = plt.subplots(len(selectionnees), len(selectionnees), figsize=(15, 15))
                for i in range(len(selectionnees)):
                    for j in range(i + 1, len(selectionnees)):
                        try:
                            axes[i, j].scatter(data[selectionnees[i]],
                                              data[selectionnees[j]])
                            axes[i, j].set_xlabel(selectionnees[i])
                            axes[i, j].set_ylabel(selectionnees[j])
                            axes[i, j].set_title(f"{selectionnees[i]} vs {selectionnees[j]}")
                        except Exception as e:
                            st.warning(f"Une erreur s'est produite lors de l'affichage du scatter plot entre {selectionnees[i]} et {selectionnees[j]} : {e}")
                st.pyplot(plt.gcf())
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage des scatter plots : {e}")



def afficher_scatter_plot(data):
    try:
        checkbox_scatter_plot = st.checkbox("Nuages de points")
        if checkbox_scatter_plot:
            st.write("Scatter Plot")
            x_axis = st.selectbox("Choisir la variable pour l'axe X", data.columns)
            y_axis = st.selectbox("Choisir la variable pour l'axe Y", data.columns)

            fig, ax = plt.subplots(figsize=(10, 6))
            try:
                ax.scatter(data[x_axis], data[y_axis])
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)
                ax.set_title(f"Scatter Plot entre {x_axis} et {y_axis}")
            except Exception as e:
                st.warning(f"Une erreur s'est produite lors de la création du scatter plot : {e}")

            st.pyplot(fig)
    except Exception as e:
        st.warning(f"Une erreur s'est produite lors de l'affichage du scatter plot : {e}")






