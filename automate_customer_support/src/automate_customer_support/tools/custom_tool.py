from crewai.tools import BaseTool,  ScrapeWebsiteTool
from typing import Type
from pydantic import BaseModel, Field


class ScrapeWebsiteToolInput(BaseModel):
    """Input schema for MyCustomTool."""

class ScrapeWebsiteToolInput(BaseTool):
    name: str = "WebpageScraper"
    description: str = (
        "Scrapes a given website and extracts relevant content."
    )
    args_schema: Type[BaseModel] = ScrapeWebsiteToolInput

    def _run(self: str) -> str:
        # Implementation goes here
        return ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
	)
