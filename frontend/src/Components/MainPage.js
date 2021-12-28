import React, { useEffect, useState } from "react";
import httpClient from "../httpClient";
import { useNavigate } from "react-router-dom";
import CryptoAllList from "./CryptoAllList";
import BankImport from "./BankImport";
import CurrencyExchange from "./CurrencyExchange";
import Transfer from "./Transfer";
import UserCryptoList from "./UserCryptoList";

const MainPage = () => {
  const navigate = useNavigate();
  const [userMoney, setUserMoney] = useState(0);
  const [toShow, setToShow] = useState("all");
  const [currencyAll, setCurrencyAll] = useState([]);
  const [currencySymbols, setCurrencySymbols] = useState([]);
  const [currencySymbolsUsd, setCurrencySymbolsUsd] = useState([]);
  const [userCryptoList, setUserCryptoList] = useState([]);

  const today = new Date();
  const date =
    today.getDay() + "/" + today.getMonth() + "/" + today.getFullYear();

  const logOut = async () => {
    const resp = await httpClient.post("http://127.0.0.1:5000/logout");
    navigate("/");
  };

  // useEffect(() => {
  //   const getUser = async () => {
  //     const resp = await httpClient.get("http://127.0.0.1:5000/@me");
  //   };

  //   getUser();
  // }, []);

  useEffect(() => {
    const getUserMoney = async () => {
      const resp = await httpClient("http://127.0.0.1:5000/getMoney");

      setUserMoney(resp.data.value);
    };

    getUserMoney();
  }, [userMoney]);

  useEffect(() => {
    const getSymbol = async () => {
      const resp = await httpClient.get(
        "http://127.0.0.1:5000/showCryptoSymbols"
      );

      const data = ["USD", ...resp.data];
      setCurrencySymbols(resp.data);
      setCurrencySymbolsUsd(data);
    };

    getSymbol();
  }, []);

  const showUserCrypto = async () => {
    setToShow("userCrypto");
    const resp = await httpClient.get("http://127.0.0.1:5000/getCrypto");
    setUserCryptoList(resp.data);
  };

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
            As of <span className="date">{date}</span>
          </p>
        </div>
        <p className="balance__value">{Math.round(userMoney)}$</p>

        <button className="btn" onClick={logOut}>
          logout
        </button>
      </div>
      <div className="movements">
        {toShow === "all" ? <CryptoAllList cryptoList={currencyAll} /> : null}
        {toShow === "userCrypto" ? (
          <UserCryptoList
            userCryptoList={userCryptoList}
            currencyAll={currencyAll}
          />
        ) : null}
      </div>
      <div className="summary">
        <button className="btn btn--show" onClick={showCurrencyAll}>
          Show currency states
        </button>
        <button className="btn btn--show">Show transactions</button>
        <button className="btn btn--show" onClick={showUserCrypto}>
          Show crypto
        </button>
        <button className="btn btn--show">Show transaction requests</button>
      </div>
      <Transfer currencySymbols={currencySymbols} />
      <BankImport userMoney={userMoney} setUserMoney={setUserMoney} />
      <CurrencyExchange currencySymbolsUsd={currencySymbolsUsd} />
    </main>
  );
};

export default MainPage;
