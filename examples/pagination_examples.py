"""Examples of pagination patterns for Kaltura API responses."""

from typing import Iterator, Dict, Callable, Optional

def page_by_offset(fetch: Callable[[int, int], Dict], page_size=500) -> Iterator[Dict]:
    """Classic offset-based pagination (pageIndex + pageSize).
    Simple and works fine for smaller datasets."""
    page = 1
    while True:
        data = fetch(page_size, page)
        items = data.get("items", [])
        if not items:
            break
        for row in items:
            yield row
        page += 1


def page_by_token(fetch: Callable[[int, Optional[str]], Dict], page_size=500) -> Iterator[Dict]:
    """Cursor or token-based pagination.
    Keeps following the 'nextPageToken' until there isn’t one."""
    token = None
    while True:
        data = fetch(page_size, token)
        for row in data.get("items", []):
            yield row
        token = data.get("nextPageToken")
        if not token:
            break


def page_time_keyset(fetch: Callable[[str, str, Optional[str]], Dict],
                     start_iso: str, end_iso: str, last_id=None) -> Iterator[Dict]:
    """Keyset pagination scoped by a time window.
    Fetches records updated in a time range, advancing by last seen ID."""
    cursor = last_id
    while True:
        data = fetch(start_iso, end_iso, cursor)
        items = data.get("items", [])
        if not items:
            break
        for row in items:
            cursor = row.get("id")
            yield row
