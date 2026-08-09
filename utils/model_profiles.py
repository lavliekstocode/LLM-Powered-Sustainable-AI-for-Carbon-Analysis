from typing import Dict, List, Optional

MODEL_PROFILES: Dict[str, Dict] = {
    'gpt-3.5-turbo': {
        'name': 'GPT-3.5 Turbo',
        'company': 'OpenAI',
        'parameters': '175B (distilled)',
        'energy_per_token_wh': 0.0001,
        'co2_per_million_tokens_g': 47.5,
        'efficiency_rating': 'A',
        'training_co2_tonnes': 552,
        'inference_co2_per_day_kg': 45,
        'hardware': 'NVIDIA A100 40GB',
        'tokens_per_second': 90,
        'context_window': 16385,
        'release_date': '2022-11',
        'notes': 'Optimized for speed and cost efficiency. Uses distillation from GPT-4.',
    },
    'gpt-4': {
        'name': 'GPT-4',
        'company': 'OpenAI',
        'parameters': '1.76T (MoE)',
        'energy_per_token_wh': 0.00045,
        'co2_per_million_tokens_g': 213.75,
        'efficiency_rating': 'B',
        'training_co2_tonnes': 8400,
        'inference_co2_per_day_kg': 380,
        'hardware': 'NVIDIA A100 80GB / H100',
        'tokens_per_second': 25,
        'context_window': 8192,
        'release_date': '2023-03',
        'notes': 'Mixture of Experts architecture. Significantly more capable but energy-intensive.',
    },
    'gpt-4-turbo': {
        'name': 'GPT-4 Turbo',
        'company': 'OpenAI',
        'parameters': '1.76T (MoE, optimized)',
        'energy_per_token_wh': 0.00035,
        'co2_per_million_tokens_g': 166.25,
        'efficiency_rating': 'A',
        'training_co2_tonnes': 8400,
        'inference_co2_per_day_kg': 290,
        'hardware': 'NVIDIA H100',
        'tokens_per_second': 40,
        'context_window': 128000,
        'release_date': '2023-11',
        'notes': 'Optimized inference with larger context. Better price-performance ratio.',
    },
    'gpt-5': {
        'name': 'GPT-5',
        'company': 'OpenAI',
        'parameters': '~2T+ (estimated)',
        'energy_per_token_wh': 0.0005,
        'co2_per_million_tokens_g': 237.5,
        'efficiency_rating': 'B',
        'training_co2_tonnes': 15000,
        'inference_co2_per_day_kg': 500,
        'hardware': 'NVIDIA H100 / H200',
        'tokens_per_second': 35,
        'context_window': 256000,
        'release_date': '2025-08',
        'notes': 'Latest flagship model. Enhanced reasoning capabilities with higher compute requirements.',
    },
    'claude-3.5-sonnet': {
        'name': 'Claude 3.5 Sonnet',
        'company': 'Anthropic',
        'parameters': '~175B (estimated)',
        'energy_per_token_wh': 0.00025,
        'co2_per_million_tokens_g': 118.75,
        'efficiency_rating': 'A+',
        'training_co2_tonnes': 1800,
        'inference_co2_per_day_kg': 120,
        'hardware': 'Google TPU v4 / AWS Trainium',
        'tokens_per_second': 50,
        'context_window': 200000,
        'release_date': '2024-06',
        'notes': 'Highly efficient model using Constitutional AI. Excellent performance-to-energy ratio.',
    },
    'claude-3.7-sonnet': {
        'name': 'Claude 3.7 Sonnet',
        'company': 'Anthropic',
        'parameters': '~200B (estimated)',
        'energy_per_token_wh': 0.00028,
        'co2_per_million_tokens_g': 133.0,
        'efficiency_rating': 'A+',
        'training_co2_tonnes': 2200,
        'inference_co2_per_day_kg': 140,
        'hardware': 'Google TPU v5e / AWS Trainium2',
        'tokens_per_second': 55,
        'context_window': 200000,
        'release_date': '2025-02',
        'notes': 'Latest Claude iteration with improved reasoning. Maintains excellent efficiency.',
    },
    'gemini-ultra': {
        'name': 'Gemini Ultra',
        'company': 'Google DeepMind',
        'parameters': '~1.5T (estimated)',
        'energy_per_token_wh': 0.0004,
        'co2_per_million_tokens_g': 190.0,
        'efficiency_rating': 'A',
        'training_co2_tonnes': 6500,
        'inference_co2_per_day_kg': 280,
        'hardware': 'Google TPU v5p',
        'tokens_per_second': 45,
        'context_window': 1000000,
        'release_date': '2023-12',
        'notes': 'Multimodal flagship. Uses custom TPU hardware for better energy efficiency.',
    },
    'gemini-pro': {
        'name': 'Gemini Pro',
        'company': 'Google DeepMind',
        'parameters': '~500B (estimated)',
        'energy_per_token_wh': 0.00018,
        'co2_per_million_tokens_g': 85.5,
        'efficiency_rating': 'A+',
        'training_co2_tonnes': 2800,
        'inference_co2_per_day_kg': 95,
        'hardware': 'Google TPU v4',
        'tokens_per_second': 65,
        'context_window': 128000,
        'release_date': '2023-12',
        'notes': 'Balanced model for most tasks. Excellent efficiency on TPU infrastructure.',
    },
    'llama-3': {
        'name': 'Meta LLaMA 3',
        'company': 'Meta AI',
        'parameters': '70B / 405B',
        'energy_per_token_wh': 0.00022,
        'co2_per_million_tokens_g': 104.5,
        'efficiency_rating': 'A+',
        'training_co2_tonnes': 1500,
        'inference_co2_per_day_kg': 85,
        'hardware': 'NVIDIA H100 (Meta Grand Teton)',
        'tokens_per_second': 70,
        'context_window': 128000,
        'release_date': '2024-04',
        'notes': 'Open-source model. Can be self-hosted for reduced cloud emissions.',
    },
    'mistral-large': {
        'name': 'Mistral Large',
        'company': 'Mistral AI',
        'parameters': '~123B (estimated)',
        'energy_per_token_wh': 0.00020,
        'co2_per_million_tokens_g': 95.0,
        'efficiency_rating': 'A+',
        'training_co2_tonnes': 980,
        'inference_co2_per_day_kg': 70,
        'hardware': 'NVIDIA H100',
        'tokens_per_second': 60,
        'context_window': 128000,
        'release_date': '2024-02',
        'notes': 'European-trained model. Benefits from France\'s low-carbon electricity grid.',
    },
    'falcon': {
        'name': 'Falcon 180B',
        'company': 'Technology Innovation Institute',
        'parameters': '180B',
        'energy_per_token_wh': 0.00032,
        'co2_per_million_tokens_g': 152.0,
        'efficiency_rating': 'B',
        'training_co2_tonnes': 2100,
        'inference_co2_per_day_kg': 145,
        'hardware': 'NVIDIA A100 / H100',
        'tokens_per_second': 35,
        'context_window': 2048,
        'release_date': '2023-09',
        'notes': 'Open-source large model. Trained primarily on RefinedWeb dataset.',
    },
}


def get_model_profile(model_id: str) -> Optional[Dict]:
    """Get the profile for a specific model."""
    return MODEL_PROFILES.get(model_id)


def get_all_models() -> List[str]:
    """Get list of all available model IDs."""
    return list(MODEL_PROFILES.keys())


def get_models_by_company(company: str) -> List[str]:
    """Get all models from a specific company."""
    return [
        model_id for model_id, profile in MODEL_PROFILES.items()
        if profile['company'].lower() == company.lower()
    ]


def get_models_by_efficiency(rating: str) -> List[str]:
    """Get all models with a specific efficiency rating."""
    return [
        model_id for model_id, profile in MODEL_PROFILES.items()
        if profile['efficiency_rating'] == rating
    ]


def compare_models(model_ids: List[str]) -> List[Dict]:
    """Get comparison data for multiple models."""
    return [
        {
            'model_id': model_id,
            **MODEL_PROFILES[model_id]
        }
        for model_id in model_ids
        if model_id in MODEL_PROFILES
    ]


def get_efficiency_ranking() -> List[Dict]:
    """Get models ranked by energy efficiency."""
    models = [
        {'model_id': model_id, **profile}
        for model_id, profile in MODEL_PROFILES.items()
    ]
    return sorted(models, key=lambda x: x['energy_per_token_wh'])
