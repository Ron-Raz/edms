"""Example: exporting attendees with incremental updates."""
import requests, datetime as dt

BASE_URL = "https://example.kaltura.endpoint"
HEADERS = {"Authorization": "Kaltura <session-token>"}

def fetch_attendees(event_id, page_size=500, page_token=None, since_iso=None):
    """Fetch one page of attendees, optionally filtered by updatedAt."""
    params = {"eventId": event_id, "pageSize": page_size}
    if page_token:
        params["pageToken"] = page_token
    if since_iso:
        params["updatedAtFrom"] = since_iso
    r = requests.get(f"{BASE_URL}/api/v1/attendees", params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

def export_incremental(event_id, since_iso=None):
    """Iterate over all attendees updated since a given timestamp."""
    token = None
    while True:
        data = fetch_attendees(event_id, page_token=token, since_iso=since_iso)
        for row in data.get("items", []):
            print({"id": row.get("id"), "email": row.get("email"), "status": row.get("status")})
        token = data.get("nextPageToken")
        if not token:
            break

if __name__ == "__main__":
    cutoff = (dt.datetime.utcnow() - dt.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    export_incremental(event_id="EVT123", since_iso=cutoff)
