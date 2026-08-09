import os
from typing import Dict, Optional
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class LLMExplainer:
    """
    LLM-based sustainability recommendation and explanation engine.
    Uses OpenAI GPT to generate natural language explanations and recommendations.
    
    Note: the newest OpenAI model is "gpt-5" which was released August 7, 2025.
    do not change this unless explicitly requested by the user
    """
    
    def __init__(self):
        """Initialize the LLM explainer with OpenAI client."""
        self.client = None
        if OPENAI_API_KEY:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
    
    def _check_client(self) -> bool:
        """Check if OpenAI client is available."""
        return self.client is not None
    
    def explain_emission_impact(self, impact_data: Dict) -> str:
        """
        Generate a natural language explanation of emission impact.
        
        Args:
            impact_data: Dictionary containing emission metrics
            
        Returns:
            Human-readable explanation of the environmental impact
        """
        if not self._check_client():
            return self._generate_fallback_explanation(impact_data)
        
        prompt = f"""You are an AI sustainability expert. Explain the following AI usage environmental impact in simple, clear terms. Be concise but informative.

Impact Data:
- Model Used: {impact_data.get('model', 'Unknown')}
- Tokens Processed: {impact_data.get('tokens', 0):,}
- Energy Consumed: {impact_data.get('energy_wh', 0):.6f} Wh
- CO2 Emitted: {impact_data.get('co2_grams', 0):.6f} grams
- Region: {impact_data.get('region', 'Global Average')}

Equivalencies:
- Trees needed: {impact_data.get('trees', 0):.4f}
- Car km equivalent: {impact_data.get('car_km', 0):.4f}
- Smartphone charges: {impact_data.get('smartphone_charges', 0):.2f}

Provide:
1. A brief explanation of what these numbers mean in everyday terms
2. Context for whether this is a small or significant impact
3. One actionable tip to reduce impact

Keep the response under 150 words."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-5",
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=500,
            )
            return response.choices[0].message.content
        except Exception as e:
            return self._generate_fallback_explanation(impact_data)
    
    def generate_sustainability_recommendations(
        self, 
        usage_profile: Dict,
        context: str = "individual"
    ) -> str:
        """
        Generate personalized sustainability recommendations.
        
        Args:
            usage_profile: Dictionary with usage patterns and metrics
            context: "individual" or "enterprise"
            
        Returns:
            Personalized recommendations
        """
        if not self._check_client():
            return self._generate_fallback_recommendations(context)
        
        prompt = f"""You are an AI sustainability consultant. Generate specific, actionable recommendations for reducing AI carbon footprint.

Context: {context.capitalize()} user

Usage Profile:
- Primary Model: {usage_profile.get('primary_model', 'Various')}
- Daily Queries: {usage_profile.get('daily_queries', 'Unknown')}
- Annual CO2 (kg): {usage_profile.get('annual_co2_kg', 0):.4f}
- Region: {usage_profile.get('region', 'Global Average')}
- Current Efficiency Rating: {usage_profile.get('efficiency_rating', 'N/A')}

Provide 5 specific recommendations:
1. Model selection optimization
2. Query efficiency improvement  
3. Infrastructure considerations
4. Offset strategies
5. Long-term sustainability practices

For each, explain the potential impact (percentage reduction or offset). Keep total response under 300 words."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-5",
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=800,
            )
            return response.choices[0].message.content
        except Exception as e:
            return self._generate_fallback_recommendations(context)
    
    def compare_models_for_task(self, task_description: str, models: list) -> str:
        """
        Recommend the most efficient model for a specific task.
        
        Args:
            task_description: Description of the AI task
            models: List of available models
            
        Returns:
            Model recommendation with reasoning
        """
        if not self._check_client():
            return self._generate_fallback_model_comparison(models)
        
        prompt = f"""You are an AI efficiency expert. Recommend the most environmentally efficient model for this task.

Task: {task_description}

Available Models (ordered by energy efficiency):
{chr(10).join(f'- {m}' for m in models)}

Consider:
1. Task complexity requirements
2. Energy efficiency of each model
3. Quality vs. environmental trade-offs

Provide:
1. Recommended model and why
2. Alternative if highest quality needed
3. Estimated energy savings from your recommendation

Keep response under 150 words."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-5",
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=400,
            )
            return response.choices[0].message.content
        except Exception as e:
            return self._generate_fallback_model_comparison(models)
    
    def generate_executive_summary(self, report_data: Dict) -> str:
        """
        Generate an executive summary for PDF reports.
        
        Args:
            report_data: Comprehensive report data
            
        Returns:
            Executive summary text
        """
        if not self._check_client():
            return self._generate_fallback_executive_summary(report_data)
        
        prompt = f"""You are a sustainability report writer. Create a professional executive summary for an AI carbon footprint report.

Report Data:
- Report Type: {report_data.get('report_type', 'Individual')}
- Period: {report_data.get('period', 'Annual')}
- Total Queries: {report_data.get('total_queries', 0):,}
- Total Energy (kWh): {report_data.get('total_energy_kwh', 0):.4f}
- Total CO2 (kg): {report_data.get('total_co2_kg', 0):.4f}
- Primary Model: {report_data.get('primary_model', 'Various')}
- Region: {report_data.get('region', 'Global')}
- Trees Needed for Offset: {report_data.get('trees_needed', 0):.2f}

Write a professional executive summary that:
1. Summarizes key environmental metrics
2. Provides context and benchmarks
3. Highlights areas of concern
4. Offers 3 key recommendations
5. Ends with a positive action-oriented conclusion

Keep it under 200 words, professional tone."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-5",
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=600,
            )
            return response.choices[0].message.content
        except Exception as e:
            return self._generate_fallback_executive_summary(report_data)
    
    def chat_response(self, user_message: str, context: Optional[Dict] = None) -> str:
        """
        Generate a chatbot response for sustainability questions.
        
        Args:
            user_message: User's question or message
            context: Optional context about current session
            
        Returns:
            Chatbot response
        """
        if not self._check_client():
            return "I'm sorry, but I need an OpenAI API key to provide personalized responses. Please configure your API key in the settings."
        
        system_prompt = """You are SustainAI, an AI sustainability expert assistant. You help users understand and reduce the environmental impact of AI usage.

Your expertise includes:
- AI model energy consumption and carbon emissions
- Carbon equivalency calculations
- Sustainability best practices for AI usage
- Enterprise AI carbon management
- Carbon offset strategies
- Green AI technologies and trends

Be helpful, accurate, and environmentally conscious. Use data when possible.
Keep responses concise but informative (under 200 words unless more detail is requested)."""

        context_info = ""
        if context:
            context_info = f"\n\nCurrent Session Context:\n- Model: {context.get('model', 'N/A')}\n- Region: {context.get('region', 'N/A')}\n- Recent CO2: {context.get('recent_co2', 'N/A')}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-5",
                messages=[
                    {"role": "system", "content": system_prompt + context_info},
                    {"role": "user", "content": user_message}
                ],
                max_completion_tokens=600,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I apologize, but I encountered an error processing your request. Please try again or check your API configuration."
    
    def _generate_fallback_explanation(self, impact_data: Dict) -> str:
        """Generate explanation without LLM."""
        co2_g = impact_data.get('co2_grams', 0)
        tokens = impact_data.get('tokens', 0)
        
        if co2_g < 0.1:
            impact_level = "minimal"
        elif co2_g < 1:
            impact_level = "small"
        elif co2_g < 10:
            impact_level = "moderate"
        else:
            impact_level = "significant"
        
        return f"""Your AI query processed {tokens:,} tokens, consuming {impact_data.get('energy_wh', 0):.6f} Wh of energy and emitting {co2_g:.6f} grams of CO2.

This represents a {impact_level} environmental impact. To put this in perspective, it's equivalent to about {impact_data.get('smartphone_charges', 0):.4f} smartphone charges.

Tip: For simpler queries, consider using a more efficient model like GPT-3.5 or Mistral to reduce energy consumption by up to 70%."""
    
    def _generate_fallback_recommendations(self, context: str) -> str:
        """Generate recommendations without LLM."""
        if context == "enterprise":
            return """**Sustainability Recommendations for Enterprise AI Usage**

1. **Model Selection**: Use GPT-3.5 or Mistral for routine tasks - potential 50-70% energy reduction
2. **Query Caching**: Implement response caching for repeated queries - potential 20-40% reduction
3. **Regional Routing**: Route to data centers in low-carbon regions (France, Sweden, Norway)
4. **Batch Processing**: Process non-urgent requests during off-peak hours
5. **Carbon Offsets**: Establish a carbon credit purchasing program for residual emissions

Implementing these strategies could reduce your AI carbon footprint by 40-60%."""
        else:
            return """**Personal AI Sustainability Tips**

1. **Choose Efficient Models**: Use GPT-3.5 or Claude for simple tasks
2. **Write Better Prompts**: Clear, concise prompts reduce token usage
3. **Batch Your Questions**: Combine related queries into single sessions
4. **Consider Alternatives**: For simple lookups, traditional search may be greener
5. **Offset Your Usage**: Plant trees or purchase carbon credits

Small changes in usage habits can significantly reduce your AI carbon footprint."""
    
    def _generate_fallback_model_comparison(self, models: list) -> str:
        """Generate model comparison without LLM."""
        efficient_models = ['gpt-3.5-turbo', 'gemini-pro', 'mistral-large', 'llama-3']
        recommended = next((m for m in efficient_models if m in models), models[0] if models else "gpt-3.5-turbo")
        
        return f"""**Model Recommendation**

For most tasks, I recommend **{recommended}** as it offers an excellent balance of capability and energy efficiency.

For complex reasoning tasks requiring maximum quality, consider GPT-4 or Claude 3.7, accepting the higher environmental cost.

Using efficient models for routine tasks can reduce energy consumption by 50-70% compared to flagship models."""
    
    def _generate_fallback_executive_summary(self, report_data: Dict) -> str:
        """Generate executive summary without LLM."""
        co2_kg = report_data.get('total_co2_kg', 0)
        queries = report_data.get('total_queries', 0)
        trees = report_data.get('trees_needed', 0)
        
        return f"""**Executive Summary: AI Carbon Footprint Report**

This report analyzes the environmental impact of AI usage over the reporting period.

**Key Metrics:**
- Total Queries: {queries:,}
- Total CO2 Emissions: {co2_kg:.4f} kg
- Trees Required for Offset: {trees:.2f}

**Recommendations:**
1. Optimize model selection based on task complexity
2. Implement query caching for frequently asked questions
3. Consider carbon offset programs for residual emissions

**Conclusion:**
By implementing the recommended strategies, organizations can significantly reduce their AI-related carbon footprint while maintaining operational effectiveness. Continuous monitoring and optimization are key to sustainable AI usage."""
