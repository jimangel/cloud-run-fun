// src/App.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, ListGroup, ListGroupItem, ListGroupItemHeading, ListGroupItemText } from "reactstrap";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    async function fetchNotes() {
      try {
        const response = await axios.get("http://localhost:8000/api/notes/");
        setNotes(response.data);
      } catch (error) {
        console.error("Failed to fetch notes:", error);
      }
    }
    fetchNotes();
  }, []);

  return (
    <Container className="mt-5">
      <h1>View Notes</h1>
      <ListGroup>
        {notes.map((note) => (
          <ListGroupItem key={note.id}>
            <ListGroupItemHeading>{note.title}</ListGroupItemHeading>
            <ListGroupItemText>{note.content}</ListGroupItemText>
          </ListGroupItem>
        ))}
      </ListGroup>
    </Container>
  );
}

export default App;
