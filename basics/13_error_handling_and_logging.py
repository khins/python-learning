# 13_error_handling_and_logging.py
import logging
from pathlib import Path    
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def read_file(path: Path) -> str:
    try:
        content = path.read_text(encoding="utf-8")
        logging.info(f"Successfully read file: {path}")
        return content
    except FileNotFoundError:
        logging.error(f"File not found: {path}")
        return ""
    except Exception as e:
        logging.error(f"Error reading file {path}: {e}")
        return ""
    
def divide_numbers(a: float, b: float) -> float:
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        return float('inf')  # Return infinity as a fallback
    except Exception as e:
        logging.error(f"Error during division: {e}")
        return float('nan')  # Return NaN as a fallback
    
# Main execution
if __name__ == "__main__":
    # Example usage of read_file
    file_content = read_file(Path("example.txt"))
    
    # Example usage of divide_numbers
    result1 = divide_numbers(10, 2)
    result2 = divide_numbers(10, 0)