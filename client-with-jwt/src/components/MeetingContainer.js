import React, { useEffect, useState } from "react";
import { Button, Input, Textarea, FormField, Label, Error } from "../styles";

function MeetingContainer() {
  const [meetings, setMeetings] = useState([]);
  const [errors, setErrors] = useState([]);
  const [formData, setFormData] = useState({ 
    student_name: "", 
    meeting_date: "", 
    notes: "" 
  });

  const getHeaders = () => ({
  "Content-Type": "application/json",
  "Authorization": `Bearer ${localStorage.getItem("token")}`,
});

  useEffect(() => {
    fetch("/meetings", { headers: getHeaders() }).then((r) => {
      if (r.ok) {
        r.json().then(setMeetings);
      }
    });
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    setErrors([]);

    fetch("/meetings", {
      method: "POST",
      headers: getHeaders(),
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        r.json().then((newM) => {
          setMeetings([...meetings, newM]);
          setFormData({ student_name: "", meeting_date: "", notes: "" });
        });
      } else {
        r.json().then((err) => setErrors(err.errors || ["Failed to save meeting"]));
      }
    });
  }

  function handleDelete(id) {
    fetch(`/meetings/${id}`, { 
      method: "DELETE", 
      headers: getHeaders() 
    }).then((r) => {
      if (r.ok) {
        setMeetings(meetings.filter((m) => m.id !== id));
      }
    });
  }

  return (
    <section style={{ padding: "20px", maxWidth: "800px", margin: "0 auto" }}>
      <h2>Add New Meeting Note</h2>
      <form onSubmit={handleSubmit}>
        <FormField>
          <Label>Student Name</Label>
          <Input 
            required
            value={formData.student_name} 
            onChange={(e) => setFormData({...formData, student_name: e.target.value})} 
          />
        </FormField>
        <FormField>
          <Label>Date</Label>
          <Input 
            required
            type="date" 
            value={formData.meeting_date} 
            onChange={(e) => setFormData({...formData, meeting_date: e.target.value})} 
          />
        </FormField>
        <FormField>
          <Label>Notes</Label>
          <Textarea 
            rows="5"
            value={formData.notes} 
            onChange={(e) => setFormData({...formData, notes: e.target.value})} 
          />
        </FormField>
        
        {errors.map((err) => (
          <Error key={err}>{err}</Error>
        ))}

        <Button type="submit">Save Meeting</Button>
      </form>

      <hr style={{ margin: "40px 0" }} />

      <h2>Your Private Notes</h2>
      {meetings.length === 0 ? <p>No meetings recorded yet.</p> : null}
      
      {meetings.map((m) => (
        <div key={m.id} style={{ border: "1px solid #ddd", borderRadius: "8px", padding: "15px", margin: "15px 0", backgroundColor: "#f9f9f9" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <h3 style={{ margin: "0 0 10px 0", color: "indigo" }}>{m.student_name}</h3>
              <small>{m.meeting_date}</small>
            </div>
            <Button onClick={() => handleDelete(m.id)} color="secondary" variant="outline">Delete</Button>
          </div>
          <p style={{ marginTop: "15px", whiteSpace: "pre-wrap" }}>{m.notes}</p>
        </div>
      ))}
    </section>
  );
} 

export default MeetingContainer;