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
        Given the information {things_to_do} about fun things to do, events and activities happening in Singapore, I want you to provide the answer in
        
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
    
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = event_template | llm | activity_parser
    
    urls = ["https://thesmartlocal.com/read/things-to-do-this-weekend-singapore/"]
    contents = scrape_urls(urls)
    things_to_do = "\n".join([c for c in contents])
    
    # print(f"things to do {things_to_do}")
    
    print("---------LLM outputs----------")
    
    response: ActivityList = chain.invoke(input={"things_to_do": things_to_do})
    response.source = "https://thesmartlocal.com/"
    print(response)
    return response
    