"""Example: mapping Kaltura data objects to a target schema."""
from typing import Dict

def map_event(row: Dict) -> Dict:
    """Normalize event fields for EDMS or CRM compatibility."""
    return {
        "event_id": row.get("id"),
        "name": row.get("title"),
        "starts_at": row.get("startDateTime"),
        "ends_at": row.get("endDateTime"),
        "timezone": row.get("timezone"),
        "capacity": row.get("capacity"),
    }

def map_attendee(row: Dict) -> Dict:
    """Normalize attendee or registration objects."""
    return {
        "registration_id": row.get("id"),
        "event_id": row.get("eventId"),
        "email": row.get("email"),
        "status": row.get("status"),
        "updated_at": row.get("updatedAt"),
    }

def map_view(row: Dict) -> Dict:
    """Normalize viewership or engagement entries."""
    return {
        "user_id": row.get("userId"),
        "event_id": row.get("eventId"),
        "session_id": row.get("sessionId"),
        "watch_seconds": row.get("watchTimeSec"),
        "updated_at": row.get("updatedAt"),
    }
