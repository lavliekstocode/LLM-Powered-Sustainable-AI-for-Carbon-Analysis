import tiktoken
from typing import Optional


class TokenEstimator:
    """
    Token estimation utility for various AI models.
    Uses tiktoken for accurate OpenAI token counting and approximations for other models.
    """
    
    CHARS_PER_TOKEN = {
        'gpt-3.5-turbo': 4.0,
        'gpt-4': 4.0,
        'gpt-4-turbo': 4.0,
        'gpt-5': 4.0,
        'claude-3.5-sonnet': 3.5,
        'claude-3.7-sonnet': 3.5,
        'gemini-ultra': 4.0,
        'gemini-pro': 4.0,
        'llama-3': 3.8,
        'mistral-large': 4.0,
        'falcon': 4.2,
    }
    
    TIKTOKEN_ENCODINGS = {
        'gpt-3.5-turbo': 'cl100k_base',
        'gpt-4': 'cl100k_base',
        'gpt-4-turbo': 'cl100k_base',
        'gpt-5': 'cl100k_base',
    }
    
    def __init__(self):
        self._encoders = {}
    
    def _get_encoder(self, model: str):
        """Get or create tiktoken encoder for a model."""
        encoding_name = self.TIKTOKEN_ENCODINGS.get(model, 'cl100k_base')
        if encoding_name not in self._encoders:
            try:
                self._encoders[encoding_name] = tiktoken.get_encoding(encoding_name)
            except Exception:
                self._encoders[encoding_name] = tiktoken.get_encoding('cl100k_base')
        return self._encoders[encoding_name]
    
    def estimate_tokens(self, text: str, model: str = 'gpt-4') -> int:
        """
        Estimate the number of tokens in a text for a given model.
        
        Args:
            text: The input text to tokenize
            model: The model name for token estimation
            
        Returns:
            Estimated number of tokens
        """
        if not text:
            return 0
        
        if model in self.TIKTOKEN_ENCODINGS:
            try:
                encoder = self._get_encoder(model)
                return len(encoder.encode(text))
            except Exception:
                pass
        
        chars_per_token = self.CHARS_PER_TOKEN.get(model, 4.0)
        return max(1, int(len(text) / chars_per_token))
    
    def estimate_response_tokens(self, prompt_tokens: int, model: str = 'gpt-4') -> int:
        """
        Estimate expected response tokens based on prompt tokens.
        Uses empirical ratios for different model types.
        
        Args:
            prompt_tokens: Number of tokens in the prompt
            model: The model name
            
        Returns:
            Estimated response tokens
        """
        response_ratios = {
            'gpt-3.5-turbo': 1.5,
            'gpt-4': 2.0,
            'gpt-4-turbo': 2.0,
            'gpt-5': 2.5,
            'claude-3.5-sonnet': 2.0,
            'claude-3.7-sonnet': 2.2,
            'gemini-ultra': 2.0,
            'gemini-pro': 1.8,
            'llama-3': 1.5,
            'mistral-large': 1.8,
            'falcon': 1.5,
        }
        
        ratio = response_ratios.get(model, 1.5)
        return int(prompt_tokens * ratio)
    
    def get_total_tokens(self, text: str, model: str = 'gpt-4', include_response: bool = True) -> dict:
        """
        Get comprehensive token analysis for a prompt.
        
        Args:
            text: The input prompt text
            model: The model name
            include_response: Whether to include estimated response tokens
            
        Returns:
            Dictionary with token breakdown
        """
        prompt_tokens = self.estimate_tokens(text, model)
        response_tokens = self.estimate_response_tokens(prompt_tokens, model) if include_response else 0
        total_tokens = prompt_tokens + response_tokens
        
        return {
            'prompt_tokens': prompt_tokens,
            'response_tokens': response_tokens,
            'total_tokens': total_tokens,
            'model': model,
            'text_length': len(text),
            'chars_per_token': len(text) / prompt_tokens if prompt_tokens > 0 else 0
        }
