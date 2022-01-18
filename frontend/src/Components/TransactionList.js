import React from "react";
import Transaction from "./Transaction";
import SortTransactionRow from "./SortTransactionRow";

const TransactionList = ({
  userTransactions,
  userEmail,
  turnOnModal,
  updateTransactions,
}) => {
  return (
    <div>
      <SortTransactionRow updateTransactions={updateTransactions} />
      {userTransactions.map((transaction, index) => (
        <Transaction
          transaction={transaction}
          key={index}
          userEmail={userEmail}
          turnOnModal={turnOnModal}
        />
      ))}
    </div>
  );
};

export default TransactionList;
