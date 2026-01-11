import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and assets
model = joblib.load("emissions_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")
data = pd.read_csv("greenhouse_gas_inventory_data_data.csv")

# Sidebar UI
st.title("🌍 Greenhouse Gas Emissions Predictor")
st.markdown("Predict future greenhouse gas emissions by selecting a country, category, and year.")

st.sidebar.header("🛠️ Input Features")
countries = data['country_or_area'].unique()
min_year = int(data['year'].min())
max_year = 2100

country = st.sidebar.selectbox("🌐 Country", sorted(countries))
filtered_categories = data[data['country_or_area'] == country]['category'].unique()
category = st.sidebar.selectbox("🧪 Emission Category", sorted(filtered_categories))
year = st.sidebar.number_input("📅 Year", min_value=min_year, max_value=max_year, value=2032)

# Prediction
if st.sidebar.button("🔮 Predict"):
    if country and category:
        # Encode and scale input
        country_encoded = label_encoders['country_or_area'].transform([country])[0]
        category_encoded = label_encoders['category'].transform([category])[0]
        input_df = pd.DataFrame([[country_encoded, year, category_encoded]],
                                columns=['country_or_area', 'year', 'category'])
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]

        # Filter historical data
        recent_years = data[
            (data['country_or_area'] == country) &
            (data['category'] == category)
        ].sort_values(by='year', ascending=False).head(5)

        if not recent_years.empty:
            avg_emissions = recent_years['value'].mean()
            total_emissions = recent_years['value'].sum()
            percent_change = ((prediction - avg_emissions) / avg_emissions) * 100

            # Graph
            st.subheader(f"📊 Emissions Trend for {country} ({category})")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(recent_years['year'], recent_years['value'], color='blue', marker='o', label='Historical Emissions')
            ax.scatter(year, prediction, color='red', label=f'Prediction ({year})', zorder=5)

            y_offset = max(avg_emissions * 0.05, 500)
            ax.annotate(f"Prediction: {prediction:.2f}",
                        xy=(year, prediction),
                        xytext=(year, prediction + y_offset),
                        arrowprops=dict(facecolor='red', shrink=0.05),
                        fontsize=10, color='red', weight='bold')

            ax.set_xlabel("Year")
            ax.set_ylabel("Emissions (Kilotonnes CO₂-eq)")
            ax.set_title(f"Emissions Trend for {country}")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

            # Results
            st.success(f"✅ Predicted Emissions for **{country}** in **{year}**: `{prediction:.2f}` kilotonnes CO₂ equivalent")
            st.markdown(f"📉 **Change from average (last 5 years)**: `{percent_change:.2f}%`")
            st.markdown(f"🌲 Estimated trees needed to offset: **{prediction / 7.8:,.0f} million trees**")

            # Evaluation logic
            if percent_change < -5:
                color = "#2e7d32"  # dark green
                status = "🌿 Below average: Positive environmental performance"
            elif abs(percent_change) <= 5:
                color = "#f9a825"  # amber
                status = "⚖️ Near average: Stable performance"
            else:
                color = "#c62828"  # red
                status = "🚨 Above average: Urgent action needed!"

            st.markdown(f"""
                <div style="background-color:{color}; padding: 12px; color: white;
                            font-size: 18px; border-radius: 8px; text-align: center;">
                    {status}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Not enough historical data available for this country and category.")
    else:
        st.warning("Please select both a country and category.")
