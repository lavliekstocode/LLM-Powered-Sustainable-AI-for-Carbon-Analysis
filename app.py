import streamlit as st
import os

st.set_page_config(
    page_title="SustainAI - AI Carbon Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #E8F5E9 0%, #C8E6C9 50%, #A5D6A7 100%);
    }
    [data-testid="stSidebar"] .stRadio label {
        color: #1B5E20;
        font-weight: 500;
    }
    .stMetric {
        background: linear-gradient(135deg, #E8F5E9, #F1F8E9);
        padding: 16px;
        border-radius: 12px;
        border-left: 4px solid #00C853;
        box-shadow: 0 2px 8px rgba(0,200,83,0.10);
    }
    [data-testid="stMetricValue"] {
        color: #1B5E20;
        font-weight: 700;
    }
    [data-testid="stMetricDelta"] {
        color: #2E7D32;
    }
    h1 {
        color: #1B5E20 !important;
        border-bottom: 3px solid #00C853;
        padding-bottom: 8px;
    }
    h2, h3 {
        color: #2E7D32 !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #00C853, #00E676) !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        box-shadow: 0 3px 12px rgba(0,200,83,0.3) !important;
    }
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #00E676, #69F0AE) !important;
        box-shadow: 0 4px 16px rgba(0,200,83,0.4) !important;
    }
    .stSelectbox label, .stTextArea label, .stNumberInput label, .stSlider label {
        color: #1B5E20 !important;
        font-weight: 500 !important;
    }
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
    }
    [data-testid="stExpander"] {
        border: 1px solid #A5D6A7;
        border-radius: 8px;
        background-color: #F1F8E9;
    }
    .stDownloadButton > button {
        background: linear-gradient(135deg, #1B5E20, #2E7D32) !important;
        color: white !important;
        border-radius: 8px !important;
    }
    .stInfo {
        background-color: #E8F5E9 !important;
        border-left-color: #00C853 !important;
        color: #1B5E20 !important;
    }
    .stSuccess {
        background-color: #C8E6C9 !important;
        border-left-color: #00C853 !important;
    }
    div[data-testid="stSidebarNav"] {
        background: transparent;
    }
    .stCaption {
        color: #4CAF50 !important;
    }
</style>
""", unsafe_allow_html=True)

from utils.token_estimator import TokenEstimator
from utils.energy_model import EnergyModel
from utils.model_profiles import MODEL_PROFILES, get_model_profile, get_all_models, get_efficiency_ranking
from utils.company_profiles import COMPANY_PROFILES, get_company_profile, get_all_companies, get_sustainability_ranking, get_total_industry_emissions
from utils.enterprise_calculator import EnterpriseCalculator
from utils.carbon_equivalency import CarbonEquivalency
from utils.llm_explainer import LLMExplainer
from utils.report_generator import ReportGenerator
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

token_estimator = TokenEstimator()
carbon_equiv = CarbonEquivalency()
llm_explainer = LLMExplainer()
report_generator = ReportGenerator()

if 'last_impact' not in st.session_state:
    st.session_state.last_impact = None

st.sidebar.markdown("## 🌱 SustainAI")
st.sidebar.markdown("*AI Carbon Intelligence Dashboard*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    [
        "Prompt Impact Calculator",
        "Model Emission Comparison",
        "Company Carbon Dashboards",
        "Enterprise Simulator",
        "Carbon Equivalency Visualizer",
        "Download Reports"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Settings")
default_region = st.sidebar.selectbox(
    "Default Region",
    options=list(EnergyModel.get_region_display_names().keys()),
    format_func=lambda x: EnergyModel.get_region_display_names()[x],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "SustainAI helps you understand and reduce the environmental impact of AI usage. "
    "Calculate emissions, compare models, and get personalized recommendations."
)


def render_prompt_calculator():
    st.title("Prompt Impact Calculator")
    st.markdown("Calculate the environmental impact of your AI queries in real-time.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        prompt_text = st.text_area(
            "Enter your prompt",
            height=150,
            placeholder="Type or paste your AI prompt here...",
            help="Enter the text you would send to an AI model"
        )
    
    with col2:
        selected_model = st.selectbox(
            "Select AI Model",
            options=get_all_models(),
            format_func=lambda x: MODEL_PROFILES[x]['name']
        )
        
        region = st.selectbox(
            "Your Region",
            options=list(EnergyModel.get_region_display_names().keys()),
            format_func=lambda x: EnergyModel.get_region_display_names()[x],
            index=0
        )
        
        include_response = st.checkbox("Include estimated response tokens", value=True)
    
    if st.button("Calculate Impact", type="primary", use_container_width=True):
        if prompt_text.strip():
            token_analysis = token_estimator.get_total_tokens(
                prompt_text, 
                selected_model, 
                include_response=include_response
            )
            
            energy_model = EnergyModel(region=region)
            impact = energy_model.calculate_full_impact(
                token_analysis['total_tokens'],
                selected_model,
                region
            )
            
            equivalencies = carbon_equiv.calculate_all_equivalencies(
                impact['co2']['co2_kg']
            )
            
            st.session_state.last_impact = {
                'tokens': token_analysis['total_tokens'],
                'model': selected_model,
                'energy_wh': impact['energy']['total_energy_wh'],
                'co2_grams': impact['co2']['co2_grams'],
                'region': EnergyModel.get_region_display_names()[region],
                'trees': equivalencies['trees']['count'],
                'car_km': equivalencies['car']['km'],
                'smartphone_charges': equivalencies['devices']['smartphone_charges'],
                'equivalencies': equivalencies
            }
            
            st.markdown("---")
            st.subheader("Impact Results")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    "Total Tokens",
                    f"{token_analysis['total_tokens']:,}",
                    delta=f"{token_analysis['prompt_tokens']} prompt + {token_analysis['response_tokens']} response"
                )
            
            with col2:
                st.metric(
                    "Energy Used",
                    f"{impact['energy']['total_energy_wh']:.6f} Wh",
                    delta=f"{impact['energy']['total_energy_kwh']:.9f} kWh"
                )
            
            with col3:
                st.metric(
                    "CO2 Emitted",
                    f"{impact['co2']['co2_grams']:.6f} g",
                    delta=f"{impact['co2']['co2_kg']:.9f} kg"
                )
            
            with col4:
                profile = get_model_profile(selected_model)
                st.metric(
                    "Efficiency Rating",
                    profile['efficiency_rating'] if profile else "N/A",
                    delta="Model Efficiency"
                )
            
            st.markdown("---")
            st.subheader("Environmental Equivalencies")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.markdown("### Trees")
                st.markdown(f"**{equivalencies['trees']['count']:.4f}**")
                st.caption("trees needed for 1 year")
            
            with col2:
                st.markdown("### Car Distance")
                st.markdown(f"**{equivalencies['car']['km']:.4f}** km")
                st.caption("of driving")
            
            with col3:
                st.markdown("### Phone Charges")
                st.markdown(f"**{equivalencies['devices']['smartphone_charges']:.2f}**")
                st.caption("full charges")
            
            with col4:
                st.markdown("### Streaming")
                st.markdown(f"**{equivalencies['digital']['streaming_hours']:.2f}** hrs")
                st.caption("of HD video")
            
            with col5:
                st.markdown("### Coffee")
                st.markdown(f"**{equivalencies['food']['coffee_cups']:.2f}**")
                st.caption("cups of coffee")
            
            with st.expander("View LLM Explanation"):
                explanation = llm_explainer.explain_emission_impact(st.session_state.last_impact)
                st.markdown(explanation)
        else:
            st.warning("Please enter a prompt to calculate its impact.")


def render_model_comparison():
    st.title("Model Emission Comparison")
    st.markdown("Compare the environmental footprint of different AI models.")
    
    efficiency_data = get_efficiency_ranking()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Energy Efficiency Ranking")
        
        df = pd.DataFrame([
            {
                'Model': m['name'],
                'Company': m['company'],
                'Energy/Token (Wh)': m['energy_per_token_wh'],
                'CO2/1M Tokens (g)': m['co2_per_million_tokens_g'],
                'Rating': m['efficiency_rating']
            }
            for m in efficiency_data
        ])
        
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("CO2 per Million Tokens")
        
        fig = go.Figure(data=[
            go.Bar(
                x=[m['name'] for m in efficiency_data],
                y=[m['co2_per_million_tokens_g'] for m in efficiency_data],
                marker_color=[
                    '#2e7d32' if m['efficiency_rating'] == 'A+' else
                    '#4caf50' if m['efficiency_rating'] == 'A' else
                    '#8bc34a' if m['efficiency_rating'] == 'A-' else
                    '#ffc107' if m['efficiency_rating'] == 'B' else '#ff9800'
                    for m in efficiency_data
                ],
                text=[f"{m['co2_per_million_tokens_g']:.1f}g" for m in efficiency_data],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            xaxis_title='Model',
            yaxis_title='CO2 (g per 1M tokens)',
            template='plotly_white',
            height=400,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Detailed Model Profiles")
    
    selected_models = st.multiselect(
        "Select models to compare",
        options=get_all_models(),
        default=['gpt-3.5-turbo', 'gpt-4', 'claude-3.5-sonnet', 'gemini-pro'],
        format_func=lambda x: MODEL_PROFILES[x]['name']
    )
    
    if selected_models:
        cols = st.columns(len(selected_models))
        
        for idx, model_id in enumerate(selected_models):
            profile = get_model_profile(model_id)
            with cols[idx]:
                st.markdown(f"### {profile['name']}")
                st.markdown(f"**Company:** {profile['company']}")
                st.markdown(f"**Parameters:** {profile['parameters']}")
                st.markdown(f"**Efficiency:** {profile['efficiency_rating']}")
                st.markdown(f"**Energy/Token:** {profile['energy_per_token_wh']} Wh")
                st.markdown(f"**Training CO2:** {profile['training_co2_tonnes']:,} tonnes")
                st.markdown(f"**Hardware:** {profile['hardware']}")
                st.markdown(f"**Context:** {profile['context_window']:,} tokens")
                
                with st.expander("Notes"):
                    st.markdown(profile['notes'])


def render_company_dashboards():
    st.title("Company Carbon Dashboards")
    st.markdown("Explore the environmental impact of major AI companies.")
    
    industry_totals = get_total_industry_emissions()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Annual CO2",
            f"{industry_totals['total_annual_co2_tonnes']:,} tonnes",
            delta="All tracked companies"
        )
    
    with col2:
        st.metric(
            "Inference CO2",
            f"{industry_totals['total_annual_inference_co2_tonnes']:,} tonnes",
            delta="Annual inference"
        )
    
    with col3:
        st.metric(
            "Training CO2",
            f"{industry_totals['total_annual_training_co2_tonnes']:,} tonnes",
            delta="Estimated training"
        )
    
    with col4:
        st.metric(
            "Daily Queries",
            f"{industry_totals['total_daily_queries']:,}",
            delta="All companies"
        )
    
    st.markdown("---")
    
    sustainability_ranking = get_sustainability_ranking()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Sustainability Ranking")
        
        fig = go.Figure(data=[
            go.Bar(
                x=[c['name'] for c in sustainability_ranking],
                y=[c['carbon_intensity_score'] for c in sustainability_ranking],
                marker_color=[
                    '#2e7d32' if c['sustainability_grade'].startswith('A') else
                    '#ffc107' if c['sustainability_grade'] == 'B' else '#ff9800'
                    for c in sustainability_ranking
                ],
                text=[c['sustainability_grade'] for c in sustainability_ranking],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            xaxis_title='Company',
            yaxis_title='Carbon Intensity Score (lower is better)',
            template='plotly_white',
            height=350,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Annual Emissions Breakdown")
        
        fig = go.Figure(data=[
            go.Bar(
                name='Inference',
                x=[c['name'] for c in sustainability_ranking],
                y=[c['estimated_annual_inference_co2_tonnes'] for c in sustainability_ranking],
                marker_color='#4caf50'
            ),
            go.Bar(
                name='Training',
                x=[c['name'] for c in sustainability_ranking],
                y=[c['estimated_training_co2_tonnes'] for c in sustainability_ranking],
                marker_color='#ff9800'
            )
        ])
        
        fig.update_layout(
            xaxis_title='Company',
            yaxis_title='CO2 (tonnes/year)',
            barmode='stack',
            template='plotly_white',
            height=350,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Company Profiles")
    
    selected_company = st.selectbox(
        "Select a company",
        options=get_all_companies(),
        format_func=lambda x: COMPANY_PROFILES[x]['name']
    )
    
    if selected_company:
        company = get_company_profile(selected_company)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.markdown(f"### {company['name']}")
            st.markdown(f"**Headquarters:** {company['headquarters']}")
            st.markdown(f"**Founded:** {company['founded']}")
            st.markdown(f"**Sustainability Grade:** {company['sustainability_grade']}")
            st.markdown(f"**Renewable Energy:** {company['renewable_energy_percent']}%")
        
        with col2:
            st.markdown("### Emissions")
            st.markdown(f"**Annual Inference CO2:** {company['estimated_annual_inference_co2_tonnes']:,} tonnes")
            st.markdown(f"**Training CO2 (Est.):** {company['estimated_training_co2_tonnes']:,} tonnes")
            st.markdown(f"**Total CO2:** {company['total_estimated_co2_tonnes']:,} tonnes")
            st.markdown(f"**Growth Rate:** {company['growth_rate_percent']}%")
        
        with col3:
            st.markdown("### Infrastructure")
            st.markdown(f"**Daily Queries:** {company['daily_queries_estimate']:,}")
            st.markdown(f"**PUE Estimate:** {company['pue_estimate']}")
            st.markdown(f"**Hardware:** {company['hardware']}")
            st.markdown(f"**Data Centers:** {', '.join(company['data_centers'])}")
        
        st.markdown("### Sustainability Initiatives")
        for initiative in company['sustainability_initiatives']:
            st.markdown(f"- {initiative}")
        
        st.markdown("### Notes")
        st.info(company['notes'])


def render_enterprise_simulator():
    st.title("Enterprise AI Usage Impact Simulator")
    st.markdown("Calculate your organization's AI carbon footprint and get actionable recommendations.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Enterprise Profile")
        
        employees = st.number_input(
            "Number of employees using AI",
            min_value=1,
            max_value=100000,
            value=100,
            step=10
        )
        
        queries_per_day = st.slider(
            "Average AI queries per person per day",
            min_value=1,
            max_value=100,
            value=15
        )
        
        selected_model = st.selectbox(
            "Primary AI model used",
            options=get_all_models(),
            format_func=lambda x: MODEL_PROFILES[x]['name'],
            key="enterprise_model"
        )
        
        region = st.selectbox(
            "Company headquarters region",
            options=list(EnergyModel.get_region_display_names().keys()),
            format_func=lambda x: EnergyModel.get_region_display_names()[x],
            index=0,
            key="enterprise_region"
        )
        
        working_days = st.number_input(
            "Working days per year",
            min_value=100,
            max_value=365,
            value=250
        )
    
    with col2:
        st.subheader("Advanced Settings")
        
        avg_tokens = st.slider(
            "Average tokens per query (prompt + response)",
            min_value=100,
            max_value=5000,
            value=500
        )
        
        st.info(
            "Tip: Simple queries typically use 200-400 tokens. "
            "Complex analysis or creative writing can use 1000-3000 tokens."
        )
    
    if st.button("Calculate Enterprise Impact", type="primary", use_container_width=True):
        calculator = EnterpriseCalculator(region=region)
        
        impact = calculator.calculate_annual_impact(
            employees=employees,
            queries_per_person_per_day=queries_per_day,
            model=selected_model,
            avg_tokens_per_query=avg_tokens,
            working_days=working_days
        )
        
        offset_plan = calculator.generate_offset_plan(impact['co2']['annual_kg'])
        
        st.markdown("---")
        st.subheader("Annual Impact Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Annual Queries",
                f"{impact['queries']['annual']:,}",
                delta=f"{impact['queries']['daily']:,}/day"
            )
        
        with col2:
            st.metric(
                "Annual Energy",
                f"{impact['energy']['annual_kwh']:.4f} kWh",
                delta=f"{impact['energy']['annual_mwh']:.6f} MWh"
            )
        
        with col3:
            st.metric(
                "Annual CO2",
                f"{impact['co2']['annual_kg']:.4f} kg",
                delta=f"{impact['co2']['annual_tonnes']:.6f} tonnes"
            )
        
        with col4:
            st.metric(
                "CO2 per Employee",
                f"{impact['per_employee']['annual_co2_kg']:.6f} kg",
                delta="Annual"
            )
        
        st.markdown("---")
        st.subheader("Carbon Offset Plan")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Tree Planting")
            st.markdown(f"**Trees needed:** {offset_plan['tree_offset']['trees_needed']:,.0f}")
            st.markdown(f"**Area required:** {offset_plan['tree_offset']['area_hectares']:.2f} hectares")
        
        with col2:
            st.markdown("### Carbon Credits")
            st.markdown(f"**Credits needed:** {offset_plan['carbon_credits']['credits_needed']:.2f} tonnes")
            st.markdown(f"**Cost range:** ${offset_plan['carbon_credits']['cost_low_usd']:,.2f} - ${offset_plan['carbon_credits']['cost_high_usd']:,.2f}")
        
        with col3:
            st.markdown("### Renewable Energy")
            st.markdown(f"**kWh to offset:** {offset_plan['renewable_energy']['kwh_to_offset']:,.2f}")
            st.markdown(f"**Solar panels equiv:** {offset_plan['renewable_energy']['solar_panels_equivalent']:.1f}")
        
        st.markdown("---")
        st.subheader("Recommendations")
        
        for rec in offset_plan['recommendations']:
            with st.expander(f"{rec['priority']}: {rec['action']}"):
                st.markdown(f"**Category:** {rec['category']}")
                st.markdown(f"**Potential Reduction:** {rec['potential_reduction']}")
                st.markdown(rec['description'])
        
        st.markdown("---")
        st.subheader("Model Comparison for Your Use Case")
        
        all_models = get_all_models()
        comparison = calculator.compare_models_for_enterprise(
            employees=employees,
            queries_per_person_per_day=queries_per_day,
            models=all_models
        )
        
        fig = go.Figure(data=[
            go.Bar(
                x=[c['model_name'] for c in comparison],
                y=[c['annual_co2_kg'] for c in comparison],
                marker_color=[
                    '#2e7d32' if c['efficiency_rating'] == 'A+' else
                    '#4caf50' if c['efficiency_rating'] == 'A' else
                    '#8bc34a' if c['efficiency_rating'] == 'A-' else
                    '#ffc107' if c['efficiency_rating'] == 'B' else '#ff9800'
                    for c in comparison
                ],
                text=[f"{c['annual_co2_kg']:.4f} kg" for c in comparison],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title='Annual CO2 by Model for Your Enterprise',
            xaxis_title='Model',
            yaxis_title='Annual CO2 (kg)',
            template='plotly_white',
            height=400,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.session_state.enterprise_impact = impact
        st.session_state.enterprise_offset = offset_plan
        st.session_state.enterprise_comparison = comparison


def render_carbon_equivalency():
    st.title("Carbon Equivalency Visualizer")
    st.markdown("Understand carbon emissions through real-world comparisons.")
    
    st.subheader("Custom CO2 Calculator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        co2_input = st.number_input(
            "Enter CO2 amount (grams)",
            min_value=0.0,
            max_value=1000000.0,
            value=100.0,
            step=10.0
        )
        
        co2_kg = co2_input / 1000
        
        st.markdown(f"**= {co2_kg:.6f} kg CO2**")
        st.markdown(f"**= {co2_kg/1000:.9f} tonnes CO2**")
    
    with col2:
        equivalencies = carbon_equiv.calculate_all_equivalencies(co2_kg)
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("### Nature")
            st.markdown(f"**Trees (1 year):** {equivalencies['trees']['count']:.4f}")
            st.markdown(f"*{equivalencies['trees']['formula']}*")
        
        with col_b:
            st.markdown("### Transport")
            st.markdown(f"**Car driving:** {equivalencies['car']['km']:.4f} km")
            st.markdown(f"**Flights (Paris-NYC):** {equivalencies['flights']['paris_nyc']:.6f}")
        
        with col_c:
            st.markdown("### Energy")
            st.markdown(f"**Household hours:** {equivalencies['household']['hours']:.4f}")
            st.markdown(f"**LPG burned:** {equivalencies['lpg']['kg']:.6f} kg")
    
    st.markdown("---")
    
    fig = go.Figure(data=[
        go.Bar(
            x=['Trees', 'Car km', 'Flights (x100)', 'Phone Charges', 'Streaming hrs', 'Coffee Cups'],
            y=[
                equivalencies['trees']['count'],
                equivalencies['car']['km'],
                equivalencies['flights']['paris_nyc'] * 100,
                equivalencies['devices']['smartphone_charges'],
                equivalencies['digital']['streaming_hours'],
                equivalencies['food']['coffee_cups']
            ],
            marker_color=['#2e7d32', '#1976d2', '#f57c00', '#7b1fa2', '#c62828', '#795548'],
            text=[
                f"{equivalencies['trees']['count']:.4f}",
                f"{equivalencies['car']['km']:.4f}",
                f"{equivalencies['flights']['paris_nyc']*100:.4f}",
                f"{equivalencies['devices']['smartphone_charges']:.2f}",
                f"{equivalencies['digital']['streaming_hours']:.2f}",
                f"{equivalencies['food']['coffee_cups']:.2f}"
            ],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=f'Carbon Equivalencies for {co2_input:.2f}g CO2',
        yaxis_title='Equivalent Units',
        template='plotly_white',
        height=400,
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Formula Reference")
    
    formulas = carbon_equiv.get_formula_explanations()
    
    for key, formula in formulas.items():
        with st.expander(f"{key.title()} Conversion"):
            st.markdown(f"**Formula:** `{formula['formula']}`")
            st.markdown(f"**Explanation:** {formula['explanation']}")
            st.markdown(f"**Source:** {formula['source']}")


def render_download_reports():
    st.title("Download Reports")
    st.markdown("Generate and download comprehensive PDF reports of your AI carbon analysis.")
    
    report_type = st.selectbox(
        "Select Report Type",
        ["Individual Impact Report", "Enterprise Report", "Industry Comparison Report"]
    )
    
    if report_type == "Individual Impact Report":
        st.subheader("Individual Impact Report")
        
        if st.session_state.last_impact:
            st.success("You have impact data from a recent calculation. Ready to generate report.")
            
            impact_data = st.session_state.last_impact
            equivalencies = impact_data.get('equivalencies', {})
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Model:** {impact_data.get('model', 'N/A')}")
                st.markdown(f"**Tokens:** {impact_data.get('tokens', 0):,}")
            with col2:
                st.markdown(f"**CO2:** {impact_data.get('co2_grams', 0):.6f} g")
                st.markdown(f"**Region:** {impact_data.get('region', 'N/A')}")
            
            if st.button("Generate Individual Report", type="primary"):
                with st.spinner("Generating report..."):
                    report_data = {
                        'report_type': 'Individual',
                        'period': 'Single Query',
                        'total_queries': 1,
                        'total_energy_kwh': impact_data.get('energy_wh', 0) / 1000,
                        'total_co2_kg': impact_data.get('co2_grams', 0) / 1000,
                        'primary_model': impact_data.get('model', 'N/A'),
                        'region': impact_data.get('region', 'Global'),
                        'trees_needed': equivalencies.get('trees', {}).get('count', 0)
                    }
                    
                    executive_summary = llm_explainer.generate_executive_summary(report_data)
                    recommendations = llm_explainer.generate_sustainability_recommendations(
                        {'primary_model': impact_data.get('model'), 'region': impact_data.get('region')},
                        context="individual"
                    )
                    
                    filepath = report_generator.generate_individual_report(
                        impact_data=impact_data,
                        equivalencies=equivalencies,
                        recommendations=recommendations,
                        executive_summary=executive_summary
                    )
                    
                    with open(filepath, "rb") as file:
                        st.download_button(
                            label="Download PDF Report",
                            data=file,
                            file_name=os.path.basename(filepath),
                            mime="application/pdf"
                        )
        else:
            st.info("No impact data available. Please use the Prompt Impact Calculator first to generate data for the report.")
    
    elif report_type == "Enterprise Report":
        st.subheader("Enterprise Report")
        
        if hasattr(st.session_state, 'enterprise_impact') and st.session_state.enterprise_impact:
            st.success("Enterprise data available. Ready to generate report.")
            
            if st.button("Generate Enterprise Report", type="primary"):
                with st.spinner("Generating enterprise report..."):
                    impact = st.session_state.enterprise_impact
                    offset_plan = st.session_state.enterprise_offset
                    comparison = st.session_state.enterprise_comparison
                    
                    calculator = EnterpriseCalculator()
                    checklist = calculator.generate_sustainability_checklist()
                    
                    report_data = {
                        'report_type': 'Enterprise',
                        'period': 'Annual',
                        'total_queries': impact['queries']['annual'],
                        'total_energy_kwh': impact['energy']['annual_kwh'],
                        'total_co2_kg': impact['co2']['annual_kg'],
                        'primary_model': impact['inputs']['model'],
                        'region': impact['inputs']['region'],
                        'trees_needed': offset_plan['tree_offset']['trees_needed']
                    }
                    
                    executive_summary = llm_explainer.generate_executive_summary(report_data)
                    
                    filepath = report_generator.generate_enterprise_report(
                        enterprise_data=impact,
                        model_comparison=comparison,
                        offset_plan=offset_plan,
                        executive_summary=executive_summary,
                        checklist=checklist
                    )
                    
                    with open(filepath, "rb") as file:
                        st.download_button(
                            label="Download Enterprise PDF Report",
                            data=file,
                            file_name=os.path.basename(filepath),
                            mime="application/pdf"
                        )
        else:
            st.info("No enterprise data available. Please use the Enterprise Simulator first to generate data for the report.")
    
    else:
        st.subheader("Industry Comparison Report")
        
        if st.button("Generate Industry Report", type="primary"):
            with st.spinner("Generating industry comparison report..."):
                companies = [
                    {**COMPANY_PROFILES[cid], 'company_id': cid}
                    for cid in get_all_companies()
                ]
                
                industry_totals = get_total_industry_emissions()
                
                report_data = {
                    'report_type': 'Industry Comparison',
                    'period': 'Annual Estimates',
                    'total_queries': industry_totals['total_daily_queries'] * 365,
                    'total_energy_kwh': industry_totals['total_annual_co2_tonnes'] * 1000 / 0.475,
                    'total_co2_kg': industry_totals['total_annual_co2_tonnes'] * 1000,
                    'primary_model': 'Various',
                    'region': 'Global',
                    'trees_needed': industry_totals['total_annual_co2_tonnes'] * 1000 / 21
                }
                
                executive_summary = llm_explainer.generate_executive_summary(report_data)
                
                filepath = report_generator.generate_company_comparison_report(
                    companies=companies,
                    industry_totals=industry_totals,
                    executive_summary=executive_summary
                )
                
                with open(filepath, "rb") as file:
                    st.download_button(
                        label="Download Industry PDF Report",
                        data=file,
                        file_name=os.path.basename(filepath),
                        mime="application/pdf"
                    )


if page == "Prompt Impact Calculator":
    render_prompt_calculator()
elif page == "Model Emission Comparison":
    render_model_comparison()
elif page == "Company Carbon Dashboards":
    render_company_dashboards()
elif page == "Enterprise Simulator":
    render_enterprise_simulator()
elif page == "Carbon Equivalency Visualizer":
    render_carbon_equivalency()
elif page == "Download Reports":
    render_download_reports()
