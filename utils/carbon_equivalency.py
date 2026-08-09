from typing import Dict


class CarbonEquivalency:
    """
    Carbon equivalency calculator for real-world comparisons.
    
    Scientific basis for conversion factors:
    - Trees: Average tree absorbs ~21 kg CO2/year (EPA, IPCC)
    - Cars: Average car emits ~192g CO2/km (EU average, includes manufacturing)
    - Flights: ~255g CO2 per passenger-km (IATA, economy class)
    - Household electricity: ~475g CO2/kWh global average
    - LPG: ~3.0 kg CO2 per kg LPG burned
    - Smartphone charge: ~8g CO2 per full charge (global average)
    - Streaming video: ~36g CO2 per hour (HD streaming)
    - Google search: ~0.2g CO2 per search
    """
    
    TREE_CO2_ABSORPTION_KG_PER_YEAR = 21.0
    
    CAR_CO2_G_PER_KM = 192.0
    
    FLIGHT_CO2_G_PER_PASSENGER_KM = 255.0
    FLIGHT_PARIS_NYC_KM = 5837
    FLIGHT_LONDON_LA_KM = 8756
    FLIGHT_SF_TOKYO_KM = 8280
    
    HOUSEHOLD_CO2_G_PER_KWH = 475.0
    AVG_HOUSEHOLD_KWH_PER_DAY = 29.0
    
    LPG_CO2_KG_PER_KG = 3.0
    LPG_KG_PER_CYLINDER = 14.2
    
    SMARTPHONE_CHARGE_CO2_G = 8.0
    LAPTOP_CHARGE_CO2_G = 52.0
    
    STREAMING_CO2_G_PER_HOUR = 36.0
    GOOGLE_SEARCH_CO2_G = 0.2
    
    BEEF_CO2_KG_PER_KG = 27.0
    COFFEE_CO2_G_PER_CUP = 21.0
    
    def co2_to_trees(self, co2_kg: float) -> float:
        """
        Convert CO2 emissions to equivalent trees needed per year.
        
        Formula: Trees = CO2 (kg) / 21 kg absorbed per tree per year
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Number of trees needed to absorb this CO2 in one year
        """
        return co2_kg / self.TREE_CO2_ABSORPTION_KG_PER_YEAR
    
    def co2_to_car_km(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent car driving distance.
        
        Formula: Distance (km) = CO2 (g) / 192 g per km
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent driving distance in kilometers
        """
        co2_g = co2_kg * 1000
        return co2_g / self.CAR_CO2_G_PER_KM
    
    def co2_to_flights(self, co2_kg: float, route: str = 'paris_nyc') -> float:
        """
        Convert CO2 to equivalent flight segments.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            route: Flight route ('paris_nyc', 'london_la', 'sf_tokyo')
            
        Returns:
            Number of equivalent one-way flights
        """
        route_distances = {
            'paris_nyc': self.FLIGHT_PARIS_NYC_KM,
            'london_la': self.FLIGHT_LONDON_LA_KM,
            'sf_tokyo': self.FLIGHT_SF_TOKYO_KM,
        }
        
        distance = route_distances.get(route, self.FLIGHT_PARIS_NYC_KM)
        co2_g = co2_kg * 1000
        flight_co2_g = distance * self.FLIGHT_CO2_G_PER_PASSENGER_KM
        
        return co2_g / flight_co2_g
    
    def co2_to_household_hours(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent household electricity hours.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent hours of average household electricity use
        """
        co2_g = co2_kg * 1000
        kwh_used = co2_g / self.HOUSEHOLD_CO2_G_PER_KWH
        hours = (kwh_used / self.AVG_HOUSEHOLD_KWH_PER_DAY) * 24
        return hours
    
    def co2_to_household_days(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent days of household electricity.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent days of average household electricity use
        """
        return self.co2_to_household_hours(co2_kg) / 24
    
    def co2_to_lpg_kg(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent LPG burned.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent kilograms of LPG burned
        """
        return co2_kg / self.LPG_CO2_KG_PER_KG
    
    def co2_to_lpg_cylinders(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent LPG cylinders (14.2kg).
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent number of standard LPG cylinders
        """
        return self.co2_to_lpg_kg(co2_kg) / self.LPG_KG_PER_CYLINDER
    
    def co2_to_smartphone_charges(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent smartphone charges.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent number of full smartphone charges
        """
        co2_g = co2_kg * 1000
        return co2_g / self.SMARTPHONE_CHARGE_CO2_G
    
    def co2_to_laptop_charges(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent laptop charges.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent number of full laptop charges
        """
        co2_g = co2_kg * 1000
        return co2_g / self.LAPTOP_CHARGE_CO2_G
    
    def co2_to_streaming_hours(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent HD streaming hours.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent hours of HD video streaming
        """
        co2_g = co2_kg * 1000
        return co2_g / self.STREAMING_CO2_G_PER_HOUR
    
    def co2_to_google_searches(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent Google searches.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent number of Google searches
        """
        co2_g = co2_kg * 1000
        return co2_g / self.GOOGLE_SEARCH_CO2_G
    
    def co2_to_coffee_cups(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent cups of coffee.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent cups of coffee (lifecycle emissions)
        """
        co2_g = co2_kg * 1000
        return co2_g / self.COFFEE_CO2_G_PER_CUP
    
    def co2_to_beef_kg(self, co2_kg: float) -> float:
        """
        Convert CO2 to equivalent beef production.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Equivalent kilograms of beef production
        """
        return co2_kg / self.BEEF_CO2_KG_PER_KG
    
    def calculate_all_equivalencies(self, co2_kg: float) -> Dict:
        """
        Calculate all carbon equivalencies for a given CO2 amount.
        
        Args:
            co2_kg: CO2 emissions in kilograms
            
        Returns:
            Dictionary with all equivalency calculations
        """
        return {
            'co2_kg': round(co2_kg, 6),
            'co2_grams': round(co2_kg * 1000, 4),
            'trees': {
                'count': round(self.co2_to_trees(co2_kg), 2),
                'description': f"{round(self.co2_to_trees(co2_kg), 2)} trees needed for 1 year to absorb",
                'formula': 'CO2 (kg) / 21 kg per tree per year',
            },
            'car': {
                'km': round(self.co2_to_car_km(co2_kg), 2),
                'miles': round(self.co2_to_car_km(co2_kg) * 0.621371, 2),
                'description': f"Equivalent to driving {round(self.co2_to_car_km(co2_kg), 2)} km",
                'formula': 'CO2 (g) / 192 g per km',
            },
            'flights': {
                'paris_nyc': round(self.co2_to_flights(co2_kg, 'paris_nyc'), 4),
                'london_la': round(self.co2_to_flights(co2_kg, 'london_la'), 4),
                'sf_tokyo': round(self.co2_to_flights(co2_kg, 'sf_tokyo'), 4),
                'description': f"Equivalent to {round(self.co2_to_flights(co2_kg, 'paris_nyc'), 4)} Paris-NYC flights",
                'formula': 'CO2 (g) / (distance × 255 g per passenger-km)',
            },
            'household': {
                'hours': round(self.co2_to_household_hours(co2_kg), 2),
                'days': round(self.co2_to_household_days(co2_kg), 4),
                'description': f"Equivalent to {round(self.co2_to_household_hours(co2_kg), 2)} hours of household electricity",
                'formula': 'CO2 (g) / 475 g per kWh / 29 kWh per day × 24 hours',
            },
            'lpg': {
                'kg': round(self.co2_to_lpg_kg(co2_kg), 4),
                'cylinders': round(self.co2_to_lpg_cylinders(co2_kg), 4),
                'description': f"Equivalent to burning {round(self.co2_to_lpg_kg(co2_kg), 4)} kg of LPG",
                'formula': 'CO2 (kg) / 3.0 kg CO2 per kg LPG',
            },
            'devices': {
                'smartphone_charges': round(self.co2_to_smartphone_charges(co2_kg), 1),
                'laptop_charges': round(self.co2_to_laptop_charges(co2_kg), 2),
                'description': f"Equivalent to {round(self.co2_to_smartphone_charges(co2_kg), 1)} smartphone charges",
                'formula': 'CO2 (g) / 8 g per smartphone charge',
            },
            'digital': {
                'streaming_hours': round(self.co2_to_streaming_hours(co2_kg), 2),
                'google_searches': round(self.co2_to_google_searches(co2_kg), 1),
                'description': f"Equivalent to {round(self.co2_to_streaming_hours(co2_kg), 2)} hours of HD streaming",
                'formula': 'CO2 (g) / 36 g per streaming hour',
            },
            'food': {
                'coffee_cups': round(self.co2_to_coffee_cups(co2_kg), 2),
                'beef_kg': round(self.co2_to_beef_kg(co2_kg), 4),
                'description': f"Equivalent to {round(self.co2_to_coffee_cups(co2_kg), 2)} cups of coffee",
                'formula': 'CO2 (g) / 21 g per cup of coffee',
            },
        }
    
    @staticmethod
    def get_formula_explanations() -> Dict:
        """Get explanations for all conversion formulas."""
        return {
            'trees': {
                'formula': 'Trees = CO2 (kg) / 21',
                'explanation': 'An average tree absorbs approximately 21 kg of CO2 per year through photosynthesis.',
                'source': 'EPA, IPCC Reports',
            },
            'car': {
                'formula': 'Distance (km) = CO2 (g) / 192',
                'explanation': 'An average passenger car emits approximately 192g of CO2 per kilometer driven.',
                'source': 'European Environment Agency',
            },
            'flights': {
                'formula': 'Flights = CO2 (g) / (distance × 255)',
                'explanation': 'Air travel emits approximately 255g of CO2 per passenger-kilometer in economy class.',
                'source': 'IATA, ICAO Carbon Calculator',
            },
            'household': {
                'formula': 'Hours = CO2 (g) / 475 / 29 × 24',
                'explanation': 'Based on global average grid carbon intensity and household consumption.',
                'source': 'IEA World Energy Outlook',
            },
            'lpg': {
                'formula': 'LPG (kg) = CO2 (kg) / 3.0',
                'explanation': 'Burning 1 kg of LPG produces approximately 3.0 kg of CO2.',
                'source': 'IPCC Emission Factors',
            },
            'devices': {
                'formula': 'Charges = CO2 (g) / 8',
                'explanation': 'A full smartphone charge consumes about 0.012 kWh, producing ~8g CO2.',
                'source': 'Lawrence Berkeley National Laboratory',
            },
        }
