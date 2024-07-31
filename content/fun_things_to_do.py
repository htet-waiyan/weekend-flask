from typing import List, Dict, Any, Optional
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class FunActivity(BaseModel):
    title: str = Field(description="Title of the event or activity")
    description: str = Field(description="escription of the event or activity")
    date: str = Field(description="Date & time of the event or activity.")
    location: str = Field(description="Place of the event or activity that takes place")
    ticket: Optional[str] = Field(description="Ticket fee or entrace fee")
    
    def to_dict(self) -> Dict[str, Any]:
        return {"title": self.title, "description": self.description, "date": self.date, "location": self.location, "ticket": self.ticket}

class ActivityList(BaseModel):
    summary: Optional[str] = Field(description="Catchy one liner summary of all the activities")
    activities: Optional[List[FunActivity]] = Field(description="List of fun activities")
    source: str = None
    
    def to_dict(self) -> Dict[str, Any]:
        activities_data = [a.to_dict() for a in self.activities] if self.activities is not None else []
        return {"summary": self.summary, "activities": activities_data, "source": self.source}
    
activity_parser = PydanticOutputParser(pydantic_object=ActivityList)