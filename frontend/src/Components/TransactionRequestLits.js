import React from "react";
import TransactionRequest from "./TransactionRequest";

const TransactionRequestLits = ({ userTransactionReqeusts, turnOnModal }) => {
  return (
    <div>
      {userTransactionReqeusts.map((transactionRequest, index) => (
        <TransactionRequest
          transactionRequest={transactionRequest}
          key={index}
          turnOnModal={turnOnModal}
        />
      ))}
    </div>
  );
};

export default TransactionRequestLits;
