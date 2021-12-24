import React, { useState, useEffect } from "react";
import LandingNav from "./LandingNav";
import logo from "../logo.png";
import coin from "../coin.png";
const LandingPage = () => {
  return (
    <div>
      <LandingNav />
      <div style={{ "text-align": "center", "margin-top": "20rem" }}>
        <img src={coin} alt="Logo" className="logo" />
        <p className="welcome">Welcome to the crypto bros</p>
      </div>
    </div>
  );
};

export default LandingPage;
