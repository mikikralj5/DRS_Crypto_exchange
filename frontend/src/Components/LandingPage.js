import React from "react";
import LandingNav from "./LandingNav";
import coin from "../coin.png";
import { Link } from "react-router-dom";
const LandingPage = () => {
  return (
    <div>
      <LandingNav />
      <div style={{ "text-align": "center", "margin-top": "20rem" }}>
        <img src={coin} alt="Logo" className="logo" />
        <p className="welcome">Welcome to the crypto bros</p>
        <Link to="/register" className="welcome">
          Register
        </Link>
      </div>
    </div>
  );
};

export default LandingPage;
