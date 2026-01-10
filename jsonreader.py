import os
import json
from typing import List, Any, Union

def flatten_json(data: Any, parent_key: str = '', separator: str = ' > ') -> str:
    """
    Recursively flatten nested JSON objects and arrays into readable text.
    
    Args:
        data: JSON data (dict, list, or primitive)
        parent_key: Current key path for nested structures
        separator: Separator for hierarchical keys
    
    Returns:
        Flattened text representation
    """
    lines = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            
            if isinstance(value, (dict, list)):
                lines.append(f"\n{new_key}:")
                lines.append(flatten_json(value, new_key, separator))
            else:
                lines.append(f"{new_key}: {value}")
    
    elif isinstance(data, list):
        if all(isinstance(item, (str, int, float, bool, type(None))) for item in data):
            return ", ".join(str(item) for item in data)
        else:
            for idx, item in enumerate(data):
                item_key = f"{parent_key}[{idx}]" if parent_key else f"Item {idx}"
                if isinstance(item, (dict, list)):
                    lines.append(f"\n{item_key}:")
                    lines.append(flatten_json(item, item_key, separator))
                else:
                    lines.append(f"{item_key}: {item}")
    
    else:
        return str(data)
    
    return "\n".join(lines)


def read_json(file_path: str) -> List[str]:
    """
    Load a JSON file and convert it to readable text format.
    
    Args:
        file_path: Path to the JSON file
    
    Returns:
        List containing the flattened text (single page)
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file is not valid JSON
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    text = flatten_json(data)
    
    return [text]
