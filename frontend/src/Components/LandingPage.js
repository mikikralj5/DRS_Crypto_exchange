import React, { useState, useEffect } from "react";
import logo from "../logo.png";

const LandingPage = () => {
  const [user, setUser] = useState();

  return (
    // <div>
    //   <h1>Welcome</h1>
    //   <br />
    //   <p>You are not logged in</p>
    //   <a href="/login">
    //     <button>Login</button>
    //   </a>
    //   <a href="/register">
    //     <button>Register</button>
    //   </a>
    // </div>
    <nav>
      <p className="welcome">Log in to get started</p>
      <img src={logo} alt="Logo" className="logo" />
      <form className="login">
        <input
          type="text"
          placeholder="user"
          className="login__input login__input--user"
        />

        <input
          type="text"
          placeholder="PIN"
          maxLength="4"
          className="login__input login__input--pin"
        />
        <button className="login__btn">&rarr;</button>
      </form>
    </nav>
  );
};

export default LandingPage;
