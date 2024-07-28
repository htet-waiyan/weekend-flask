from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv

load_dotenv()

def scrape_url(url:str):
    graph_config = {
        "llm": {
            "api_key": "",
            "model": "gpt-3.5-turbo",
        },
        "verbose": True,
        "headless": False,
    }
    prompt = """
        Find me the detail list of fun things to do in Singapore with description, date and time, place and ticket fee if any.
        Exclude the title list. Find me the details.
    """
    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        source=url,
        config=graph_config
    )

    # Run the pipeline
    print("start scraping.....")
    result = smart_scraper_graph.run()
    print(result)
    
if __name__ == "__main__":
    scrape_url("https://thesmartlocal.com/read/things-to-do-this-weekend-singapore/")