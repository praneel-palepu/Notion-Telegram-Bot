from notion_client import Client
from config import NOTION_API_KEY, NOTION_DATABASE_ID

notion = Client(auth=NOTION_API_KEY)

def update_notion_document(content: str) -> str:
    try:
        # Create a new page in the specified database
        page = notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties={
                "title": [{ "type": "text", "text": { "content": "Can I create a URL property", "link": None } }]
            },
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": content}}]
                    }
                }
            ]
        )

        # Return the URL of the created page
        return f"https://www.notion.so/{page['id'].replace('-', '')}"
    except Exception as e:
        raise Exception(f"Error updating Notion document: {str(e)}")