import LandingPage from "./Components/LandingPage";
import RegistrationForm from "./Components/RegistrationForm";
import MainPage from "./Components/MainPage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ModalWindow from "./Components/ModalWindow";
import Verification from "./Components/Verification";
import { useState } from "react";

function App() {
  const [showModal, setShowModal] = useState(false);
  const [modalTransaction, setModalTransaction] = useState(null);
  const turnOff = () => {
    setShowModal(false);
  };

  const turnOnModal = (transaction) => {
    setShowModal(true);
    setModalTransaction(transaction);
  };
  return (
    <Router>
      <div>
        {showModal ? (
          <ModalWindow turnOff={turnOff} modalTransaction={modalTransaction} />
        ) : null}
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route
            path="/mainPage"
            element={<MainPage turnOnModal={turnOnModal} />}
          />
          <Route path="/register" element={<RegistrationForm />} />
          <Route path="/verification" element={<Verification />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
