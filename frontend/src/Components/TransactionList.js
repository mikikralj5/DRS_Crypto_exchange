import React from "react";
import Transaction from "./Transaction";

const TransactionList = ({ userTransactions }) => {
  return (
    <div>
      {userTransactions.map((transaction, index) => (
        <Transaction transaction={transaction} key={index} />
      ))}
    </div>
  );
};

export default TransactionList;
