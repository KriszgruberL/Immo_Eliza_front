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
    <a href="https://scikit-learn.org/stable/user_guide.html" target="_blank"><img alt="Sklearn" src="https://img.shields.io/badge/sklearn%20-%20sklearn?style=for-the-badge&logo=sklearn&color=blue" style="border-radius:0.5rem"></a>
    <a href="https://pandas.pydata.org/docs/" target="_blank"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-Pandas?style=for-the-badge&logo=pandas&color=61B3DD" style="border-radius:0.5rem"></a>
    <br>
</p>


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



### 👀 Classes Overview

---
`Model and Data

    `Model`: The pre-trained model is stored in model.pkl. The model was trained on a dataset that includes various property features.

    `Data`:
        feature_names.json: Contains the list of features used in the model.
        final_dataset.json: The dataset used for training the model.
        feature_scaler.pkl: Scaler for normalizing features.
        target_scaler.pkl: Scaler for normalizing the target variable.
        zipcode-belgium.json: Contains mapping of zip codes to regions.



## 🎯 Requirements

- `numpy==2.0.1`
- `pandas==2.2.2`
- `pillow==10.4.0`
- `scikit-learn==1.5.1`
- `streamlit==1.37.0`
- `--extra-index-url=https://packagecloud.io/github/git-lfs/pypi/simple`
