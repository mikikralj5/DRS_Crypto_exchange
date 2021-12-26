import React, { useState } from "react";
import { resolvePath, useNavigate } from "react-router-dom";

const LandingNav = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState(false);

  const navigate = useNavigate();

  const logInUser = async () => {
    const resp = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    setEmail("");
    setPassword("");

    if (resp.status == 401) {
      console.log("invalid credentials");
      setErr(true);
    } else {
      navigate("/mainPage");
    }
  };
  return (
    <nav>
      <p className="welcome">Log in to get started</p>
      <form className="login">
        {err ? (
          <p style={{ color: "red", marginRight: "3rem" }} className="welcome">
            Invalid credentials
          </p>
        ) : null}

        <input
          type="text"
          placeholder="email"
          className="login__input login__input--user"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
            setErr(false);
          }}
        />

        <input
          type="password"
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
