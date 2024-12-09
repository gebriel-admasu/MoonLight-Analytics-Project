# Solar Radiation Dashboard

An interactive Streamlit dashboard to explore and analyze solar radiation and environmental data for multiple regions. Designed for **AI Mastery Week 0 Challenge by Kifiya AI Mastery**.

---

## 📖 Overview

This dashboard provides interactive visualizations to help users analyze solar radiation trends, correlations, and other insights. It supports data from **Benin**, **Sierra Leone**, and **Togo**, focusing on:

- Time-Series Analysis
- Correlation Analysis
- Wind-Solar Interaction
- Outliers Detection

---

## 🚀 Features

- 📊 **Interactive Visualizations**: Line charts, scatter plots, heatmaps, and more.
- 🧹 **Data Cleaning**: Handles missing values and removes anomalies.
- 🔄 **Dynamic Data Loading**: Supports multiple datasets with automated preprocessing.
- 🖱️ **User-Friendly Interface**: Intuitive navigation and interactive controls.

---

## 📂 Project Structure

```plaintext
.
├── src/
│   ├── app/
│   │   ├── main.py         # Main dashboard application
│   │   ├── data_loader.py  # Functions to load and preprocess data
│   │   ├── utils.py        # Utility functions for analysis
│   └── assets/
│       ├── data/           # CSV datasets for Benin, Sierra Leone, and Togo
│       ├── screenshots/    # Screenshots for documentation
├── tests/
│   ├── test_main.py        # Unit tests for the application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🔧 Setup Instructions
Follow these steps to set up and run the dashboard locally:

1. Clone the Repository
```
git clone https://github.com/your-username/solar-radiation-dashboard.git
```
3. Navigate to the Project Directory
```
cd solar-radiation-dashboard
```
3. Create and Activate a Virtual Environment
For Windows:
```
python -m venv venv
.\venv\Scripts\activate
```
For macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
4. Install Dependencies
```
pip install -r requirements.txt
```
5. Run the Dashboard
bash
```
streamlit run src/app/main.py
```
## ✨ Visualizations
1. Time-Series Analysis
Analyze GHI, DNI, and DHI trends over time for different regions.

2. Correlation Heatmap
Visualize relationships between solar radiation components and other variables.

3. Wind-Solar Interaction
Understand how wind speed affects solar radiation.

4. Outliers Detection
Detect anomalies in solar radiation data using box plots.

## 🛠️ Key Insights
1. Solar radiation trends differ across regions, with noticeable peaks and anomalies.
2. Temperature has a strong correlation with solar irradiance, as evident in the heatmap.
3. Wind speed impacts solar energy generation, particularly during high GHI periods.

## 🧪 Running Tests
Unit tests are included to ensure the functionality of core components:


```pytest
```
## 📜 License
This project is open-source under the MIT License.

## 🙌 Acknowledgments
Special thanks to Kifiya AI Mastery for providing the opportunity to work on this insightful challenge.

