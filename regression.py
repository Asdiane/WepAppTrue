import streamlit as st
import pandas as pd

from function_regression import get_scaler, perform_regression


def regression(data):

    # Vérifier si la colonne 'target' existe dans le DataFrame
    if 'target' in data.columns:
        # Sélectionner les fonctionnalités et la cible
        X = data.drop(columns=['target'], errors='ignore')
        y = data['target']

        # Sélectionner la transformation des données
        scaler_option = st.selectbox("Sélectionnez une transformation des données",
                      ['StandardScaler', 'Normalizer', 'MinMaxScaler', 'Aucun'])

        scaler = get_scaler(scaler_option)

        # Sélectionner le modèle de régression
        regressor_option = st.selectbox("Sélectionnez un modèle de régression",
                                             ['Linear Regression', 'Ridge', 'Lasso', 'Decision Tree',
                                              'Random Forest', 'Gradient Boosting'])

        st.write("## Paramètres sélectionnés")
        st.write(f"Transformation des données : {scaler_option}")
        st.write(f"Modèle de régression : {regressor_option}")

        # Effectuer la régression
        perform_regression(X, y, scaler, regressor_option)
    else:
        st.write("La colonne 'target' n'a pas été trouvée dans le DataFrame.")




if __name__ == '__main__':
    regression()
