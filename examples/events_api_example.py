"""Example: pulling event metadata from Kaltura."""
import requests

BASE_URL = "https://example.kaltura.endpoint"
HEADERS = {"Authorization": "Kaltura <session-token>"}

def fetch_events(page_size=500, page_index=1):
    """One page of event objects."""
    params = {"pageSize": page_size, "pageIndex": page_index}
    r = requests.get(f"{BASE_URL}/api/v1/events", params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

def list_event_titles():
    """Iterate through all pages and print a few key fields."""
    page = 1
    while True:
        data = fetch_events(page_index=page)
        items = data.get("items", [])
        if not items:
            break
        for ev in items:
            print(ev.get("id"), ev.get("title"), ev.get("startDateTime"))
        page += 1

if __name__ == "__main__":
    list_event_titles()
