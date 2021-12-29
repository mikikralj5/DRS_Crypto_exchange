import React from "react";
import Transaction from "./Transaction";

const TransactionList = ({ userTransactions, userEmail }) => {
  return (
    <div>
      {userTransactions.map((transaction, index) => (
        <Transaction
          transaction={transaction}
          key={index}
          userEmail={userEmail}
        />
      ))}
    </div>
  );
};

export default TransactionList;
