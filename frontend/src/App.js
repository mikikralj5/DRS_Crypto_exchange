import LandingPage from "./Components/LandingPage";
import RegistrationForm from "./Components/RegistrationForm";
import LoginPage from "./Components/LoginPage";
import MainPage from "./Components/MainPage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/mainPage" element={<MainPage />} />
          <Route path="/register" element={<RegistrationForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
