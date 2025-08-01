from crewai.tools import tool

class CalculatorTools:
    @staticmethod
    @tool("Calculate mathematical expressions")
    def calculate(expression: str) -> str:
        """Calculate mathematical expressions.
        
        Args:
            expression: The mathematical expression to evaluate
            
        Returns:
            str: The result of the calculation or error message
        """
        try:
            allowed_chars = set('0123456789+-*/(). ')
            if all(c in allowed_chars for c in expression):
                result = eval(expression)
                return str(result)
            else:
                return "Invalid expression"
        except Exception as e:
            return f"Calculation error: {str(e)}"