# Product Spec

## Step 1
Search Google or Tavily "things to do this weekend in {location}. Get top 5 urls.

## Step 2
Scrape each urls and retrieve content

## Step 3
Ask LLM to summarise the web content in
- Title of the event or activity
- Brief description of the event or activity
- Date & Time of the event or activity
- Place of the event or activity
- Entrace or ticket fee if any

## Step 4
Curated list may have duplicates. Ask LLM to find the unique events

## Step 5
Return as JSON

## Next improvement
### Extract event photo and details url
Current version is only able to extract the text. Next version is to locate the each event content from the web response and extract the event photo url and event details url.

### Scrape the second level event details link
Some website link to the more details event. Next version is to scrape the second level event details content.