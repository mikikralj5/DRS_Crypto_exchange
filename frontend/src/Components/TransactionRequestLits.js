import React from "react";
import TransactionRequest from "./TransactionRequest";

const TransactionRequestLits = ({
  userTransactionReqeusts,
  turnOnModal,
  onRequestResolve,
}) => {
  return (
    <div>
      {userTransactionReqeusts.map((transactionRequest, index) => (
        <TransactionRequest
          transactionRequest={transactionRequest}
          key={index}
          turnOnModal={turnOnModal}
          onRequestResolve={onRequestResolve}
        />
      ))}
    </div>
  );
};

export default TransactionRequestLits;
