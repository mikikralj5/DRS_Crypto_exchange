import React, { useState } from "react";

const LandingNav = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const logInUser = async () => {
    console.log(email, password);
    const resp = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await resp.json();
    if (data.status === 200) {
      // window.location.href = "/";
    }
  };
  return (
    <nav>
      <p className="welcome">Log in to get started</p>
      <form className="login">
        <input
          type="text"
          placeholder="email"
          className="login__input login__input--user"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="text"
          placeholder="password"
          className="login__input login__input--pin"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          type="button"
          className="login__btn"
          onClick={() => logInUser()}
        >
          &rarr;
        </button>
      </form>
    </nav>
  );
};

export default LandingNav;
