"""Example: pulling viewership and engagement data incrementally."""
import requests, datetime as dt

BASE_URL = "https://example.kaltura.endpoint"
HEADERS = {"Authorization": "Kaltura <session-token>"}

def fetch_viewership(event_id=None, page_size=500, page_token=None, since_iso=None):
    """Fetch a page of viewership data, optionally filtered by event or timestamp."""
    params = {"pageSize": page_size}
    if event_id:
        params["eventId"] = event_id
    if page_token:
        params["pageToken"] = page_token
    if since_iso:
        params["updatedAtFrom"] = since_iso
    r = requests.get(f"{BASE_URL}/api/v1/viewership", params=params, headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()

def pull_viewership(event_id=None, since_iso=None):
    """Paginate through all viewership records and print summarized info."""
    token = None
    while True:
        data = fetch_viewership(event_id, page_token=token, since_iso=since_iso)
        for v in data.get("items", []):
            print({
                "userId": v.get("userId"),
                "sessionId": v.get("sessionId"),
                "watchTimeSec": v.get("watchTimeSec")
            })
        token = data.get("nextPageToken")
        if not token:
            break

if __name__ == "__main__":
    since = (dt.datetime.utcnow() - dt.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M:%SZ")
    pull_viewership(event_id=None, since_iso=since)
