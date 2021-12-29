import React, { useState } from "react";

const Transaction = ({ transaction, userEmail }) => {
  // const [transactionColor, setTransactionColor] = useState("");
  // const [transactionAmount, setTransactionAmount] = useState("");
  // if (transaction.state === "REJECTED") {
  //   setTransactionColor("withdrawal");
  //   setTransactionAmount("REJECTED");
  // } else if (transaction.state === "IN_PROGRESS") {
  //   setTransactionColor("progress");
  //   setTransactionAmount("MINING");
  // } else {
  //   setTransactionColor("deposit");
  //   setTransactionAmount(transaction.amount);
  // }
  return (
    <div>
      <div className="movements__row">
        {/* <div
          className={`movements__type movements__type--${
            transaction.state === "REJECTED" ? "withdrawal" : "deposit"
          }`}
        > */}
        <div
          className={`movements__type movements__type--${
            transaction.state === "IN_PROGRESS" ? "progress" : "deposit"
          }`}
        >
          {transaction.cryptocurrency}
        </div>

        <div className="movements__value">{transaction.amount}</div>
      </div>
    </div>
  );
};

export default Transaction;
