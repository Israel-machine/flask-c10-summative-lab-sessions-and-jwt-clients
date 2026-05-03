import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Login from "../pages/Login";
// 1. Add the import here
import MeetingContainer from "./MeetingContainer";

function App() {
  const [user, setUser] = useState(null);

 useEffect(() => {
  const token = localStorage.getItem("token");

  if (token) {
    fetch("/me", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }).then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      } else {
        localStorage.removeItem("token");
      }
    });
  }
}, []);

  const onLogin = (token, user) => {
    localStorage.setItem("token", token);
    setUser(user);
  }

  if (!user) return <Login onLogin={onLogin} />;

  return (
    <>
      <NavBar setUser={setUser} />
      <main>
        {/* 2. Replace the <p> tag with your container */}
        <MeetingContainer />
      </main>
    </>
  );
}

export default App;