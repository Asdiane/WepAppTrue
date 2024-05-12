import streamlit as st


from function_classification import get_scaler,perform_classification



def classification(data):
    st.write("# Classification de Dataset")
   
    # Vérifier si la colonne 'target' existe dans le DataFrame
    if 'target' in data.columns:
        # Sélectionner les fonctionnalités et la cible
        X = data.drop(columns=['target'], errors='ignore')
        Y = data['target']

        # Sélectionner la transformation des données
        scaler_option = st.selectbox("Sélectionnez une transformation des données",
                                         ['StandardScaler', 'Normalizer', 'MinMaxScaler', 'Aucun'])
        scaler = get_scaler(scaler_option)

        # Sélectionner le modèle de classification
        classifier_option = st.selectbox("Sélectionnez un modèle de classification",
                                             ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM',
                                              'K Neighbors', 'MLP', 'Naive Bayes'])

        st.write("## Paramètres sélectionnés")
        st.write(f"Transformation des données : {scaler_option}")
        st.write(f"Modèle de classification : {classifier_option}")

        # Effectuer la classification
        perform_classification(X, Y, scaler, classifier_option)
    else:
        st.write("La colonne 'target' n'a pas été trouvée dans le DataFrame.")



if __name__ == '__main__':
    classification()
