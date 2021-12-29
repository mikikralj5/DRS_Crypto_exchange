import React, { useEffect, useState } from "react";
import httpClient from "../httpClient";
import { useNavigate } from "react-router-dom";
import CryptoAllList from "./CryptoAllList";
import BankImport from "./BankImport";
import CurrencyExchange from "./CurrencyExchange";
import Transfer from "./Transfer";
import UserCryptoList from "./UserCryptoList";
import TransactionList from "./TransactionList";

const MainPage = ({ turnOnModal }) => {
  const navigate = useNavigate();
  const [toShow, setToShow] = useState("all");
  const [currencySymbols, setCurrencySymbols] = useState([]);
  const [currencySymbolsUsd, setCurrencySymbolsUsd] = useState([]);

  const [currencyAll, setCurrencyAll] = useState([]);
  const [userCryptoList, setUserCryptoList] = useState([]);
  const [userTransactions, setUserTransactions] = useState([]);
  const [userEmail, setUserEmail] = useState("");

  //dependencies
  const [amountToBuy, setAmountToBuy] = useState(0); //za exchange
  const [transferAmount, setTransferAmount] = useState(0);
  const [userMoney, setUserMoney] = useState(0);

  const today = new Date();
  const date =
    today.getDate() + "/" + (today.getMonth() + 1) + "/" + today.getFullYear();

  const logOut = async () => {
    const resp = await httpClient.post("http://127.0.0.1:5000/logout");
    navigate("/");
  };

  useEffect(() => {
    const getUserMoney = async () => {
      const resp = await httpClient("http://127.0.0.1:5000/getMoney");

      setUserMoney(resp.data.value);
    };

    getUserMoney();
  }, [userMoney]);

  useEffect(() => {
    const getUserCrypto = async () => {
      const resp = await httpClient.get("http://127.0.0.1:5000/getCrypto");
      setUserCryptoList(resp.data);
    };

    getUserCrypto();
  }, [amountToBuy]);

  useEffect(() => {
    const getUserTransactions = async () => {
      const resp = await httpClient.get(
        "http://127.0.0.1:5000/getTransactions"
      );
      setUserTransactions(resp.data);
    };

    getUserTransactions();
  }, [transferAmount]);

  useEffect(() => {
    const getUserEmail = async () => {
      const resp = await httpClient.get("http://127.0.0.1:5000/@me");
      setUserEmail(resp.data);
    };

    getUserEmail();
  }, [userTransactions]);

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

  useEffect(() => {
    const getCurrencyAll = async () => {
      const resp = await httpClient.get("http://127.0.0.1:5000/showCrypto_all");
      setCurrencyAll(resp.data);
    };

    getCurrencyAll();
  }, []);

  const showUserCrypto = () => {
    setToShow("userCrypto");
  };

  const showCurrencyAll = () => {
    setToShow("all");
  };

  const showTransactions = () => {
    setToShow("transactions");
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
        {toShow === "transactions" ? (
          <TransactionList
            userTransactions={userTransactions}
            userEmail={userEmail}
            turnOnModal={turnOnModal}
          />
        ) : null}
      </div>
      <div className="summary">
        <button className="btn btn--show" onClick={showCurrencyAll}>
          Show currency states
        </button>
        <button className="btn btn--show" onClick={showTransactions}>
          Show transactions
        </button>
        <button className="btn btn--show" onClick={showUserCrypto}>
          Show crypto
        </button>
        <button className="btn btn--show">Show transaction requests</button>
      </div>

      <Transfer
        currencySymbols={currencySymbols}
        transferAmount={transferAmount}
        setTransferAmount={setTransferAmount}
      />
      <BankImport userMoney={userMoney} setUserMoney={setUserMoney} />
      <CurrencyExchange
        currencySymbolsUsd={currencySymbolsUsd}
        amountToBuy={amountToBuy}
        setAmountToBuy={setAmountToBuy}
      />
    </main>
  );
};

export default MainPage;
