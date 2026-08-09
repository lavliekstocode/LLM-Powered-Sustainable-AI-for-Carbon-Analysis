from typing import Dict, List, Optional

COMPANY_PROFILES: Dict[str, Dict] = {
    'openai': {
        'name': 'OpenAI',
        'headquarters': 'San Francisco, USA',
        'founded': 2015,
        'estimated_annual_inference_co2_tonnes': 95000,
        'estimated_training_co2_tonnes': 25000,
        'total_estimated_co2_tonnes': 120000,
        'growth_rate_percent': 35,
        'carbon_intensity_score': 6.5,
        'renewable_energy_percent': 45,
        'sustainability_grade': 'B',
        'primary_models': ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo', 'gpt-5'],
        'data_centers': ['Azure (Multiple Regions)', 'Custom Supercomputers'],
        'hardware': 'NVIDIA A100/H100, Custom ASICs',
        'pue_estimate': 1.15,
        'daily_queries_estimate': 200000000,
        'notes': 'Largest commercial LLM provider. Heavy investment in compute infrastructure. Partner with Microsoft Azure for carbon credits.',
        'sustainability_initiatives': [
            'Carbon credit purchasing',
            'Azure renewable energy commitments',
            'Efficiency improvements in inference',
            'Research into efficient architectures',
        ],
    },
    'google_deepmind': {
        'name': 'Google DeepMind',
        'headquarters': 'London, UK / Mountain View, USA',
        'founded': 2010,
        'estimated_annual_inference_co2_tonnes': 78000,
        'estimated_training_co2_tonnes': 18000,
        'total_estimated_co2_tonnes': 96000,
        'growth_rate_percent': 28,
        'carbon_intensity_score': 4.8,
        'renewable_energy_percent': 92,
        'sustainability_grade': 'A',
        'primary_models': ['gemini-ultra', 'gemini-pro'],
        'data_centers': ['Google Cloud (Global)'],
        'hardware': 'Custom TPU v4/v5, Some NVIDIA GPUs',
        'pue_estimate': 1.10,
        'daily_queries_estimate': 150000000,
        'notes': 'Benefits from Google\'s carbon-neutral cloud. TPU architecture is more energy-efficient than GPUs for inference.',
        'sustainability_initiatives': [
            'Carbon neutral since 2007',
            '100% renewable energy matching',
            'Custom TPU hardware for efficiency',
            'AI for climate research',
            'Carbon-intelligent computing',
        ],
    },
    'meta_ai': {
        'name': 'Meta AI',
        'headquarters': 'Menlo Park, USA',
        'founded': 2013,
        'estimated_annual_inference_co2_tonnes': 45000,
        'estimated_training_co2_tonnes': 12000,
        'total_estimated_co2_tonnes': 57000,
        'growth_rate_percent': 42,
        'carbon_intensity_score': 5.2,
        'renewable_energy_percent': 78,
        'sustainability_grade': 'A-',
        'primary_models': ['llama-3'],
        'data_centers': ['Meta Data Centers (Global)'],
        'hardware': 'NVIDIA H100 (Grand Teton Clusters)',
        'pue_estimate': 1.08,
        'daily_queries_estimate': 100000000,
        'notes': 'Open-source approach reduces industry-wide duplication of training. Very efficient data centers.',
        'sustainability_initiatives': [
            'Open-source models reduce retraining',
            'Net zero emissions goal by 2030',
            'Water restoration programs',
            'Efficient data center design',
        ],
    },
    'anthropic': {
        'name': 'Anthropic',
        'headquarters': 'San Francisco, USA',
        'founded': 2021,
        'estimated_annual_inference_co2_tonnes': 28000,
        'estimated_training_co2_tonnes': 8000,
        'total_estimated_co2_tonnes': 36000,
        'growth_rate_percent': 65,
        'carbon_intensity_score': 4.2,
        'renewable_energy_percent': 85,
        'sustainability_grade': 'A',
        'primary_models': ['claude-3.5-sonnet', 'claude-3.7-sonnet'],
        'data_centers': ['Google Cloud', 'AWS'],
        'hardware': 'Google TPU v4/v5e, AWS Trainium',
        'pue_estimate': 1.12,
        'daily_queries_estimate': 50000000,
        'notes': 'Focus on AI safety and efficiency. Constitutional AI approach reduces need for extensive fine-tuning.',
        'sustainability_initiatives': [
            'Cloud provider renewable commitments',
            'Efficient Constitutional AI training',
            'TPU usage for lower energy inference',
            'Research into efficient alignment',
        ],
    },
    'mistral_ai': {
        'name': 'Mistral AI',
        'headquarters': 'Paris, France',
        'founded': 2023,
        'estimated_annual_inference_co2_tonnes': 8500,
        'estimated_training_co2_tonnes': 2500,
        'total_estimated_co2_tonnes': 11000,
        'growth_rate_percent': 120,
        'carbon_intensity_score': 2.8,
        'renewable_energy_percent': 95,
        'sustainability_grade': 'A+',
        'primary_models': ['mistral-large'],
        'data_centers': ['Scaleway (France)', 'European Cloud Providers'],
        'hardware': 'NVIDIA H100',
        'pue_estimate': 1.18,
        'daily_queries_estimate': 15000000,
        'notes': 'Benefits significantly from France\'s nuclear-powered electricity grid (very low carbon). European focus.',
        'sustainability_initiatives': [
            'French nuclear grid (56g CO2/kWh)',
            'Efficient architecture design',
            'Open-weight models',
            'European data sovereignty',
        ],
    },
    'cohere': {
        'name': 'Cohere',
        'headquarters': 'Toronto, Canada',
        'founded': 2019,
        'estimated_annual_inference_co2_tonnes': 12000,
        'estimated_training_co2_tonnes': 3500,
        'total_estimated_co2_tonnes': 15500,
        'growth_rate_percent': 55,
        'carbon_intensity_score': 3.5,
        'renewable_energy_percent': 88,
        'sustainability_grade': 'A',
        'primary_models': ['Command R+', 'Embed'],
        'data_centers': ['Google Cloud', 'AWS', 'Oracle Cloud'],
        'hardware': 'NVIDIA A100/H100, Google TPU',
        'pue_estimate': 1.15,
        'daily_queries_estimate': 25000000,
        'notes': 'Enterprise-focused with emphasis on efficiency. Canadian operations benefit from hydroelectric power.',
        'sustainability_initiatives': [
            'Canadian hydroelectric grid',
            'Multi-cloud efficiency optimization',
            'Enterprise deployment optimization',
            'Efficient embedding models',
        ],
    },
    'huggingface': {
        'name': 'HuggingFace',
        'headquarters': 'New York, USA',
        'founded': 2016,
        'estimated_annual_inference_co2_tonnes': 5500,
        'estimated_training_co2_tonnes': 4500,
        'total_estimated_co2_tonnes': 10000,
        'growth_rate_percent': 45,
        'carbon_intensity_score': 4.5,
        'renewable_energy_percent': 72,
        'sustainability_grade': 'A-',
        'primary_models': ['Community Models', 'StarCoder', 'BLOOM'],
        'data_centers': ['AWS', 'Various Cloud Providers'],
        'hardware': 'Various (User-defined)',
        'pue_estimate': 1.25,
        'daily_queries_estimate': 80000000,
        'notes': 'Platform model - emissions vary widely based on community model usage. Promotes model sharing to reduce retraining.',
        'sustainability_initiatives': [
            'Model Hub reduces retraining',
            'Carbon emissions tracking tools',
            'Efficient model cards',
            'Green AI research promotion',
        ],
    },
}


def get_company_profile(company_id: str) -> Optional[Dict]:
    """Get the profile for a specific company."""
    return COMPANY_PROFILES.get(company_id.lower().replace(' ', '_'))


def get_all_companies() -> List[str]:
    """Get list of all available company IDs."""
    return list(COMPANY_PROFILES.keys())


def get_company_display_names() -> Dict[str, str]:
    """Get mapping of company IDs to display names."""
    return {
        company_id: profile['name']
        for company_id, profile in COMPANY_PROFILES.items()
    }


def get_companies_by_grade(grade: str) -> List[str]:
    """Get all companies with a specific sustainability grade."""
    return [
        company_id for company_id, profile in COMPANY_PROFILES.items()
        if profile['sustainability_grade'] == grade
    ]


def compare_companies(company_ids: List[str]) -> List[Dict]:
    """Get comparison data for multiple companies."""
    return [
        {
            'company_id': company_id,
            **COMPANY_PROFILES[company_id]
        }
        for company_id in company_ids
        if company_id in COMPANY_PROFILES
    ]


def get_sustainability_ranking() -> List[Dict]:
    """Get companies ranked by sustainability (carbon intensity score, lower is better)."""
    companies = [
        {'company_id': company_id, **profile}
        for company_id, profile in COMPANY_PROFILES.items()
    ]
    return sorted(companies, key=lambda x: x['carbon_intensity_score'])


def get_total_industry_emissions() -> Dict:
    """Calculate total estimated industry emissions."""
    total_inference = sum(p['estimated_annual_inference_co2_tonnes'] for p in COMPANY_PROFILES.values())
    total_training = sum(p['estimated_training_co2_tonnes'] for p in COMPANY_PROFILES.values())
    total_queries = sum(p['daily_queries_estimate'] for p in COMPANY_PROFILES.values())
    
    return {
        'total_annual_inference_co2_tonnes': total_inference,
        'total_annual_training_co2_tonnes': total_training,
        'total_annual_co2_tonnes': total_inference + total_training,
        'total_daily_queries': total_queries,
        'total_annual_queries': total_queries * 365,
        'avg_co2_per_query_grams': (total_inference * 1000000) / (total_queries * 365),
    }
