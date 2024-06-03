import re
from bs4 import BeautifulSoup

def extract_section_from_html(html_content, section_id):
    """
    Extracts a specific section from the HTML content.
    
    Args:
        html_content (str): The HTML content to search within.
        section_id (str): The ID of the section to extract.
    
    Returns:
        str: The extracted HTML section, or an empty string if not found.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    section = soup.find(id=section_id)
    return str(section) if section else ''

def validate_slug(slug):
    """
    Ensures the slug is valid for WordPress.
    
    Args:
        slug (str): The slug to validate.
    
    Returns:
        bool: True if the slug is valid, False otherwise.
    """
    if not slug:
        return False
    if slug != slug.lower():
        return False
    if not re.match("^[a-z0-9]+(?:-[a-z0-9]+)*$", slug):
        return False
    return True
