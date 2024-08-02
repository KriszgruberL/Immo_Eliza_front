import json
import time
import pickle
import streamlit as st
import pandas as pd
import time


### CSS Styling
st.markdown(
    """
    <style>
    :root {
        --accent-color: #ea638c;
        --text_color: #ffd9da;
        --success_color : #2CA677;
        --error_color : #FFC107;
        --bg-color : #1B2021;
    }

    div.stButton {text-align:center;}

    /* Specific styling for buttons */
    .stButton button {
        border: 2px solid var(--accent-color);
        color: var(--accent-color);
        padding: 0.75rem 1rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 2rem !important;
        margin: 4px 2px;
        border-radius: 1rem 1rem 0rem 1rem;
        cursor: pointer;
    }
    
    /* Optional: Hover effect for buttons */
    .stButton button:hover {
        background-color: var(--accent-color);
        color: var(--text_color);
    }
    
    .stButton button:active {
        box-shadow: inset -5px -5px 10px 0px rgba(28,28,28,0.5);
    }
    
    .custom-container {
        border: 1px solid var(--accent-color);
        border-radius: 1rem;
        padding: 1rem;
    }
    
    .title {
        text-align:center; 
        border: 2px solid var(--accent-color);
        border-radius : 1rem 1rem 0rem 1rem
    }
    
    .small {
        color:var(--error_color); 
        font-size:small
    }
    
    # .success-msg {
    #     text-align: center; 
    #     background: var(--success-color); 
    #     border-radius: 1rem 1rem 0rem 1rem;
    #     color: white;
    #     padding: 1rem;
    # }
    </style>
    """,
    unsafe_allow_html=True,
)

# ********************************************************************************
# ********************************************************************************
# ********************************Functions***************************************
# ********************************************************************************
# ********************************************************************************

# # Callback function to handle submission
def handle_submit():
    st.session_state.submitted = True
    progress_bar()


peb_string = ["A++", "A+", "A", "B", "C", "D", "E", "F", "G"]
state_string = ["Select a state of building*","As new","Just renovated","Good","To restore","To renovate","To be done up"]

def peb_stringify(i: int = 0) -> str:
    return peb_string[i - 1]

def state_stringify(i: int = 0) -> str:
    # Ensure the index is valid; if not, return the first placeholder entry
    if i <= 0 or i >= len(state_string):
        return state_string[0]
    return state_string[i]

def progress_bar():
    """
    Displays a progress bar with a text indicating the operation in progress.
    """
    # Progress bar
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()

 
def load_model_and_scalers():
    """
    Load the pre-trained model, scalers, and feature names from the specified files.

    Returns:
        model (object): The pre-trained model.
        feature_scaler (object): The scaler used for feature normalization.
        target_scaler (object): The scaler used for target normalization.
        feature_names (list): The names of the features used by the model.
    """
    # Load the pre-trained model and scalers
    with open("data/model.pkl", "rb") as file:
        model = pickle.load(file)
    with open("data/feature_scaler.pkl", "rb") as scaler_file:
        feature_scaler = pickle.load(scaler_file)
    with open("data/target_scaler.pkl", "rb") as target_scaler_file:
        target_scaler = pickle.load(target_scaler_file)  
    
    return model, feature_scaler, target_scaler

def prepare_data_for_prediction(region, province, feature_names, data):
    """
    Prepare the data for prediction by performing one-hot encoding on the given features.

    Args:
        region (str): The region value.
        province (str): The province value.
        feature_names (list): A list of feature names.
        data (dict): The data dictionary containing the feature values.

    Returns:
        dict: The updated data dictionary with one-hot encoded features or None for placeholders.

    """
    # Initialize all features to zero or None
    prepared_data = {feature: 0 for feature in feature_names}

    # Update with provided data values
    for key, value in data.items():
        if key in prepared_data:
            prepared_data[key] = value

    # Set None for placeholders and perform one-hot encoding for valid values
    if province == "Select the province*":
        # Handle the case where province is still the placeholder
        prepared_data["province"] = None
    else:
        province_column = f"Province_{province}"
        if province_column in prepared_data:
            prepared_data[province_column] = 1

    if region == "Select the region*":
        # Handle the case where region is still the placeholder
        prepared_data["region"] = None
    else:
        region_column = f"Region_{region}"
        if region_column in prepared_data:
            prepared_data[region_column] = 1

    return prepared_data


def import_feature() -> list: 
    with open("data/feature_names.json", "r") as f:
        feature_names = json.load(f) 
    return feature_names

# ********************************************************************************
# ********************************************************************************
# ******************************Init**********************************************
# ********************************************************************************
# ********************************************************************************

default_values = {
    "bed": 0,
    "shower": 0,
    "toilet": 0,
    "bath": 0,
    "garden_area": 0,
    "year": 2000,
    "nb_facade": 1,
    "zip_code": 1000,
    "kitchen": "No",
    "state_building": 0,
    "living_area": 0,
    "plot_area": 0,
    "flood": "No",
    "province": "Select the province*",
    "region" : "Select the region*",
    "property_type":0,
    "sale_type": 0,
    "garden": "No",
    "pool": "No",
    "terrace": "No",
    "peb": 5  # Default PEB value
}

# Initialize session state variables
if "submitted" not in st.session_state:
    st.session_state.submitted = False


st.session_state.feature_names = import_feature()

# ********************************************************************************
# ********************************************************************************
# ***********************************Form*****************************************
# ********************************************************************************
# ********************************************************************************

# Title of the app
st.markdown("""<br><h1 class="title" >House Price Prediction</h1>""", unsafe_allow_html=True)

# Form container

feature_names = st.session_state.feature_names
if not st.session_state.submitted:
    with st.container(border = True):
        st.write("Property Details")
        col1, col2 = st.columns(2)
        with col1:
            region = st.selectbox(
                "Select the region*",
                options=["Select the region*","Brussels", "Flanders", "Wallonia"],
                index =0,
                key="region",
                label_visibility="hidden",
            )
            st.markdown("""<p class="small">*Required field</p>""", unsafe_allow_html=True)
            if st.session_state.region == "Select the region*":
                st.error("Please select a valid region.")
        with col2:
            if st.session_state.region == "Brussels":
                province_options = ["Brussels"]
            elif st.session_state.region == "Flanders":
                province_options = [
                    "Select the province*",
                    "Antwerp",
                    "Flemish Brabant",
                    "Limburg",
                    "East Flanders",
                    "West Flanders",
                ]
            elif st.session_state.region == "Wallonia":
                province_options = [
                    "Select the province*",
                    "Walloon Brabant",
                    "Hainaut",
                    "Liege",
                    "Luxembourg",
                    "Namur",
                ]
            else:
                province_options = ["Select the province*"]
                    # Selectbox for province
            province = st.selectbox(
                "Select the province*",
                options=province_options,
                index=0 if "Select the province*" in province_options else None,
                key="province",
                label_visibility="hidden",
            )
            if region: 
                st.markdown("""<p class="small">*Required field</p>""", unsafe_allow_html=True)
                
            # Check for valid selections
            if st.session_state.province == "Select the province*":
                st.error("Please select a valid province.")

        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.session_state.property_type = st.radio(
                "Select the type of property*",
                ["House", "Apartment"],
                index=0,
                key="type_property",
                horizontal=True,
            )
            st.markdown("""<p class="small">*Required field</p>""", unsafe_allow_html=True)
            
            st.session_state.year = st.number_input(
                "Enter the construction year (1600 - 2040)",
                min_value=1600,
                max_value=2040,
                value=2000,
                format="%d",
                help="Enter a value between 1600 - 2040",
            )

            st.session_state.nb_facade = st.number_input(
                "Enter the number of facades (0 - 4)",
                min_value=0,
                max_value=4,
                value=1,
                format="%d",
                help="Enter a value between 0 and 4",
            )

        with col2:
            st.session_state.sale_type = st.radio(
                "Select the type of sale*",
                ["For Sale", "For Rent"],
                index=0,
                key="type_sale",
                horizontal=True,
            )
            st.markdown("""<p class="small">*Required field</p>""", unsafe_allow_html=True)
            st.session_state.zip_code = st.number_input(
                "Enter the postal code",
                min_value=1000,
                max_value=9992,
                value=5000,
                format="%d",
                help="Enter a value between 1000 and 9992 (Belgium zip codes)",
            )
            state_building = st.selectbox(
                "Select the state of the building*",
                options=range(len(state_string)),
                index=0,
                key="state_building",
                format_func=state_stringify,
                help="Select the state of the building - Required field",
            )
            st.markdown("""<p class="small">*Required field</p>""", unsafe_allow_html=True)
             
        st.divider()
        
        st.session_state.living_area = st.number_input(
            "Enter the living area (in m²)*",
            min_value=1,
            value=1,
            format="%d",
            help="Enter a value greater than 0 - Required field",
        )
        
        st.session_state.plot_area = st.number_input(
            "Enter the plot area (in m²)",
            min_value=0,
            value=1,
            format="%d",
            help="Enter a numerical value",
        )
        peb = st.select_slider(
            "Select the PEB value",
            options=range(1, len(peb_string) + 1),
            key="peb",
            value=5,
            format_func=peb_stringify,
        )
        
        flood = st.radio(
            "Is it in a flooding zone?",
            options=["Yes", "No"],
            key="flood",
            horizontal=True,
        )

    #Inside
    with st.container(border = True):
        st.write("Inside Details")
        col1, col2 = st.columns(2)
        with col1:

            st.session_state.bed = st.number_input(
                "Enter the number of bedrooms (0 - 200)",
                min_value=0,
                max_value=200,
                step=1,
                help="Enter a numerical value between 0 and 200",
            )
            kitchen = st.radio(
                "Is the kitchen installed?",
                ["Yes", "No"],
                index = 1,
                key="kitchen",
                horizontal=True,
            )
        with col2:
            st.session_state.bath = st.number_input(
                "Enter the number of bathrooms",
                min_value=0,
                format="%d",
                help="Enter a numerical value",
            )
            st.session_state.shower = st.number_input(
                "Enter the number of showers",
                min_value=0,
                value=0,
                format="%d",
                help="Enter a numerical value",
            )
            st.session_state.toilet = st.number_input(
                "Enter the number of toilets ",
                min_value=0,
                value=0,
                format="%d",
                help="Enter a numerical value",
            )
            

    with st.container(border = True):
        st.write("Outside Details")
        garden = st.radio(
            "Does the house have a garden?",
            ["Yes", "No"],
            key="garden",
            horizontal=True,
        )
        # Dynamic garden area input
        if st.session_state.garden == "Yes":
            st.session_state.garden_area = st.number_input(
                "Garden Area (in m²)", min_value=1, format="%d", value=None
            )
        else:
            garden_area = 0

        pool = st.radio(
            "Does the house have a swimming pool?",
            ["Yes", "No"],
            key="pool",
            horizontal=True,
        )
        terrace = st.radio(
            "Does the house have a terrace?",
            ["Yes", "No"],

            key="terrace",
            horizontal=True,
        )


    st.session_state.data = {
        "TypeOfProperty": 0 if st.session_state.property_type == "House" else 1,
        "ConstructionYear": st.session_state.year,
        "NumberOfFacades": st.session_state.nb_facade,
        "TypeOfSale": 0 if st.session_state.sale_type == "For Sale" else 1,
        "PostalCode": st.session_state.zip_code,
        "StateOfBuilding": st.session_state.state_building - 1,
        "LivingArea": st.session_state.living_area,
        "SurfaceOfPlot": st.session_state.plot_area,
        "PEB": st.session_state.peb,
        "FloodingZone": 1 if st.session_state.flood == "Yes" else 0,
        "Kitchen": 1 if st.session_state.kitchen == "Yes" else 0,
        "BathroomCount": st.session_state.bath,
        "BedroomCount": st.session_state.bed,
        "ShowerCount": st.session_state.shower,
        "ToiletCount": st.session_state.toilet,
        "Garden": 1 if st.session_state.garden == "Yes" else 0,
        "GardenArea": st.session_state.garden_area,
        "SwimmingPool": 1 if st.session_state.pool == "Yes" else 0,
        "Terrace": 1 if st.session_state.terrace == "Yes" else 0,
    }
    
    st.session_state.data = prepare_data_for_prediction(st.session_state.region, st.session_state.province, feature_names, st.session_state.data)
    
    # Ensure all values are not None and of correct type
    st.session_state.data = {k: (0 if v is None else v) for k, v in st.session_state.data.items()}
    if st.button("Predict !", on_click=handle_submit) : 
            st.session_state.submitted = True
            
            
# ********************************************************************************
# ********************************************************************************
# ***********************************Prediction***********************************
# ********************************************************************************
# ********************************************************************************
        

if st.session_state.submitted:

    # Load the pre-trained model and scalers
    model, feature_scaler, target_scaler = load_model_and_scalers()

    # Create a DataFrame for the input data
    df = pd.DataFrame([st.session_state.data], columns=feature_names)

    # Ensure all columns are of the correct type
    df = df.astype(
        {
            "TypeOfProperty": "int",
            "ConstructionYear": "float",
            "NumberOfFacades": "float",
            "TypeOfSale": "float",
            "PostalCode": "int",
            "StateOfBuilding": "float",
            "LivingArea": "float",
            "SurfaceOfPlot": "float",
            "PEB": "float",
            "FloodingZone": "float",
            "Kitchen": "float",
            "BathroomCount": "float",
            "BedroomCount": "int",
            "ShowerCount": "float",
            "ToiletCount": "float",
            "Garden": "float",
            "GardenArea": "float",
            "SwimmingPool": "float",
            "Terrace": "float",
            "Region_Brussels": "int",
            "Region_Flanders": "int",
            "Region_Wallonie": "int",
            "Province_Antwerp": "int",
            "Province_Brussels": "int",
            "Province_East Flanders": "int",
            "Province_Flemish Brabant": "int",
            "Province_Hainaut": "int",
            "Province_Limburg": "int",
            "Province_Liège": "int",
            "Province_Luxembourg": "int",
            "Province_Namur": "int",
            "Province_Walloon Brabant": "int",
            "Province_West Flanders": "int",
        }
    )

    # Scale the features
    X = feature_scaler.transform(df)

    # Predict using the model
    predictions_scaled = model.predict(X)
    predictions_original = target_scaler.inverse_transform(
        predictions_scaled.reshape(-1, 1)
    )

    
    
# ********************************************************************************
# ********************************************************************************
# ***********************************Results**************************************
# ********************************************************************************
# ********************************************************************************

    # Display the predicted price
    st.markdown("<h2 style='text-align:center'>Predicted Price</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h5>With the following data : </h5>", unsafe_allow_html=True)
        st.markdown(f"""
        <style>
        .small-text {{
            line-height: 1.2;
            margin: 0;
        }}
        </style>
        <div class="small-text">
            - Type of property: {st.session_state.property_type}<br>
            - Construction year: {st.session_state.year}<br>
            - Number of facades: {st.session_state.nb_facade}<br>
            - Type of sale: {st.session_state.sale_type}<br>
            - Postal code: {st.session_state.zip_code}<br>
            - State of building: {state_string[st.session_state.state_building]}<br>
            - Living area: {st.session_state.living_area}<br>
            - Plot area: {st.session_state.plot_area}<br>
            - PEB value: {st.session_state.peb}<br>
            - Flooding zone: {st.session_state.flood}<br>
            - Kitchen installed: {st.session_state.kitchen}<br>
            - Number of bathrooms: {st.session_state.bath}<br>
            - Number of bedrooms: {st.session_state.bed}<br>
            - Number of showers: {st.session_state.shower}<br>
            - Number of toilets: {st.session_state.toilet}<br>
            - Garden: {st.session_state.garden}<br>
            - Garden area: {st.session_state.garden_area}<br>
            - Swimming pool: {st.session_state.pool}<br>
            - Terrace: {st.session_state.terrace}<br>
            - Region: {st.session_state.region}<br>
            - Province: {st.session_state.province}
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("assets/1_lTWsQr8phKRUVGMjL7SqGg.webp", use_column_width=True)
        
    st.markdown(f"<br><h4 style='text-align:center; background : var(--success_color); border-radius : 1rem 1rem 0rem 1rem; '>Predicted price: {predictions_original.flatten()[0]:.2f} €</h4>", unsafe_allow_html=True)
    st.button("Reset", on_click=st.session_state.clear)