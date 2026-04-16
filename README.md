### Install Dependencies

Ensure Python is installed:

```bash
python --version
```

Install Flask and dependencies using pipenv:

```bash
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install flask
```

app = Flask(__name__)

# Event class
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory data store
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: POST /events - Create a new event from JSON input
# TODO: PATCH /events/<id> - Update the title of an event
# TODO: DELETE /events/<id> - Remove an event from the list

if __name__ == "__main__":
    app.run(debug=True)
```

---

### Task 4: Test the API

Start the Flask development server:

```bash
python app.py
```

Test your endpoints using Postman or curl:

- `POST http://localhost:5000/events`
  - Body: `{ "title": "Hackathon" }`
- `PATCH http://localhost:5000/events/1`
  - Body: `{ "title": "Hackathon 2025" }`
- `DELETE http://localhost:5000/events/2`

---

## Best Practices

- Use RESTful nouns in routes (e.g., `/events`)
- Validate incoming JSON and handle missing keys gracefully
- Use helper functions to reduce code repetition
- Return:
  - `201 Created` for successful POST
  - `200 OK` or `204 No Content` for PATCH and DELETE
  - `404 Not Found` if a resource doesn't exist
- Include inline comments to explain logic

---

## Considerations

**1. Input Validation**
- Ensure the `title` field is provided.
- Return a `400 Bad Request` if missing.

**2. Event Not Found**
- Return `404 Not Found` with a clear message when the event ID doesn't exist.

**3. Reusable Logic**
- Consider writing a helper function to look up events by ID.

**4. Scalability**
- While using a single file works here, separate concerns into modules as your API grows.

---

## API Documentation

This API manages a simple event system, allowing users to create, update, and delete events. Data is stored purely in-memory and will reset when the server restarts.

### Routes

#### 1. Create an Event
- **URL:** `/events`
- **Method:** `POST`
- **Description:** Creates a new event and returns it.
- **Example Request:**
  ```bash
  curl -X POST http://localhost:5000/events -H "Content-Type: application/json" -d '{"title": "Hackathon"}'
  ```
- **Example Response (`201 Created`):**
  ```json
  {
    "id": 3,
    "title": "Hackathon"
  }
  ```

#### 2. Update an Event
- **URL:** `/events/<id>`
- **Method:** `PATCH`
- **Description:** Updates the title of an existing event.
- **Example Request:**
  ```bash
  curl -X PATCH http://localhost:5000/events/1 -H "Content-Type: application/json" -d '{"title": "Updated Tech Meetup"}'
  ```
- **Example Response (`200 OK`):**
  ```json
  {
    "id": 1,
    "title": "Updated Tech Meetup"
  }
  ```

#### 3. Delete an Event
- **URL:** `/events/<id>`
- **Method:** `DELETE`
- **Description:** Removes an event from the in-memory store.
- **Example Request:**
  ```bash
  curl -X DELETE http://localhost:5000/events/2
  ```
- **Example Response (`200 OK`):**
  ```json
  {
    "message": "Event deleted successfully"
  }
  ```

