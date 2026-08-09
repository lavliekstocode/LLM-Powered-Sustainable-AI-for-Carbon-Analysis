# SustainAI - AI Emission Estimator & LLM Carbon Intelligence Dashboard

SustainAI is a comprehensive platform for calculating and understanding the environmental impact of AI model usage. It provides tools for individuals, enterprises, and industry analysis.

## Overview

SustainAI helps you:
- Calculate the carbon footprint of your AI queries
- Compare energy efficiency across major AI models
- Analyze company-level sustainability metrics
- Generate enterprise carbon reduction plans
- Understand emissions through real-world equivalencies
- Get AI-powered sustainability recommendations
- Generate professional PDF reports

## Features

### 1. Prompt Impact Calculator
Calculate real-time energy consumption and CO2 emissions for any AI prompt.
- Token counting (using tiktoken for OpenAI models)
- Energy calculation based on model profiles
- Regional grid carbon intensity factors
- Real-world equivalency conversions

### 2. Model Emission Comparison
Compare environmental footprints across 11 major AI models:
- GPT-3.5 Turbo, GPT-4, GPT-4 Turbo, GPT-5
- Claude 3.5 Sonnet, Claude 3.7 Sonnet
- Gemini Ultra, Gemini Pro
- Meta LLaMA 3
- Mistral Large
- Falcon 180B

Each profile includes:
- Energy per token (Wh)
- CO2 per million tokens
- Efficiency rating (A+ to C)
- Training emissions estimate
- Hardware specifications

### 3. Company Carbon Dashboards
Track environmental metrics for major AI companies:
- OpenAI
- Google DeepMind
- Meta AI
- Anthropic
- Mistral AI
- Cohere
- HuggingFace

Metrics include:
- Annual inference CO2 (tonnes)
- Training emissions
- Growth rate
- Renewable energy percentage
- Sustainability grade

### 4. Enterprise AI Usage Simulator
Calculate your organization's AI carbon footprint:
- Input: employees, queries/day, model, region
- Output: annual energy, CO2, and equivalencies
- Carbon offset recommendations
- Model comparison for your use case
- Sustainability checklist

### 5. Carbon Equivalency Visualizer
Understand carbon emissions through real-world comparisons:
- Trees needed for absorption
- Car driving distance
- Flight equivalents
- Household electricity hours
- Smartphone charges
- Streaming video hours

### 6. PDF Report Generator
Generate professional reports:
- Individual impact reports
- Enterprise carbon reports
- Industry comparison reports

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SustainAI Dashboard                          │
│                      (Streamlit UI)                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Prompt     │  │    Model     │  │   Company    │          │
│  │  Calculator  │  │  Comparison  │  │  Dashboards  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Enterprise  │  │   Carbon     │  │   Download   │          │
│  │  Simulator   │  │ Equivalency  │  │    Reports   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                       Utility Layer                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  token_estimator │ energy_model │ carbon_equivalency    │   │
│  │  model_profiles  │ company_profiles │ enterprise_calc   │   │
│  │  llm_explainer   │ report_generator                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                    External Services                            │
│  ┌──────────────┐  ┌──────────────┐                            │
│  │   OpenAI     │  │    PDF       │                            │
│  │    API       │  │  Generation  │                            │
│  └──────────────┘  └──────────────┘                            │
└─────────────────────────────────────────────────────────────────┘
```

## Scientific Formulas

### Energy Calculation
```
Energy (Wh) = Tokens × Energy per Token (Wh) × PUE Factor
```

### CO2 Calculation
```
CO2 (grams) = Energy (kWh) × Grid Carbon Intensity (g CO2/kWh)
```

### Key Conversion Factors
| Metric | Value | Source |
|--------|-------|--------|
| Tree CO2 absorption | 21 kg/year | EPA, IPCC |
| Car emissions | 192 g CO2/km | EU average |
| Flight emissions | 255 g CO2/passenger-km | IATA |
| Global grid average | 475 g CO2/kWh | IEA |
| Smartphone charge | 8 g CO2 | Berkeley Lab |
| LPG combustion | 3.0 kg CO2/kg | IPCC |

### Regional Grid Factors (g CO2/kWh)
| Region | Factor |
|--------|--------|
| Global Average | 475 |
| France | 56 |
| Sweden | 45 |
| Norway | 28 |
| USA Average | 386 |
| China | 555 |
| India | 708 |

## Installation

### Requirements
- Python 3.11+
- Dependencies listed in `pyproject.toml`
- OpenAI API key (optional, for AI-generated explanations and recommendations)

### Setup
1. Clone the repository
2. Install the project and its dependencies:
   ```bash
   pip install -e .
   ```
3. Optionally set `OPENAI_API_KEY` in your environment for AI-generated explanations and recommendations.
4. Run the dashboard:
   ```bash
   streamlit run app.py --server.port 5000
   ```

## Project Structure

```
sustainai/
├── app.py                      # Main Streamlit application
├── pyproject.toml               # Python project metadata and dependencies
├── README.md                   # This file
├── utils/
│   ├── __init__.py
│   ├── token_estimator.py      # Token counting utilities
│   ├── energy_model.py         # Energy & CO2 calculations
│   ├── model_profiles.py       # AI model specifications
│   ├── company_profiles.py     # Company carbon data
│   ├── enterprise_calculator.py # Enterprise calculations
│   ├── carbon_equivalency.py   # Real-world equivalencies
│   ├── llm_explainer.py        # OpenAI-powered explanations
│   └── report_generator.py     # PDF report generation
└── reports/                    # Locally generated PDF reports (not committed)
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| OPENAI_API_KEY | No* | OpenAI API key for AI-generated explanations and recommendations |

*The application works without an API key and uses built-in fallback explanations and recommendations.

## Data Sources & Methodology

### Model Profiles
Energy consumption estimates are based on:
- Published research papers on LLM energy consumption
- Hardware specifications (TDP, efficiency ratings)
- Tokens per second benchmarks
- Data center PUE factors

### Company Data
Company emissions are estimated from:
- Public sustainability reports
- Academic research on AI compute
- Industry analysis and estimates
- Data center efficiency reports

### Limitations
- All values are estimates based on public information
- Actual emissions may vary based on specific deployments
- Training emissions are difficult to measure precisely
- Company data is based on best available public estimates

## Contributing

Contributions are welcome! Please focus on:
- Improving emission estimate accuracy
- Adding new model profiles
- Updating company sustainability data
- Enhancing visualization features

## License

MIT License. See [LICENSE](LICENSE) for details.

## Disclaimer

This tool provides estimates based on public data and scientific approximations. Actual emissions may vary. Use responsibly for educational and planning purposes.
