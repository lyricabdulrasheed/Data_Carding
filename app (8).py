
import gradio as gr

# Ethics DataCard content for forest wildfire prediction model
datacard_content = """
# Ethics DataCard for Forest Wildfire Prediction Model

## Dataset Overview
**Input Variables**: Temperature, Humidity, Wind Speed, Rainfall, Fuel Moisture, Vegetation Type, Slope, Region
**Output Variables**: Fire Size, Fire Duration, Suppression Cost, Fire Occurrence

## Data Collection Process
Weather data, satellite imagery, vegetation reports, topographical data.
Data Sourcing and Privacy: Data is sourced from public and licensed sources, ensuring proper consent and anonymization of private information.

## Bias Considerations
**Potential Bias**: Historical data may underreport wildfires in remote or underserved regions.
**Mitigation**: The model is designed to minimize biases through diverse data sources and continuous monitoring.

## Fairness & Justice
The model predicts wildfires across various regions and forest types, avoiding disproportionate impacts on vulnerable communities.
The model focuses on reducing both unnecessary evacuations (false positives) and failure to predict real wildfires (false negatives).

## Privacy and Security
The model anonymizes personal information inadvertently captured through satellite data, weather stations, or geographic data.
No social media or surveillance data is used without explicit consent.

## Sustainability and Environmental Impact
The model assists in land management, wildfire mitigation, and reducing wildfire severity.
The model informs decisions on land use, deforestation, and conservation practices.

## Model Limitations
The model's accuracy may vary based on the region and data availability.
The model may have limitations in predicting wildfires in regions with insufficient historical data.
The model is regularly updated to incorporate new climate data and environmental changes.

## Accountability and Transparency
The development team monitors the model for performance and adapts it to new data and environmental shifts.
Stakeholders are informed of the model's limitations to ensure proper interpretation of predictions.
 A process is in place to communicate and address false predictions and improve the model.

## Societal Impact
The model contributes to protecting human lives and the environment through better wildfire planning and response.
The model has the potential to inform policy changes in land management, conservation, and emergency response strategies.
"""

# Function to display the DataCard
def display_datacard():
    return datacard_content

# Gradio interface to display the ethics DataCard
iface = gr.Interface(fn=display_datacard, inputs=[], outputs="markdown")

# Launch the Gradio interface
iface.launch()
