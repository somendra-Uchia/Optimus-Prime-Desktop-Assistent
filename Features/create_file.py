import re

def get_file_extension(text):
    """Extracts the correct file extension based on user input."""
    extensions = {
        "python": ".py",
        "java": ".java",
        "text": ".txt",
        "html": ".html",
        "css": ".css",
        "javascript": ".js",
        "json": ".json",
        "xml": ".xml",
        "csv": ".csv",
        "markdown": ".md",
        "yaml": ".yaml",
        "c": ".c",
        "cpp": ".cpp",
        "php": ".php",
        "ruby": ".rb",
        "go": ".go",
        "rust": ".rs",
        "swift": ".swift",
        "kotlin": ".kt",
        "typescript": ".ts",
        "perl": ".pl",
        "bash": ".sh",
        "r": ".r",
        "dart": ".dart",
        "scala": ".scala",
        "lua": ".lua",
    }
    
    for key in extensions.keys():
        if key in text:
            return key, extensions[key]  # Return both key and extension
    
    return None, ""  # If no match found

def extract_filename(text, file_type):
    """Extracts a valid filename from user input while removing file type."""
    # Remove unnecessary words
    text = re.sub(r"\b(create|a|an|the|name|with name|file|make|new)\b", "", text, flags=re.IGNORECASE)
    text = text.strip()

    # Remove the detected file type (e.g., "java") from the filename
    if file_type:
        text = re.sub(rf"\b{file_type}\b", "", text, flags=re.IGNORECASE).strip()

    # Remove special characters except spaces and dashes
    text = re.sub(r"[^\w\s-]", "", text)  
    text = text.replace(" ", "_")  # Replace spaces with underscores

    return text

def create_file(text):
    """Creates a file based on spoken text input."""
    file_type, selected_ex = get_file_extension(text)
    filename = extract_filename(text, file_type)
    
    if not filename:  # If no valid filename is detected, use default
        filename = "untitled"

    full_filename = f"{filename}{selected_ex}"

    try:
        with open(full_filename, "w"):
            pass
        return f"File '{full_filename}' created successfully."
    except Exception as e:
        return f"Error creating file: {e}"

