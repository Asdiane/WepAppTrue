import streamlit  as st


# from verifydata import has_headers, add_headers, upload_dataset

# Import the functions
from EDA import EDA

from classication import classification

from function_classification import load_data

from regression  import regression


def main():
    
    st.write(
        """
            # Exploratory Data Analysis & Predictive Modelling
            
        """

    )
    data = None

    import_fichier = st.file_uploader("Telecharger le fichier CSV", type=[".csv"])


    # Delimiter Selection
    delimiter_options = [',', ';', '\t']  # You can add more delimiters as needed
    delimiter = st.selectbox("Sélectionnez le délimiteur", delimiter_options)

    une_entete = st.checkbox("Le fichier a-t-il un en-tête ?")

    if import_fichier is not None:
        data = load_data(import_fichier, delimiter, une_entete)

  
    option = st.sidebar.selectbox(
    'Select option',
    ('EDA', 'Classification', 'Regression'))
    
    st.write('You selected:', option)
    if option == "EDA":
        if data is not None:
            EDA(data)
        else:
            st.warning("Veuillez télécharger un fichier CSV pour effectuer l'EDA.")

    elif option == "Classification":
        if data is not None:
            classification(data)
        else:
            st.warning("Veuillez télécharger un fichier CSV pour effectuer la classification")

    elif option == "Regression":
        if data is not None:
            regression(data)
        else:
            st.warning("Veuillez télécharger un fichier CSV pour effectuer la regression")


if __name__ == '__main__':
    main()

