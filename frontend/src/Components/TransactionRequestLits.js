import React from "react";
import TransactionRequest from "./TransactionRequest";

const TransactionRequestLits = ({
  userTransactionReqeusts,
  turnOnModal,
  onRequestResolve,
  addTransactions,
  onAccept,
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
          showTransactions={onAccept}
        />
      ))}
    </div>
  );
};

export default TransactionRequestLits;
