import React, { useState } from "react";

const Transaction = ({ transaction, userEmail, turnOnModal }) => {
  let transactionAmount;
  let transactionColor;
  if (transaction.state === "REJECTED") {
    transactionColor = "withdrawal";
    transactionAmount = "REJECTED";
  } else if (transaction.state === "IN_PROGRESS") {
    transactionColor = "progress";
    transactionAmount = transaction.amount;
  } else {
    transactionColor = "deposit";
    transactionAmount = transaction.amount;
  }

  const transactionDetails = () => {
    console.log("clicked");
  };
  return (
    <div>
      <div
        className="movements__row"
        onClick={() => turnOnModal(transaction)}
        style={{ cursor: "pointer" }}
      >
        <div className={`movements__type movements__type--${transactionColor}`}>
          {transaction.cryptocurrency}
        </div>

        <div className="movements__value">{transactionAmount}</div>
      </div>
    </div>
  );
};

export default Transaction;
