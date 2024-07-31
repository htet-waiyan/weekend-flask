from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts.prompt import PromptTemplate
from scrape.extract import scrape_urls
from .fun_things_to_do import activity_parser, ActivityList
import os

load_dotenv()

def get_fun_things_to_do() -> ActivityList:
    print(os.getenv("OPENAI_API_KEY"))
    template = """
        Given the information {things_to_do} about fun things to do, events and activities happening in Singapore.
        Look out for the text "New events in Singapore this week". Information about fun activities should follow after this text.
        
        I want you to provide the list of activties in
        
        1.) Catchy one liner summary of all the activities
        2.) List of fun activities in
            • Title of the event or activity
            • Description of the event or activity.
            • Date & time of the event or activity.
            • Place of the event or activity that takes place.
            • Ticket fee or entrace fee if any. Leave this blank if you cannot find the information.
        
        Use both information about fun things to do
        \n{format_instructions}
    """
    event_template = PromptTemplate(
        input_variables=["things_to_do"],
        template=template,
        partial_variables={"format_instructions": activity_parser.get_format_instructions()}
    )
    
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    chain = event_template | llm | activity_parser
    
    urls = ["https://thehoneycombers.com/singapore/things-to-do-in-singapore/"]
    contents = scrape_urls(urls)
    things_to_do = "\n".join([c for c in contents])
    
    print(f"things to do {things_to_do}")
    
    print("---------LLM outputs----------")
    
    response: ActivityList = chain.invoke(input={"things_to_do": things_to_do})
    response.source = "https://thehoneycombers.com/singapore/things-to-do-in-singapore/"
    print(response)
    return response
    