import React from "react";
import TransactionRequest from "./TransactionRequest";

const TransactionRequestLits = ({
  userTransactionReqeusts,
  turnOnModal,
  onRequestResolve,
  addTransactions,
}) => {
  return (
    <div>
      {userTransactionReqeusts.map((transactionRequest, index) => (
        <TransactionRequest
          transactionRequest={transactionRequest}
          key={index}
          turnOnModal={turnOnModal}
          onRequestResolve={onRequestResolve}
          addTransactions={addTransactions}
        />
      ))}
    </div>
  );
};

export default TransactionRequestLits;
