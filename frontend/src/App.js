import RegistrationForm from "./Components/RegistrationForm";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        <Link to="/register">Register user</Link>
        <Routes>
          <Route path="/register" element={<RegistrationForm />}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
