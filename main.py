import streamlit as st
import pandas as pd
from st_timeline import st_timeline
import plotly.express as px
import connections_graph


st.title("Lockdown and & Diabetes")
st.header("Introduction")
st.markdown(
    """
    Diabetes Type 2 is a non communicable disease where the body does not use insulin properly to manage blood sugar. Unlike Type 1 which is hereditary, Type 2 can be caused by over - consumption of certain foods and unhealthy lifestyle choices. 

    The Covid-19 pandemic began in late - 2019, and continues to infect people today, though at a lower rate. For more information, skip to [Covid Timeline](#covid-19-timeline)
    """
)

st.header("Research Question")
st.markdown("""
To what extent did lockdown during Covid-19 (2019-2023) affect the prevalence and deaths from Diabetes in Singapore?
""")

st.header("Background Data")
data = {
    "Year": [2022, 2020, 2017, 2013, 2010],
    "Value": [8.5, 9.5, 8.8, None, 8.6],
    "Size": [10, 10, 10, 10, 10],
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Sort the values by Year chronologically (good practice)
df = df.sort_values("Year")

fig = px.scatter(
    df,
    x="Year",
    y="Value",
    size_max=10,
    title="Prevalence of Diabetes in Singapore (data.gov.sg)",
    labels={
        "Year": "Year",
        "Value": "% of Pop.",
    },
    size="Size",
)

st.plotly_chart(fig, use_container_width=True)
st.markdown(
    "*Source: **data.gov.sg**. Click [here](#bibliography) to view the bibliography.*"
)
st.write("")

# ---------------------------------------------------------
# ANIMATED GLOBAL MAP (UPDATED WITH DISCRETE YELLOW-RED SCALE)
# ---------------------------------------------------------
# Load the global data from the CSV
df_global = pd.read_csv("global.csv")

# Sort by Year to ensure the animation slider plays in chronological order
df_global = df_global.sort_values("Year")

# Name of the column containing the raw numbers
value_col = "Total deaths from diabetes mellitus among both sexes"

# 1. Define the numerical breakpoints from your image
bins = [-1, 1000, 3000, 10000, 30000, 100000, float("inf")]

# 2. Define the text labels for the legend
labels = [
    "0 - 1,000",
    "1,000 - 3,000",
    "3,000 - 10,000",
    "10,000 - 30,000",
    "30,000 - 100,000",
    "100,000+",
]

# 3. Create a new column in the dataframe that assigns each row to a category
df_global["Death Range"] = pd.cut(df_global[value_col], bins=bins, labels=labels)

# 4. Map exact hex colors to those labels (Matching the Yellow -> Dark Red image)
color_map = {
    "0 - 1,000": "#FEE8C8",  # Pale yellow/beige
    "1,000 - 3,000": "#FDD49E",  # Light orange
    "3,000 - 10,000": "#FDBB84",  # Orange
    "10,000 - 30,000": "#FC8D59",  # Dark orange
    "30,000 - 100,000": "#E34A33",  # Red-orange
    "100,000+": "#B30000",  # Dark red
}

# Create the animated Plotly map using the new discrete 'Death Range' column
fig_map = px.choropleth(
    df_global,
    locations="Code",
    color="Death Range",  # <-- Now mapping by the text categories
    hover_name="Entity",
    hover_data={value_col: True},  # Shows exact number on hover
    animation_frame="Year",
    color_discrete_map=color_map,  # <-- Applies our custom colors
    category_orders={
        "Death Range": labels
    },  # <-- Forces legend to stay in perfect order
    projection="natural earth",
    title="Global Total Deaths from Diabetes",
)

# Add white outlines (borders) to the countries
fig_map.update_traces(
    marker_line_color="white",
    marker_line_width=0.5,
)

# Customize the map's layout to be TRANSPARENT so it matches Streamlit's theme
fig_map.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=40, b=0),
    geo=dict(
        bgcolor="rgba(0,0,0,0)",
        showframe=False,
        showcoastlines=False,
    ),
    legend_title_text="Total Deaths",  # Cleans up the legend title
)

# Display the map in Streamlit
st.plotly_chart(fig_map, use_container_width=True, theme="streamlit")
st.markdown(
    "*Source: **Our World In Data**. Click [here](#bibliography) to view the bibliography.*"
)
st.write("")

st.header("Covid-19 Timeline")
my_events = [
    {
        "date": "December 2019",
        "title": "Covid-19 Begins",
        "description": "The early form of Covid-19 begins to spread rapidly in Wuhan, China.",
    },
    {
        "date": "13th January 2020",
        "title": "First case outside of China",
        "description": "The Thai government confirms the first case of Covid-19 outside of China.",
    },
    {
        "date": "23rd January 2020",
        "title": "Wuhan in lockdown",
        "description": "Wuhan, China is placed under lockdown due to Covid-19",
    },
    {
        "date": "23rd January 2020",
        "title": "First confirmed case in Singapore",
        "description": "A 66 year old Chinese national test positive for Covid-19.",
    },
    {
        "date": "21st March 2020",
        "title": "First 2 deaths in Singapore",
        "description": "The Singapore government announces the first 2 deaths due to Covid-19 in Singapore.",
    },
    {
        "date": "3rd April 2020",
        "title": "Circuit Breaker measures announced",
        "description": "Singapore Prime Minister announces circuit breaker measures.",
    },
    {
        "date": "16th & 18th November 2020",
        "title": "Moderna & Pfizer Vaccines",
        "description": "Moderna & Pfizer Vaccines are found to be more than 95% effective in clinical trials.",
    },
]

# Render the timeline (you can adjust the height here)
st_timeline(my_events, height=1000)
st.markdown(
    """
    *Source: **CDC** & **CNA**. Click [here](#bibliography) to view the bibliography.*
    """
)  # Define your timeline data

st.header("Government response")
st.markdown(
    """
    Aware of the negative health effects of a sedentary life style for everyone (not just DM patients), the singapore government - specifically Active SG - made multiple steps to keep the population active throughout lockdown. Click through the tabs below to see.
    """
)
tab4, tab1, tab2, tab3 = st.tabs(
    [
        "**Circuit - Breaker**",
        "**Active Enabler**",
        "**Active SG Circle**",
        "**DM Patients**",
    ]
)
with tab4:
    st.markdown(
        """
        :green-badge[**Political**]

        The circuit breaker laws and policies are the main cause of mass sedentary lifestyles during the pandemic. This contributed to the cases of DM 2 during the pandemic, and worsened the lifestyle of those who had already developed the disease. 
        """
    )
with tab1:
    st.markdown(
        """
        :blue-badge[**Economic**] :green-badge[**Political**]

        Over 2 Million SGD was offered in grants to programs / companies that helped keep the Singaporean population active. Seeing as this was offered during April 2020, the pandemic was likely a contributor to this. The programs supported by these grants would likely have helped lessen the blow for DM patients at home (helping to reduce strain on medical facilities), and prevented more people from developing Diabetes type 2, by keeping them physically active. The grants given would have supported companies and projects financially during Covid - 19. 
        """
    )
with tab2:
    st.markdown(
        """
        :red-badge[**Social**]

        Active SG circle is a central website for online - based physical training, and booking publicly available fitness events. The online classes likely helped keep SG’s population more active, helping DM patients, and preventing more from developing DM 2. 
        """
    )

with tab3:
    st.markdown(
        """
        :blue-badge[**Economic**] :red-badge[**Social**]

        Long term, incurable diseases such as DM can cause significant stress on patients. Dealing with not only the direct symptoms of the disease, but also keeping up with treatment.
        Paying for the treatment of their disease adds extra financial strain upon DM patients. In countries where such treatments are subsidised (very few), the government still has to pay for such treatments. Both ways, DM has direct negative economic effects.
        """
    )
st.header("Systems Graph")
st.markdown(
    """
    Diabetes Type-2 is caused and affected by lifestyle choices such as healthy food and exercise. The Circuit - Breaker / Lockdown measures made during the pandemic significantly restricted people's access to the outdoors, forcing them to stay at home, leading to a more sedintary lifestyle. Furthermore, the pressure placed upon healthcare systems by the pandemic often made medication less accesible. Both forms of diabetes require long-term treatment, and a discrupted healthcare system could cause disruptions in the level of care provided to diabetes patients. There is also some evidence that Covid-19 affects Diabetes patients in more acute ways.
    The widespread effects of Covid-19 on the healthcare system have been widely documented. A paper written by medical scientists at Beijing's China Academy of Chinese Medical Sciences discusses the interplay between Diabetes and Covid-19. They presented evidence for 
     is a systems graph, which represents these elements. Mouse over a node / connection to see how it affects / is affected by other nodes.

    *:red[Red] = Negative, :green[Green] = Positive*
    """
)

connections_graph.render()

st.header("Bibliography")

st.markdown(
    """
- [Global Death from Diabetes, Our World In Data](https://ourworldindata.org/grapher/deaths-from-diabetes-ghe?time=2000..latest&country=RUS~CHN~USA~BRA~OWID_WRL)
- [Covid-19 Timeline, Center for Disease Control](https://www.cdc.gov/museum/timeline/covid19.html)
- [Diabetes prevalence in Singapore, Data.gov.sg](https://data.gov.sg/datasets?query=diabetes&resultId=d_711586488b23182801c94bd7b6807833)
- [Progression of Covid-19 in Singapore, CNA](https://www.channelnewsasia.com/singapore/singapore-covid-19-outbreak-evolved-coronavirus-deaths-timeline-764126)
- [Contact tracing in Singapore, global-is-asian](https://lkyspp.nus.edu.sg/gia/article/tracetogether-questions-of-data-and-privacy)
- [Active Enablers program, Straits Times](https://www.straitstimes.com/sport/coronavirus-active-enabler-programme-offering-2-million-grant-to-get-singaporeans-active)

"""
)
