import React, { useEffect, useState } from "react";
import httpClient from "../httpClient";
import { useNavigate } from "react-router-dom";
import CryptoAllList from "./CryptoAllList";
import BankImport from "./BankImport";

const MainPage = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState();
  const [toShow, setToShow] = useState("all");
  const [currencyAll, setCurrencyAll] = useState([]);
  const [currencySymbols, setCurrencySymbols] = useState([]);
  const logOut = async () => {
    const resp = await httpClient.post("http://127.0.0.1:5000/logout");
    navigate("/");
  };

  useEffect(() => {
    const getUser = async () => {
      const resp = await httpClient.get("http://127.0.0.1:5000/@me");
      setUser(resp.data);
    };

    getUser();
  }, []);

  useEffect(() => {
    const getSymbol = async () => {
      const resp = await httpClient.get("http://127.0.0.1:5000/showCrypto");
      setCurrencySymbols(resp.data);
    };

    getSymbol();
  }, []);

  const showCurrencyAll = async () => {
    setToShow("all");
    const resp = await httpClient.get("http://127.0.0.1:5000/showCrypto_all");
    setCurrencyAll(resp.data);
  };

  return (
    <main className="app">
      <div className="balance">
        <div>
          <p className="balance__label">Current balance</p>
          <p className="balance__date">
            As of <span className="date">05/03/2037</span>
          </p>
        </div>
        <p className="balance__value">
          {user != null ? Math.round(user.crypto_account.amount) : 0}$
        </p>

        <button className="btn" onClick={logOut}>
          logout
        </button>
      </div>
      <div className="movements">
        {toShow === "all" ? <CryptoAllList cryptoList={currencyAll} /> : null}
      </div>
      <div className="summary">
        <button className="btn btn--show" onClick={showCurrencyAll}>
          Show currency states
        </button>
        <button className="btn btn--show">Show transactions</button>
        <button className="btn btn--show">Show crypto</button>
        <button className="btn btn--show">Show transaction requests</button>
      </div>
      <div className="operation operation--transfer">
        <h2>Transfer</h2>
        <form className="form form--transfer">
          <input type="text" className="form__input form__input--to" />
          <input type="text" className="form__input form__input--to" />
          <select name="currency" className="form__input form__input--to">
            {currencySymbols.map((symbol) => (
              <option>{symbol}</option>
            ))}
          </select>
          <button className="form__btn form__btn--transfer">&rarr;</button>
          <label className="form__label">Transfer to</label>
          <label className="form__label">Amount</label>
          <label className="form__label">Currency</label>
        </form>
      </div>
      <BankImport />
      <div className="operation operation--close">
        <h2>Currency change</h2>
        <form className="form form--close">
          <input type="text" className="form__input form__input--to" />
          <select
            name="currency"
            className="form__input form__input--to"
          ></select>
          <select
            name="currency"
            className="form__input form__input--to"
          ></select>
          <button className="form__btn form__btn--close">&rarr;</button>
          <label className="form__label">Amount</label>
          <label className="form__label">From</label>
          <label className="form__label">To</label>
        </form>
      </div>
    </main>
  );
};

export default MainPage;
