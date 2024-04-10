import zipfile
import os

def get_base_directory():
    """
    Returns the base directory path based on the environment.
    
    If running in Google Colab, returns '/content/', otherwise returns an empty string.
    """
    try:
        import google.colab
        return '/content/'
    except ImportError:
        return ''

def unzip_file(zip_file_path, extract_to_path):
    """
    Unzips a zip file to a specified directory.

    Parameters:
    - zip_file_path (str): Path to the zip file.
    - extract_to_path (str): Directory where the contents of the zip file will be extracted.

    Returns:
    - extracted_files (list): List of paths to the extracted files.
    """
    # Check if the zip file exists
    if not os.path.exists(zip_file_path):
        print(f"Error: Zip file '{zip_file_path}' not found.")
        return None
    
    # Create the extraction directory if it doesn't exist
    if not os.path.exists(extract_to_path):
        os.makedirs(extract_to_path)
    
    # Initialize a list to store the paths of extracted files
    extracted_files = []

    # Unzip the file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
        extracted_files = zip_ref.namelist()
        print("Extraction complete.")

    return extracted_files

# Function to map countries to regions
def map_to_region(country):
      """
      Maps a country with predefined category.

      Parameters:
      - country: name of a country

      Returns:
      - region of the country
      """
    region_mapping = {
        'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'],
        'US': ['US'],
        'China': ['China'],
        'EU': ['UK', 'Germany', 'France', 'Italy', 'Spain', 'Netherlands', 'Belgium', 'Sweden', 'Poland', 'Austria', 'Switzerland', 'Norway', 'Denmark', 'Finland', 'Greece', 'Portugal', 'Ireland', 'Czech Republic', 'Romania', 'Hungary', 'Slovakia', 'Croatia', 'Bulgaria', 'Estonia', 'Slovenia', 'Lithuania', 'Latvia', 'Luxembourg', 'Malta', 'Cyprus'],
        'Russia': ['Russia'],
        'Ukraine': ['Ukraine'],
        'Middle East': ['Saudi Arabia', 'Iran', 'Iraq', 'United Arab Emirates', 'Qatar', 'Kuwait', 'Bahrain', 'Oman', 'Yemen', 'Syria', 'Jordan', 'Lebanon', 'Israel', 'Palestine', 'Egypt', 'Turkey']
    }

    for region, countries in region_mapping.items():
        if country in countries:
            return region
    return 'Other'

# Function to extract domain names from URLs
def extract_domain(url):
    if "://" in url:
        url = url.split("://")[1]
    return url.split("/")[0]
