# blog/utils.py
import requests

def fetch_wikipedia_image(title, house_type):
    if house_type == "Abbey":
        title += "_Abbey"
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=500"
    response = requests.get(url)
    data = response.json()
    pages = data.get('query', {}).get('pages', {})
    for page_id, page in pages.items():
        if 'thumbnail' in page:
            return page['thumbnail']['source']
    return None