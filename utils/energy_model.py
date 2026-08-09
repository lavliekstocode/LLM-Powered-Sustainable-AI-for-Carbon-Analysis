from typing import Dict, Optional
from utils.model_profiles import get_model_profile


class EnergyModel:
    """
    Energy consumption model for AI inference.
    
    Scientific basis:
    - GPU power consumption varies by model (A100: ~400W, H100: ~700W, TPU v4: ~200W)
    - Tokens processed per second varies by model size and hardware
    - Energy per token = (GPU Power × Time per Token) / Efficiency Factor
    
    Key formulas:
    - Energy (Wh) = Tokens × Energy per Token (Wh/token)
    - CO₂ (g) = Energy (kWh) × Grid Carbon Intensity (g CO₂/kWh)
    """
    
    REGIONAL_GRID_FACTORS = {
        'global_average': 475,
        'usa_average': 386,
        'usa_california': 210,
        'usa_texas': 396,
        'usa_new_york': 230,
        'europe_average': 295,
        'uk': 233,
        'germany': 385,
        'france': 56,
        'sweden': 45,
        'norway': 28,
        'china': 555,
        'india': 708,
        'japan': 471,
        'australia': 656,
        'brazil': 74,
        'canada': 120,
        'south_africa': 928,
        'singapore': 408,
        'south_korea': 459,
    }
    
    PUE_FACTORS = {
        'hyperscale': 1.1,
        'efficient': 1.2,
        'average': 1.4,
        'legacy': 1.8,
    }
    
    def __init__(self, region: str = 'global_average', data_center_type: str = 'hyperscale'):
        """
        Initialize the energy model.
        
        Args:
            region: Geographic region for grid carbon intensity
            data_center_type: Type of data center for PUE factor
        """
        self.region = region
        self.data_center_type = data_center_type
        self.grid_factor = self.REGIONAL_GRID_FACTORS.get(region, 475)
        self.pue = self.PUE_FACTORS.get(data_center_type, 1.2)
    
    def calculate_energy(self, tokens: int, model: str) -> Dict:
        """
        Calculate energy consumption for a given number of tokens.
        
        Formula: Energy (Wh) = Tokens × Energy per Token × PUE
        
        Args:
            tokens: Number of tokens processed
            model: Model identifier
            
        Returns:
            Dictionary with energy metrics
        """
        profile = get_model_profile(model)
        if not profile:
            energy_per_token = 0.0003
        else:
            energy_per_token = profile['energy_per_token_wh']
        
        base_energy_wh = tokens * energy_per_token
        total_energy_wh = base_energy_wh * self.pue
        
        return {
            'tokens': tokens,
            'model': model,
            'energy_per_token_wh': energy_per_token,
            'base_energy_wh': round(base_energy_wh, 6),
            'pue_factor': self.pue,
            'total_energy_wh': round(total_energy_wh, 6),
            'total_energy_kwh': round(total_energy_wh / 1000, 9),
        }
    
    def calculate_co2(self, energy_kwh: float, region: Optional[str] = None) -> Dict:
        """
        Calculate CO₂ emissions from energy consumption.
        
        Formula: CO₂ (g) = Energy (kWh) × Grid Carbon Intensity (g CO₂/kWh)
        
        Args:
            energy_kwh: Energy consumption in kWh
            region: Optional region override
            
        Returns:
            Dictionary with CO₂ metrics
        """
        grid_factor = self.REGIONAL_GRID_FACTORS.get(region, self.grid_factor) if region else self.grid_factor
        
        co2_grams = energy_kwh * grid_factor
        co2_kg = co2_grams / 1000
        
        return {
            'energy_kwh': energy_kwh,
            'grid_factor_g_per_kwh': grid_factor,
            'region': region or self.region,
            'co2_grams': round(co2_grams, 6),
            'co2_kg': round(co2_kg, 9),
            'co2_tonnes': round(co2_kg / 1000, 12),
        }
    
    def calculate_full_impact(self, tokens: int, model: str, region: Optional[str] = None) -> Dict:
        """
        Calculate complete environmental impact for a query.
        
        Args:
            tokens: Number of tokens processed
            model: Model identifier
            region: Optional region for grid factor
            
        Returns:
            Comprehensive impact dictionary
        """
        energy = self.calculate_energy(tokens, model)
        co2 = self.calculate_co2(energy['total_energy_kwh'], region)
        
        profile = get_model_profile(model)
        
        return {
            'tokens': tokens,
            'model': model,
            'model_efficiency_rating': profile.get('efficiency_rating', 'N/A') if profile else 'N/A',
            'energy': energy,
            'co2': co2,
            'summary': {
                'total_energy_wh': energy['total_energy_wh'],
                'total_co2_grams': co2['co2_grams'],
                'region': co2['region'],
            }
        }
    
    @classmethod
    def get_available_regions(cls) -> Dict[str, int]:
        """Get all available regions and their grid factors."""
        return cls.REGIONAL_GRID_FACTORS.copy()
    
    @classmethod
    def get_region_display_names(cls) -> Dict[str, str]:
        """Get human-readable names for regions."""
        return {
            'global_average': 'Global Average',
            'usa_average': 'USA (Average)',
            'usa_california': 'USA - California',
            'usa_texas': 'USA - Texas',
            'usa_new_york': 'USA - New York',
            'europe_average': 'Europe (Average)',
            'uk': 'United Kingdom',
            'germany': 'Germany',
            'france': 'France',
            'sweden': 'Sweden',
            'norway': 'Norway',
            'china': 'China',
            'india': 'India',
            'japan': 'Japan',
            'australia': 'Australia',
            'brazil': 'Brazil',
            'canada': 'Canada',
            'south_africa': 'South Africa',
            'singapore': 'Singapore',
            'south_korea': 'South Korea',
        }
