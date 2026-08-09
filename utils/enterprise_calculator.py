from typing import Dict, List, Optional
from utils.energy_model import EnergyModel
from utils.model_profiles import get_model_profile
from utils.carbon_equivalency import CarbonEquivalency


class EnterpriseCalculator:
    """
    Enterprise-level AI carbon footprint calculator.
    
    Calculates annual emissions based on:
    - Number of employees using AI
    - Average queries per person per day
    - Model selection
    - Regional grid factors
    - Working days per year
    """
    
    WORKING_DAYS_PER_YEAR = 250
    AVG_TOKENS_PER_QUERY = 500
    
    def __init__(self, region: str = 'global_average'):
        """
        Initialize enterprise calculator.
        
        Args:
            region: Geographic region for grid carbon intensity
        """
        self.energy_model = EnergyModel(region=region)
        self.carbon_equiv = CarbonEquivalency()
        self.region = region
    
    def calculate_annual_impact(
        self,
        employees: int,
        queries_per_person_per_day: float,
        model: str,
        avg_tokens_per_query: int = 500,
        working_days: int = 250
    ) -> Dict:
        """
        Calculate annual environmental impact for an enterprise.
        
        Args:
            employees: Number of employees using AI
            queries_per_person_per_day: Average AI queries per person per day
            model: Model being used
            avg_tokens_per_query: Average tokens per query (prompt + response)
            working_days: Working days per year
            
        Returns:
            Comprehensive impact dictionary
        """
        daily_queries = employees * queries_per_person_per_day
        annual_queries = daily_queries * working_days
        
        total_annual_tokens = annual_queries * avg_tokens_per_query
        
        daily_tokens = daily_queries * avg_tokens_per_query
        daily_impact = self.energy_model.calculate_full_impact(int(daily_tokens), model)
        
        annual_energy_wh = daily_impact['energy']['total_energy_wh'] * working_days
        annual_energy_kwh = annual_energy_wh / 1000
        
        annual_co2 = self.energy_model.calculate_co2(annual_energy_kwh)
        
        equivalencies = self.carbon_equiv.calculate_all_equivalencies(annual_co2['co2_kg'])
        
        return {
            'inputs': {
                'employees': employees,
                'queries_per_person_per_day': queries_per_person_per_day,
                'model': model,
                'avg_tokens_per_query': avg_tokens_per_query,
                'working_days': working_days,
                'region': self.region,
            },
            'queries': {
                'daily': round(daily_queries),
                'weekly': round(daily_queries * 5),
                'monthly': round(daily_queries * 21.67),
                'annual': round(annual_queries),
            },
            'tokens': {
                'daily': round(daily_tokens),
                'annual': round(total_annual_tokens),
            },
            'energy': {
                'daily_wh': round(daily_impact['energy']['total_energy_wh'], 4),
                'daily_kwh': round(daily_impact['energy']['total_energy_wh'] / 1000, 6),
                'annual_wh': round(annual_energy_wh, 2),
                'annual_kwh': round(annual_energy_kwh, 4),
                'annual_mwh': round(annual_energy_kwh / 1000, 6),
            },
            'co2': {
                'daily_grams': round(daily_impact['co2']['co2_grams'], 4),
                'daily_kg': round(daily_impact['co2']['co2_grams'] / 1000, 6),
                'annual_grams': round(annual_co2['co2_grams'], 2),
                'annual_kg': round(annual_co2['co2_kg'], 4),
                'annual_tonnes': round(annual_co2['co2_kg'] / 1000, 6),
            },
            'equivalencies': equivalencies,
            'per_employee': {
                'annual_queries': round(queries_per_person_per_day * working_days),
                'annual_tokens': round(queries_per_person_per_day * working_days * avg_tokens_per_query),
                'annual_co2_kg': round(annual_co2['co2_kg'] / employees, 6) if employees > 0 else 0,
            },
        }
    
    def generate_offset_plan(self, annual_co2_kg: float) -> Dict:
        """
        Generate a carbon offset and sustainability plan.
        
        Args:
            annual_co2_kg: Annual CO2 emissions in kg
            
        Returns:
            Offset plan with recommendations
        """
        annual_co2_tonnes = annual_co2_kg / 1000
        
        trees_needed = self.carbon_equiv.co2_to_trees(annual_co2_kg)
        
        cost_per_tonne_low = 15
        cost_per_tonne_high = 50
        
        return {
            'annual_co2_tonnes': round(annual_co2_tonnes, 4),
            'tree_offset': {
                'trees_needed': round(trees_needed),
                'area_hectares': round(trees_needed / 1000, 2),
                'description': f"Plant {round(trees_needed):,} trees to offset annual AI emissions",
            },
            'carbon_credits': {
                'credits_needed': round(annual_co2_tonnes, 2),
                'cost_low_usd': round(annual_co2_tonnes * cost_per_tonne_low, 2),
                'cost_high_usd': round(annual_co2_tonnes * cost_per_tonne_high, 2),
                'description': f"Purchase {round(annual_co2_tonnes, 2)} carbon credits",
            },
            'renewable_energy': {
                'kwh_to_offset': round(annual_co2_kg / 0.475, 2),
                'solar_panels_equivalent': round(annual_co2_kg / 0.475 / 1500, 1),
                'description': "Switch to renewable energy sources for equivalent offset",
            },
            'recommendations': self._generate_recommendations(annual_co2_tonnes),
        }
    
    def _generate_recommendations(self, annual_co2_tonnes: float) -> List[Dict]:
        """Generate sustainability recommendations based on emission level."""
        recommendations = [
            {
                'priority': 'High',
                'category': 'Model Selection',
                'action': 'Use more efficient models for routine tasks',
                'potential_reduction': '30-50%',
                'description': 'Reserve large models (GPT-4, GPT-5) for complex tasks. Use GPT-3.5 or Mistral for simple queries.',
            },
            {
                'priority': 'High',
                'category': 'Query Optimization',
                'action': 'Implement prompt caching and response caching',
                'potential_reduction': '20-40%',
                'description': 'Cache frequent queries to reduce duplicate API calls.',
            },
            {
                'priority': 'Medium',
                'category': 'Regional Optimization',
                'action': 'Route queries to low-carbon regions when possible',
                'potential_reduction': '10-30%',
                'description': 'Use providers with data centers in regions with clean energy grids.',
            },
            {
                'priority': 'Medium',
                'category': 'Batch Processing',
                'action': 'Batch non-urgent requests during off-peak hours',
                'potential_reduction': '5-15%',
                'description': 'Process batch jobs when grid carbon intensity is lower.',
            },
            {
                'priority': 'Low',
                'category': 'Employee Training',
                'action': 'Train employees on efficient AI usage',
                'potential_reduction': '10-20%',
                'description': 'Educate teams on writing effective prompts to reduce token usage.',
            },
        ]
        
        if annual_co2_tonnes > 100:
            recommendations.insert(0, {
                'priority': 'Critical',
                'category': 'Carbon Offsets',
                'action': 'Implement immediate carbon offset program',
                'potential_reduction': '100% (offset)',
                'description': 'At your emission level, immediate offsetting is recommended.',
            })
        
        return recommendations
    
    def compare_models_for_enterprise(
        self,
        employees: int,
        queries_per_person_per_day: float,
        models: List[str]
    ) -> List[Dict]:
        """
        Compare different models for enterprise use case.
        
        Args:
            employees: Number of employees
            queries_per_person_per_day: Average queries per person per day
            models: List of model IDs to compare
            
        Returns:
            List of comparison results sorted by efficiency
        """
        results = []
        
        for model in models:
            impact = self.calculate_annual_impact(
                employees=employees,
                queries_per_person_per_day=queries_per_person_per_day,
                model=model
            )
            
            profile = get_model_profile(model)
            
            results.append({
                'model': model,
                'model_name': profile['name'] if profile else model,
                'efficiency_rating': profile.get('efficiency_rating', 'N/A') if profile else 'N/A',
                'annual_co2_kg': impact['co2']['annual_kg'],
                'annual_co2_tonnes': impact['co2']['annual_tonnes'],
                'annual_energy_kwh': impact['energy']['annual_kwh'],
                'cost_to_offset_usd': round(impact['co2']['annual_tonnes'] * 25, 2),
                'trees_needed': round(self.carbon_equiv.co2_to_trees(impact['co2']['annual_kg'])),
            })
        
        return sorted(results, key=lambda x: x['annual_co2_kg'])
    
    def generate_sustainability_checklist(self) -> List[Dict]:
        """Generate a comprehensive sustainability checklist for enterprises."""
        return [
            {
                'category': 'Assessment',
                'items': [
                    'Audit current AI usage across teams',
                    'Identify most frequently used models',
                    'Measure baseline carbon footprint',
                    'Set emission reduction targets',
                ]
            },
            {
                'category': 'Optimization',
                'items': [
                    'Implement query caching system',
                    'Create model selection guidelines',
                    'Optimize prompt templates',
                    'Establish batch processing workflows',
                ]
            },
            {
                'category': 'Infrastructure',
                'items': [
                    'Evaluate cloud provider carbon intensity',
                    'Consider regional routing for queries',
                    'Explore on-premise options for frequent queries',
                    'Implement monitoring and reporting',
                ]
            },
            {
                'category': 'Offsetting',
                'items': [
                    'Research verified carbon offset programs',
                    'Calculate required offset budget',
                    'Establish partnership with offset provider',
                    'Set up automated offset purchasing',
                ]
            },
            {
                'category': 'Culture',
                'items': [
                    'Train employees on sustainable AI use',
                    'Include AI carbon in sustainability reports',
                    'Set team-level emission budgets',
                    'Celebrate sustainability achievements',
                ]
            },
        ]
