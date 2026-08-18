from pathlib import Path
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

BASE = Path(__file__).parent
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

mcp = FastMCP("gmail-organizer")

def gmail():
    creds = Credentials.from_authorized_user_file(BASE / "token.json", SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        (BASE / "token.json").write_text(creds.to_json())
    return build("gmail", "v1", credentials=creds, cache_discovery=False)

@mcp.tool()
def search_messages(query: str, max_results: int = 20) -> list[dict[str, Any]]:
    """Search Gmail. This tool makes no changes."""
    service = gmail()
    response = service.users().messages().list(
        userId="me", q=query, maxResults=min(max_results, 100)
    ).execute()

    results = []
    for item in response.get("messages", []):
        message = service.users().messages().get(
            userId="me",
            id=item["id"],
            format="metadata",
            metadataHeaders=["From", "To", "Subject", "Date"],
        ).execute()
        headers = {
            h["name"].lower(): h["value"]
            for h in message.get("payload", {}).get("headers", [])
        }
        results.append({
            "id": message["id"],
            "thread_id": message["threadId"],
            "from": headers.get("from", ""),
            "subject": headers.get("subject", ""),
            "date": headers.get("date", ""),
            "labels": message.get("labelIds", []),
            "snippet": message.get("snippet", ""),
        })
    return results

@mcp.tool()
def list_labels() -> list[dict[str, str]]:
    """List Gmail labels. This tool makes no changes."""
    service = gmail()
    labels = service.users().labels().list(userId="me").execute()
    return [
        {"id": label["id"], "name": label["name"]}
        for label in labels.get("labels", [])
    ]

if __name__ == "__main__":
    mcp.run()