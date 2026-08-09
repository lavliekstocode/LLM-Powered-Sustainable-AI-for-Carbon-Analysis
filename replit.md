# SustainAI - AI Emission Estimator & LLM Carbon Intelligence Dashboard

## Overview
SustainAI is a comprehensive Streamlit-based dashboard for calculating and understanding the environmental impact of AI model usage. It provides tools for individuals, enterprises, and industry analysis with real-world carbon equivalencies.

## Current State
- **Status**: Complete MVP with all 6 dashboard pages functional
- **Framework**: Streamlit (Python)
- **Port**: 5000

## Project Architecture

```
sustainai/
├── app.py                      # Main Streamlit multi-page application
├── README.md                   # Project documentation
├── utils/
│   ├── __init__.py            # Package exports
│   ├── token_estimator.py     # Token counting (tiktoken for OpenAI)
│   ├── energy_model.py        # Energy & CO2 calculations with regional factors
│   ├── model_profiles.py      # 11 AI model specifications
│   ├── company_profiles.py    # 7 AI company carbon data
│   ├── enterprise_calculator.py # Enterprise-level calculations
│   ├── carbon_equivalency.py  # Real-world carbon equivalencies
│   ├── llm_explainer.py       # OpenAI GPT-5 powered explanations
│   └── report_generator.py    # PDF report generation (FPDF2)
└── reports/                   # Locally generated PDF reports (not committed)
```

## Key Features

### 6 Dashboard Pages:
1. **Prompt Impact Calculator** - Real-time energy & CO2 for any prompt
2. **Model Emission Comparison** - Compare 11 AI models by efficiency
3. **Company Carbon Dashboards** - Track 7 major AI companies
4. **Enterprise Simulator** - Calculate organizational AI footprint
5. **Carbon Equivalency Visualizer** - Real-world comparisons
6. **Download Reports** - PDF generation

### Scientific Formulas:
- Energy (Wh) = Tokens × Energy per Token × PUE Factor
- CO2 (g) = Energy (kWh) × Grid Carbon Intensity (g CO2/kWh)

### Regional Grid Factors:
Supports 20+ regions including USA, Europe, Asia with accurate g CO2/kWh values.

## Dependencies
- streamlit >= 1.51.0
- openai >= 1.0.0 (for AI explanations, optional)
- plotly >= 5.18.0 (interactive charts)
- pandas >= 2.0.0
- numpy >= 1.24.0
- fpdf2 >= 2.7.0 (PDF generation)
- tiktoken >= 0.5.0 (token counting)
- pillow >= 10.0.0

## Environment Variables
- `OPENAI_API_KEY` (optional) - Enables AI-generated explanations and recommendations

## Running the Application
```bash
streamlit run app.py --server.port 5000
```

## Recent Changes
- 2024-12: Initial implementation with all pages
- All utility modules created with scientific formulas
- PDF report generation functional
- OpenAI GPT-5 integration for LLM explanations in reports
- 2024-12: Removed AI Sustainability Chatbot page per user request

## User Preferences
- Focus on scientific accuracy for carbon calculations
- Use real-world equivalencies for better understanding
- Clean, data-centric Streamlit UI
