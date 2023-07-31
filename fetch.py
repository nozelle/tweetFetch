import streamlit as st

def main():
    st.title("Malama Carbon Footprint Calculator")

    # Initialize variables to store user inputs
    energy_consumption = 0
    transportation_emissions = 0
    diet_emissions = 0
    waste_production = 0
    shopping_habits = 0

    st.write("Please answer the following questions to calculate your carbon footprint:")

    # Question 1: Energy consumption
    energy_consumption = st.slider("1. Energy Consumption (kWh per month)", min_value=0, max_value=1000, step=10)

    # Question 2: Transportation
    transportation_emissions = st.slider("2. Transportation Emissions (kg CO2 per year)", min_value=0, max_value=10000, step=100)

    # Question 3: Diet
    diet_options = ["Plant-based", "Mixed (Some meat and dairy)", "High meat and dairy"]
    diet_emissions = st.selectbox("3. Diet", diet_options)

    # Question 4: Waste production
    waste_production = st.slider("4. Waste Production (kg per week)", min_value=0, max_value=100, step=1)

    # Question 5: Shopping habits
    shopping_options = ["Minimal waste (buying local, reducing packaging, etc.)", "Regular shopping habits"]
    shopping_habits = st.selectbox("5. Shopping Habits", shopping_options)

    # Calculate total carbon footprint based on the user's inputs
    total_carbon_footprint = energy_consumption * 0.35 + transportation_emissions * 0.15

    if diet_emissions == "Plant-based":
        total_carbon_footprint += 150
    elif diet_emissions == "Mixed (Some meat and dairy)":
        total_carbon_footprint += 400
    elif diet_emissions == "High meat and dairy":
        total_carbon_footprint += 800

    total_carbon_footprint += waste_production * 0.1

    st.markdown("<h2>Your estimated carbon footprint is:</h2>", unsafe_allow_html=True)

    # Display the total_carbon_footprint value in a card format
    total_carbon_footprint = int(total_carbon_footprint)
    st.info(f"{total_carbon_footprint} kg CO2 per year")
    
if __name__ == "__main__":
    main()
