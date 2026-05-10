import streamlit as st
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- HEADER SECTION ---
# Displaying Name and Roll Number as requested
st.title("Mechanical Unit Converter & Material Density Checker")
st.subheader("Student Identification")
st.info(f"**Name:** Hamza Bin Shakeel  \n**Roll Number:** 25 ME 144")

st.divider()

# --- SECTION 1: UNIT CONVERTER ---
st.header("1. Mechanical Unit Converter")

conversion_type = st.selectbox("Select Conversion Category", ["Length", "Pressure", "Force"])

if conversion_type == "Length":
    val = st.number_input("Enter Value", value=1.0)
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Inches", "Feet", "Millimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Inches", "Feet", "Millimeters"])
    
    # Length Logic (Base unit: Meters)
    length_dict = {"Meters": 1.0, "Inches": 0.0254, "Feet": 0.3048, "Millimeters": 0.001}
    result = val * (length_dict[from_unit] / length_dict[to_unit])
    st.success(f"**Result:** {result:.4f} {to_unit}")

elif conversion_type == "Pressure":
    val = st.number_input("Enter Value", value=1.0)
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Pascal", "Bar", "PSI", "Atmosphere"])
    with col2:
        to_unit = st.selectbox("To", ["Pascal", "Bar", "PSI", "Atmosphere"])
    
    # Pressure Logic (Base unit: Pascal)
    press_dict = {"Pascal": 1.0, "Bar": 100000.0, "PSI": 6894.76, "Atmosphere": 101325.0}
    result = val * (press_dict[from_unit] / press_dict[to_unit])
    st.success(f"**Result:** {result:.4f} {to_unit}")

elif conversion_type == "Force":
    val = st.number_input("Enter Value", value=1.0)
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Newton", "KiloNewton", "Pound-force"])
    with col2:
        to_unit = st.selectbox("To", ["Newton", "KiloNewton", "Pound-force"])
    
    # Force Logic (Base unit: Newton)
    force_dict = {"Newton": 1.0, "KiloNewton": 1000.0, "Pound-force": 4.44822}
    result = val * (force_dict[from_unit] / force_dict[to_unit])
    st.success(f"**Result:** {result:.4f} {to_unit}")

st.divider()

# --- SECTION 2: DENSITY CHECKER ---
st.header("2. Material Density Checker")

# Data Dictionary
density_data = {
    "Material": ["Steel", "Aluminum", "Copper", "Titanium", "Cast Iron", "Concrete", "Water"],
    "Density (kg/m³)": [7850, 2700, 8960, 4507, 7200, 2400, 1000],
    "Density (lb/ft³)": [490, 168.5, 559, 281, 450, 150, 62.4]
}
df = pd.DataFrame(density_data)

selected_material = st.selectbox("Select a Material to check its density:", df["Material"])

# Display result for the selected material
material_info = df[df["Material"] == selected_material]
st.table(material_info)

# Optional: Density Search
with st.expander("View Full Density Table"):
    st.dataframe(df, use_container_width=True)

st.divider()
st.caption("Developed for Mechanical Engineering Calculations")
