<p align="center">
    <br>
    <a href="https://github.com/KriszgruberL" target="_blank"> <img alt="Made with Frogs" src="./assets/made-with-🐸.svg" style="border-radius:0.5rem"></a>
    <br>
    <br><br>
    <a><img src="./assets/logo-modified.png" width="350"  /></a>
    <h2 align="center">Using:
    <br>
    <br>
    <a href="https://www.python.org/downloads/release/python-3120/" target="_blank"><img alt="Python 3.12" src="https://img.shields.io/badge/Python%203.12-python?style=for-the-badge&logo=python&logoColor=F8E71C&labelColor=427EC4&color=2680D1" style="border-radius:0.5rem"></a>
    <a href="https://docs.streamlit.io/" target="_blank"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit%20-%20Streamlit?style=for-the-badge&logo=streamlit&color=%2389CFF0" style="border-radius:0.5rem"></a>
    <a href="https://pandas.pydata.org/docs/" target="_blank"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-Pandas?style=for-the-badge&logo=pandas&color=61B3DD" style="border-radius:0.5rem"></a>
    <br>
</p>

## BeCode red line project - Immo_Eliza 4/4

1. [Scrapping](https://github.com/KriszgruberL/Immo_Eliza)
2. [Data Analysis](https://github.com/KriszgruberL/Immo_Eliza_Data_Analysis)
3. [Preprocessing and Machine Learning](https://github.com/KriszgruberL/Immo_eliza_ML)
4. [API and Deployment](https://github.com/KriszgruberL/Immo_Eliza_front)

## 📚 Overview

This project is a web-based application for predicting house prices based on various features. It uses machine learning models to provide estimates based on user input. The application is built using Python, Streamlit, and other data science libraries.

## 🎙️ Deployed
https://immo--eliza-front-lukiwa.streamlit.app/



## 🚧 Project Structure
```
IMMO_ELIZA_FRONT/
│
├── .streamlit/
│   └── config.toml
│
├── .vscode/
│   └── settings.json
│
├── assets/
│   └── (Images and other assets)
│
├── data/
│   ├── feature_names.json
│   ├── feature_scaler.pkl
│   ├── final_dataset.json
│   ├── model.pkl
│   ├── preprocessed_df.csv
│   ├── preprocessed_df.pkl
│   ├── target_scaler.pkl
│   └── zipcode-belgium.json
│
├── .gitignore
├── .gitattributes
├── README.md
├── app.py
└── requirements.txt

```

## ⚒️ Setup

1. **Clone the repository**:
    ```sh
    https://github.com/KriszgruberL/Immo_Eliza_front.git
    cd Immo_Eliza_front
    ```

2. **Create a virtual environment**:
    ```sh
    python -m env env
    source venv/bin/activate  
    # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## ⚙️ Usage

1. To run the application :
    ```sh
    streamlit run app.py
    ```
2. Fill out the form: Enter the required details like region, province, property type, construction year, etc.

3. Submit the form: Click on the "Predict!" button to get the estimated price.

4. Reset: Click the "Reset" button to clear all the input fields and start over.


## 👀 Model and Data

- **Model:** The pre-trained model is stored in `model.pkl`. The model was trained on a dataset that includes various property features.

- **Data:** 
  - `feature_names.json`: Contains the list of features used in the model.
  - `final_dataset.json`: The dataset used for training the model.
  - `feature_scaler.pkl`: Scaler for normalizing features.
  - `target_scaler.pkl`: Scaler for normalizing the target variable.
  - `zipcode-belgium.json`: Contains mapping of zip codes to regions.

## 😎 Styling

The application has custom CSS styling to enhance the user interface. The primary colors and elements are defined in the `<style>` tag in `app.py`. Additionally, custom color schemes are specified in the Streamlit configuration files (`config.toml` and `config copy.toml`) located in the `.streamlit/` directory. These configurations allow for consistent theming throughout the application.

## 🤖 Functions

#### `handle_submit()`
Callback function that sets the `submitted` state to `True` and calls the `progress_bar` function.

#### `peb_stringify(i: int) -> str`
Converts an index to the corresponding PEB (Energy Performance Certificate) rating.

#### `state_stringify(i: int) -> str`
Converts an index to the corresponding state description of the building. Ensures valid indices and returns a placeholder if invalid.

#### `progress_bar()`
Displays a progress bar indicating that an operation is in progress. It updates the progress bar in increments until complete.

#### `load_model_and_scalers()`
Loads the pre-trained model and scalers from the specified files. Returns the model, feature scaler, and target scaler.

 #### `prepare_data_for_prediction(region: str, province: str, feature_names: list, data: dict) -> dict`
Prepares the data for prediction by initializing features and performing one-hot encoding on the region and province. Returns the updated data dictionary.

#### `import_feature() -> list`
Loads and returns the list of feature names from `feature_names.json`.

## 📚 Libraires 
- [Streamlit](https://docs.streamlit.io/)
- [Pandas](https://pandas.pydata.org/docs/)


## 🎯 Requirements

- `numpy==2.0.1`
- `pandas==2.2.2`
- `pillow==10.4.0`
- `scikit-learn==1.5.1`
- `streamlit==1.37.0`
- `--extra-index-url=https://packagecloud.io/github/git-lfs/pypi/simple`


