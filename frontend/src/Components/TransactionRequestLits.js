import React from "react";

const TransactionRequestLits = ({ transactionRequests, turnOnModal }) => {
  return (
    <div>
      {userTransactions.map((transactionRequest, index) => (
        <Transaction
          transactionRequest={transactionRequest}
          key={index}
          turnOnModal={turnOnModal}
        />
      ))}
    </div>
  );
};

export default TransactionRequestLits;
