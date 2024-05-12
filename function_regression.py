import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler





def get_scaler(scaler_option):
    scalers = {
        'StandardScaler': StandardScaler(),
        'Normalizer': Normalizer(),
        'MinMaxScaler': MinMaxScaler(),
        'Aucun': None
    }
    return scalers.get(scaler_option)


def perform_regression(X, y, scaler, regressor):
    try:
        # Appliquer la transformation si elle est sélectionnée
        if scaler:
            X = scaler.fit_transform(X)

        # Diviser les données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

        # Initialiser le modèle de régression sélectionné
        model = get_regressor(regressor)

        # Entraîner le modèle
        model.fit(X_train, y_train)

        # Faire des prédictions
        predictions = model.predict(X_test)

        # Afficher les métriques d'évaluation
        display_metrics(y_test, predictions)
    except Exception as e:
        st.error(f"Une erreur s'est produite : {str(e)}")

        
def get_regressor(regressor_name):
    regressors = {
        'Linear Regression': LinearRegression(),
        'Ridge': Ridge(),
        'Lasso': Lasso(),
        'Decision Tree': DecisionTreeRegressor(),
        'Random Forest': RandomForestRegressor(),
        'Gradient Boosting': GradientBoostingRegressor()
    }
    return regressors.get(regressor_name)

def display_metrics(y_test, predictions):
    try:
        st.header('Evaluation du modèle de régression')
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        st.write(f"Erreur quadratique moyenne (MSE) : {mse}")
        st.write(f"Coefficient de détermination (R2) : {r2}")
    except Exception as e:
        st.error(f"Une erreur s'est produite lors de l'affichage des métriques : {str(e)}")
