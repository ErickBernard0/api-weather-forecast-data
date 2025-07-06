import streamlit as st
import altair as alt
import pandas as pd
from sqlalchemy import create_engine
from src.config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

# connect to the database
def get_engine():
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    engine = create_engine(DATABASE_URL)
    return engine

# load data from the database
@st.cache_data
def load_data():
    engine = get_engine()
    query = "SELECT * FROM weather_forecast"
    df = pd.read_sql(query, engine)
    return df

# ---------------------------
# Streamlit App
# ---------------------------

# Set up the Streamlit app
st.set_page_config(page_title="Weather Forecast BR", layout="wide")
st.title("⛅ Weather Forecast - Capitals of Brazil")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("🎯 Filters")

# Filter data
states = sorted(df['state'].unique())
selected_state = st.sidebar.selectbox("Select a state", states)

cities = sorted(df[df['state'] == selected_state]['city'].unique())
selected_city = st.sidebar.selectbox("Select a city", cities)

# Filtered DataFrame
df_filt = df[(df['state'] == selected_state) & (df['city'] == selected_city)].copy()
df_filt['date'] = pd.to_datetime(df_filt['datetime']).dt.strftime('%d/%m')

# Get highlight rows
max_temp_row = df_filt.loc[df_filt['tempmax'].idxmax()]
min_temp_row = df_filt.loc[df_filt['tempmin'].idxmin()]

# Temperature chart
chart = (
    alt.Chart(df_filt)
    .transform_fold(['tempmax', 'tempmin'], as_=['Type', 'Temperature'])
    .mark_line(point=True)
    .encode(
        x=alt.X('date:N', title='', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Temperature:Q', title='Temperature (°C)'),
        color=alt.Color(
            'Type:N',
            title='Type:',
            legend=alt.Legend(orient='top', title='')
        ),
        tooltip=['date', 'tempmax', 'tempmin']
    )
    .properties(
        title=f"🌡️ Max and Min Temperature - {selected_city} / {selected_state}",
        width='container'
    )
)
# Highlights section
left_col, right_col = st.columns([1, 3])

with left_col:
    st.subheader("📌 Highlights")
    st.metric(
        label=f"🔥 Highest temperature ({max_temp_row['date']})",
        value=f"{max_temp_row['tempmax']}°C"
    )
    st.metric(
        label=f"❄️ Lowest temperature ({min_temp_row['date']})",
        value=f"{min_temp_row['tempmin']}°C"
    )

with right_col:
    tab1, tab2 = st.tabs(["📈 Chart", "📋 Table"])

    with tab1:
        st.altair_chart(chart, use_container_width=True)

    with tab2:
        st.dataframe(df_filt, use_container_width=True)