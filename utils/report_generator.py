import os
from datetime import datetime
from typing import Dict, List, Optional
from fpdf import FPDF
import plotly.graph_objects as go


class SustainAIPDF(FPDF):
    """Custom PDF class for SustainAI reports."""
    
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(34, 139, 34)
        self.cell(0, 10, 'SustainAI Carbon Report', border=False, ln=True, align='C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')
    
    def chapter_title(self, title: str):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 100, 0)
        self.cell(0, 10, title, ln=True)
        self.ln(2)
    
    def chapter_body(self, body: str):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, body)
        self.ln(5)
    
    def add_metric_box(self, label: str, value: str, unit: str = ""):
        self.set_font('Helvetica', 'B', 10)
        self.set_fill_color(240, 255, 240)
        full_text = f"{label}: {value} {unit}".strip()
        self.cell(0, 8, full_text, ln=True, fill=True)
        self.ln(2)


class ReportGenerator:
    """
    PDF report generator for SustainAI.
    Generates comprehensive carbon footprint reports with charts and recommendations.
    """
    
    def __init__(self, output_dir: str = "reports"):
        """
        Initialize the report generator.
        
        Args:
            output_dir: Directory to save generated reports
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_individual_report(
        self,
        impact_data: Dict,
        equivalencies: Dict,
        recommendations: str,
        executive_summary: str
    ) -> str:
        """
        Generate an individual user impact report.
        
        Args:
            impact_data: Emission impact data
            equivalencies: Carbon equivalency calculations
            recommendations: LLM-generated recommendations
            executive_summary: Executive summary text
            
        Returns:
            Path to generated PDF file
        """
        pdf = SustainAIPDF()
        pdf.add_page()
        
        pdf.set_font('Helvetica', 'B', 20)
        pdf.set_text_color(34, 139, 34)
        pdf.cell(0, 15, 'AI Carbon Footprint Report', ln=True, align='C')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', ln=True, align='C')
        pdf.ln(10)
        
        pdf.chapter_title('Executive Summary')
        pdf.chapter_body(executive_summary)
        
        pdf.chapter_title('Emission Metrics')
        pdf.add_metric_box('Model Used', impact_data.get('model', 'N/A'))
        pdf.add_metric_box('Tokens Processed', f"{impact_data.get('tokens', 0):,}")
        pdf.add_metric_box('Energy Consumed', f"{impact_data.get('energy_wh', 0):.6f}", "Wh")
        pdf.add_metric_box('CO2 Emitted', f"{impact_data.get('co2_grams', 0):.6f}", "grams")
        pdf.add_metric_box('Region', impact_data.get('region', 'Global Average'))
        
        pdf.chapter_title('Environmental Equivalencies')
        equiv = equivalencies
        pdf.add_metric_box('Trees Needed (1 year)', f"{equiv.get('trees', {}).get('count', 0):.4f}")
        pdf.add_metric_box('Car Driving', f"{equiv.get('car', {}).get('km', 0):.4f}", "km")
        pdf.add_metric_box('Smartphone Charges', f"{equiv.get('devices', {}).get('smartphone_charges', 0):.2f}")
        pdf.add_metric_box('Streaming Video', f"{equiv.get('digital', {}).get('streaming_hours', 0):.2f}", "hours")
        
        pdf.chapter_title('Sustainability Recommendations')
        pdf.chapter_body(recommendations)
        
        pdf.add_page()
        pdf.chapter_title('Methodology & Formulas')
        methodology = """
Energy Calculation:
Energy (Wh) = Tokens x Energy per Token (Wh) x PUE Factor

CO2 Calculation:
CO2 (g) = Energy (kWh) x Grid Carbon Intensity (g CO2/kWh)

Key Conversion Factors:
- Tree absorption: 21 kg CO2/year
- Car emissions: 192 g CO2/km
- Smartphone charge: 8 g CO2
- Global grid average: 475 g CO2/kWh
        """
        pdf.chapter_body(methodology)
        
        filename = f"individual_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        pdf.output(filepath)
        
        return filepath
    
    def generate_enterprise_report(
        self,
        enterprise_data: Dict,
        model_comparison: List[Dict],
        offset_plan: Dict,
        executive_summary: str,
        checklist: List[Dict]
    ) -> str:
        """
        Generate an enterprise carbon footprint report.
        
        Args:
            enterprise_data: Enterprise calculation results
            model_comparison: Model comparison data
            offset_plan: Offset recommendations
            executive_summary: Executive summary text
            checklist: Sustainability checklist
            
        Returns:
            Path to generated PDF file
        """
        pdf = SustainAIPDF()
        pdf.add_page()
        
        pdf.set_font('Helvetica', 'B', 20)
        pdf.set_text_color(34, 139, 34)
        pdf.cell(0, 15, 'Enterprise AI Carbon Report', ln=True, align='C')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', ln=True, align='C')
        pdf.ln(10)
        
        pdf.chapter_title('Executive Summary')
        pdf.chapter_body(executive_summary)
        
        pdf.chapter_title('Enterprise Profile')
        inputs = enterprise_data.get('inputs', {})
        pdf.add_metric_box('Employees', f"{inputs.get('employees', 0):,}")
        pdf.add_metric_box('Queries/Person/Day', f"{inputs.get('queries_per_person_per_day', 0):.1f}")
        pdf.add_metric_box('Primary Model', inputs.get('model', 'N/A'))
        pdf.add_metric_box('Region', inputs.get('region', 'Global Average'))
        
        pdf.chapter_title('Annual Impact Summary')
        queries = enterprise_data.get('queries', {})
        energy = enterprise_data.get('energy', {})
        co2 = enterprise_data.get('co2', {})
        
        pdf.add_metric_box('Annual Queries', f"{queries.get('annual', 0):,}")
        pdf.add_metric_box('Annual Energy', f"{energy.get('annual_kwh', 0):.4f}", "kWh")
        pdf.add_metric_box('Annual CO2', f"{co2.get('annual_kg', 0):.4f}", "kg")
        pdf.add_metric_box('Annual CO2', f"{co2.get('annual_tonnes', 0):.6f}", "tonnes")
        
        pdf.add_page()
        pdf.chapter_title('Carbon Offset Plan')
        
        tree_offset = offset_plan.get('tree_offset', {})
        carbon_credits = offset_plan.get('carbon_credits', {})
        
        pdf.add_metric_box('Trees Required', f"{tree_offset.get('trees_needed', 0):,.0f}")
        pdf.add_metric_box('Area Needed', f"{tree_offset.get('area_hectares', 0):.2f}", "hectares")
        pdf.add_metric_box('Carbon Credits', f"{carbon_credits.get('credits_needed', 0):.2f}", "tonnes")
        pdf.add_metric_box('Offset Cost (Low)', f"${carbon_credits.get('cost_low_usd', 0):,.2f}")
        pdf.add_metric_box('Offset Cost (High)', f"${carbon_credits.get('cost_high_usd', 0):,.2f}")
        
        if model_comparison:
            pdf.chapter_title('Model Comparison')
            for model in model_comparison[:5]:
                line = f"{model.get('model_name', 'N/A')} ({model.get('efficiency_rating', 'N/A')}): {model.get('annual_co2_kg', 0):.4f} kg CO2/year"
                pdf.add_metric_box('', line)
        
        pdf.add_page()
        pdf.chapter_title('Sustainability Checklist')
        for category in checklist:
            pdf.set_font('Helvetica', 'B', 11)
            pdf.cell(0, 8, category.get('category', ''), ln=True)
            pdf.set_font('Helvetica', '', 10)
            for item in category.get('items', []):
                pdf.cell(0, 6, f"  [ ] {item}", ln=True)
            pdf.ln(3)
        
        filename = f"enterprise_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        pdf.output(filepath)
        
        return filepath
    
    def generate_company_comparison_report(
        self,
        companies: List[Dict],
        industry_totals: Dict,
        executive_summary: str
    ) -> str:
        """
        Generate a company comparison report.
        
        Args:
            companies: List of company profiles
            industry_totals: Industry-wide emission totals
            executive_summary: Executive summary text
            
        Returns:
            Path to generated PDF file
        """
        pdf = SustainAIPDF()
        pdf.add_page()
        
        pdf.set_font('Helvetica', 'B', 20)
        pdf.set_text_color(34, 139, 34)
        pdf.cell(0, 15, 'AI Industry Carbon Report', ln=True, align='C')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', ln=True, align='C')
        pdf.ln(10)
        
        pdf.chapter_title('Executive Summary')
        pdf.chapter_body(executive_summary)
        
        pdf.chapter_title('Industry Overview')
        pdf.add_metric_box('Total Annual Inference CO2', f"{industry_totals.get('total_annual_inference_co2_tonnes', 0):,.0f}", "tonnes")
        pdf.add_metric_box('Total Annual Training CO2', f"{industry_totals.get('total_annual_training_co2_tonnes', 0):,.0f}", "tonnes")
        pdf.add_metric_box('Total Annual CO2', f"{industry_totals.get('total_annual_co2_tonnes', 0):,.0f}", "tonnes")
        pdf.add_metric_box('Daily Queries (All Companies)', f"{industry_totals.get('total_daily_queries', 0):,.0f}")
        
        for company in companies:
            pdf.add_page()
            pdf.chapter_title(company.get('name', 'Unknown Company'))
            
            pdf.add_metric_box('Headquarters', company.get('headquarters', 'N/A'))
            pdf.add_metric_box('Sustainability Grade', company.get('sustainability_grade', 'N/A'))
            pdf.add_metric_box('Renewable Energy', f"{company.get('renewable_energy_percent', 0)}%")
            pdf.add_metric_box('Annual Inference CO2', f"{company.get('estimated_annual_inference_co2_tonnes', 0):,}", "tonnes")
            pdf.add_metric_box('Training CO2 (Est.)', f"{company.get('estimated_training_co2_tonnes', 0):,}", "tonnes")
            pdf.add_metric_box('Daily Queries (Est.)', f"{company.get('daily_queries_estimate', 0):,}")
            pdf.add_metric_box('Growth Rate', f"{company.get('growth_rate_percent', 0)}%")
            
            pdf.set_font('Helvetica', 'B', 11)
            pdf.cell(0, 8, 'Sustainability Initiatives:', ln=True)
            pdf.set_font('Helvetica', '', 10)
            for initiative in company.get('sustainability_initiatives', []):
                pdf.cell(0, 6, f"  - {initiative}", ln=True)
        
        filename = f"company_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        pdf.output(filepath)
        
        return filepath
    
    @staticmethod
    def create_model_comparison_chart(models: List[Dict]) -> go.Figure:
        """Create a plotly chart comparing model emissions."""
        model_names = [m.get('name', m.get('model_id', 'Unknown')) for m in models]
        co2_values = [m.get('co2_per_million_tokens_g', 0) for m in models]
        efficiency = [m.get('efficiency_rating', 'N/A') for m in models]
        
        colors = []
        for e in efficiency:
            if e == 'A+':
                colors.append('#2e7d32')
            elif e == 'A':
                colors.append('#4caf50')
            elif e == 'A-':
                colors.append('#8bc34a')
            elif e == 'B':
                colors.append('#ffc107')
            else:
                colors.append('#ff9800')
        
        fig = go.Figure(data=[
            go.Bar(
                x=model_names,
                y=co2_values,
                marker_color=colors,
                text=[f"{v:.1f}g" for v in co2_values],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title='CO2 Emissions per Million Tokens by Model',
            xaxis_title='Model',
            yaxis_title='CO2 (grams per 1M tokens)',
            template='plotly_white',
            height=400,
        )
        
        return fig
    
    @staticmethod
    def create_company_comparison_chart(companies: List[Dict]) -> go.Figure:
        """Create a plotly chart comparing company emissions."""
        company_names = [c.get('name', 'Unknown') for c in companies]
        inference_co2 = [c.get('estimated_annual_inference_co2_tonnes', 0) for c in companies]
        training_co2 = [c.get('estimated_training_co2_tonnes', 0) for c in companies]
        
        fig = go.Figure(data=[
            go.Bar(name='Inference CO2', x=company_names, y=inference_co2, marker_color='#4caf50'),
            go.Bar(name='Training CO2', x=company_names, y=training_co2, marker_color='#ff9800'),
        ])
        
        fig.update_layout(
            title='Annual CO2 Emissions by Company (tonnes)',
            xaxis_title='Company',
            yaxis_title='CO2 (tonnes/year)',
            barmode='stack',
            template='plotly_white',
            height=400,
        )
        
        return fig
    
    @staticmethod
    def create_equivalency_chart(equivalencies: Dict) -> go.Figure:
        """Create a visual representation of carbon equivalencies."""
        categories = ['Trees', 'Car km', 'Flights', 'Phone Charges', 'Streaming Hours']
        values = [
            equivalencies.get('trees', {}).get('count', 0),
            equivalencies.get('car', {}).get('km', 0),
            equivalencies.get('flights', {}).get('paris_nyc', 0) * 100,
            equivalencies.get('devices', {}).get('smartphone_charges', 0),
            equivalencies.get('digital', {}).get('streaming_hours', 0),
        ]
        
        fig = go.Figure(data=[
            go.Bar(
                x=categories,
                y=values,
                marker_color=['#2e7d32', '#1976d2', '#f57c00', '#7b1fa2', '#c62828'],
                text=[f"{v:.2f}" for v in values],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title='Carbon Equivalencies',
            xaxis_title='Category',
            yaxis_title='Equivalent Units',
            template='plotly_white',
            height=400,
        )
        
        return fig
