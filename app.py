from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Helper function to find an event by ID
def find_event(event_id):
    return next((e for e in events if e.id == event_id), None)

@app.route("/", methods=["GET"])
def index():
    # Return a JSON welcome message at the root route
    return jsonify({"message": "Welcome to the Event Management API"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    # Return a JSON array of all event data
    return jsonify([event.to_dict() for event in events]), 200

@app.route("/events", methods=["POST"])
def create_event():
    # Parse the incoming JSON request body
    data = request.get_json()
    
    # Input validation: ensure title is provided
    if not data or "title" not in data:
        return jsonify({"message": "Bad Request: 'title' is required"}), 400

    # Create a new event with an auto-incremented ID
    new_event = Event(len(events) + 1, data["title"])
    events.append(new_event)
    
    # Return the new event and a 201 Created status
    return jsonify(new_event.to_dict()), 201    

@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)
    if event:
        data = request.get_json()
        
        # Input validation: ensure title is provided
        if not data or "title" not in data:
            return jsonify({"message": "Bad Request: 'title' is required"}), 400
            
        # Update the event's title
        event.title = data["title"]
        # Return the updated event and a 200 OK status
        return jsonify(event.to_dict()), 200
        
    # If the event doesn't exist, return a 404 Not Found error
    return jsonify({"message": "Event not found"}), 404
   
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)
    if event:
        # Remove the event from the in-memory list
        events.remove(event)
        # Return a 204 No Content status
        return "", 204
        
    # If the event doesn't exist, return a 404 Not Found error
    return jsonify({"message": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
