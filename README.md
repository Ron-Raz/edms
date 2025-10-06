# Kaltura Events to EDMS Integration — Reference Examples

This repository provides **concise, real-world examples** of how to integrate **Kaltura Events data** with an **Event Data Management System (EDMS)**.
It’s intended as a technical reference — not something to install or deploy — with focused, ready-to-adapt code snippets.

---

## 1. Purpose

These examples demonstrate how to:

* Retrieve event, attendee, and viewership data from Kaltura APIs.
* Handle large datasets using different pagination methods.
* Map and transform Kaltura data to external systems such as CRMs, analytics tools, or EDMS platforms.
* Apply privacy and data-retention practices aligned with typical AppSec requirements (for example, hard delete and anonymization after a defined period).

---

## 2. Repository Structure

```
kaltura-events-edms-integration/
├─ README.md
├─ examples/
│  ├─ pagination_examples.py       # Offset, token, keyset, and time-window patterns
│  ├─ events_api_example.py        # Retrieving event metadata
│  ├─ attendees_api_example.py     # Accessing attendee and registration data
│  ├─ viewership_api_example.py    # Exporting viewership and engagement data
│  ├─ data_mapping_example.py      # Translating Kaltura data for external systems
│  ├─ error_handling_example.py    # Retry, backoff, and partial result handling
│  └─ anonymization_example.py     # Removing or hashing PII for compliance
└─ LICENSE
```

Each file is self-contained and designed for reference. Replace endpoints, parameters, and credentials with those specific to your environment.

---

## 3. Event Data Domains

### Events

Typical attributes:

* `id`, `title`, `description`, `type`, `startDateTime`, `endDateTime`, `timezone`, `capacity`, `status`, `tags`.

### Attendees

Typical attributes:

* `id`, `eventId`, `email`, `registrationStatus`, `company`, `title`, `country`, `updatedAt`.

### Viewership

Typical attributes:

* `userId`, `eventId`, `sessionId`, `joinTime`, `leaveTime`, `watchTimeSec`, `device`, `geo`, `updatedAt`.

---

## 4. Pagination Strategies

The Kaltura API may limit results per request. The examples demonstrate multiple ways to retrieve large datasets efficiently.

### Offset and Limit

Use `pageIndex` and `pageSize`. Simple and reliable for small datasets.

### Token or Cursor-Based

Follow the `nextPageToken` returned by the API for stable, continuous iteration.

### Time-Windowed Incremental

Query based on timestamps (for example, `updatedAt >= last_sync_time`) for incremental updates.

### Keyset (Seek-Based)

Iterate by a stable key (for example, `id > last_id_seen`) for efficient traversal without offset overhead.

---

## 5. Data Mapping

Kaltura field names may differ from your target schema. Example mapping:

```yaml
Event:
  id: event_id
  title: name
  startDateTime: starts_at
  endDateTime: ends_at
Attendee:
  id: registration_id
  eventId: event_id
  email: email
  registrationStatus: status
View:
  userId: user_id
  eventId: event_id
  watchTimeSec: watch_seconds
```

---

## 6. Error Handling and Resilience

Patterns included for stability and reliability:

* **Exponential backoff** with random delay to avoid rate-limit collisions.
* **Checkpointing** to allow restart from the last processed record.
* **Clear logging** for page size, runtime, and completion status.

---

## 7. Privacy and Data Retention

To align with AppSec and privacy requirements, examples include anonymization and cleanup logic.

```python
import hashlib

def anonymize(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()[:12]
```

These patterns can be adapted to enforce per-event or global retention policies, with either hard deletion or irreversible hashing of user identifiers.

---

## 8. Example Highlights

* **pagination_examples.py** — demonstrates offset, token, and incremental pagination.
* **events_api_example.py** — retrieves events metadata and updates.
* **attendees_api_example.py** — exports registration and attendee data.
* **viewership_api_example.py** — extracts viewership and engagement metrics.
* **anonymization_example.py** — shows anonymization aligned with retention policies.

---

## 9. References

For detailed API and authentication documentation:

* [Kaltura Developer Portal](https://developer.kaltura.com)
* [Kaltura API Reference](https://developer.kaltura.com/api-docs/)
* [Kaltura Knowledge Base](https://knowledge.kaltura.com/help)

---

This collection focuses on practical API usage patterns and best practices for integration, not on packaging or deployment. Adapt as needed for your workflow and data policies.
