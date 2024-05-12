import streamlit as st
import pandas as pd
import io
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler



def perform_classification(X, Y, scaler, classifier):
    try:
            # Appliquer la transformation si elle est sélectionnée
            if scaler:
                X = scaler.fit_transform(X)
            # Diviser les données en ensembles d'entraînement et de test
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=7)
            # Initialiser le modèle de classification sélectionné
            model = get_classifier(classifier)
            # Entraîner le modèle
            model.fit(X_train, Y_train)
            # Faire des prédictions
            predictions = model.predict(X_test)
            # Afficher les métriques d'évaluation
            display_metrics(Y_test, predictions)
    except Exception as e:
            st.error(f"Une erreur s'est produite lors de la classification : {e}")


def load_data(file, delimiter, une_entete):
        if une_entete:
            # Si le fichier a un en-tête, utilisez simplement le délimiteur spécifié
            data = pd.read_csv(io.StringIO(file.read().decode('utf-8')), delimiter=delimiter)
        else:
            # Si le fichier n'a pas d'en-tête, lisez-le d'abord sans en-tête
            data = pd.read_csv(io.StringIO(file.read().decode('utf-8')), delimiter=delimiter, header=None)
            # Générez des noms de colonnes par défaut (Colonne0, Colonne1, ...)
            data.columns = [f"Colonne{i}" for i in range(data.shape[1])]
        return data

def get_classifier(classifier_name):
    classifiers = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC(),
        'K Neighbors': KNeighborsClassifier(),
        'MLP': MLPClassifier(),
        'Naive Bayes': GaussianNB(),
    }
    return classifiers.get(classifier_name)

def display_metrics(Y_test, predictions):
    st.header('Evaluation du modèle')
    accuracy = accuracy_score(Y_test, predictions)
    precision = precision_score(Y_test, predictions)
    recall = recall_score(Y_test, predictions)
    f1 = f1_score(Y_test, predictions)

    TN, FP, FN, TP = confusion_matrix(Y_test, predictions).ravel()
    specificity = (TN) / (TN + FP)    
    accuracy = (TN + TP)/ (TP + TN + FP + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    
    st.write(f"Accuracy : {accuracy}")
    st.write(f"Précision : {precision}")
    st.write(f"Recall : {recall}")
    st.write(f"Spécificité : {specificity}")
    st.write(f"F1-Score : {f1}")
    st.subheader('Matrice de Confusion')
    confusion = confusion_matrix(Y_test, predictions)
    st.write(confusion)


def get_scaler(scaler_option):
    scalers = {
        'StandardScaler': StandardScaler(),
        'Normalizer': Normalizer(),
        'MinMaxScaler': MinMaxScaler(),
        'Aucun': None
    }
    return scalers.get(scaler_option)