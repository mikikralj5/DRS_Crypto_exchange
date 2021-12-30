import React from "react";

const TransactionRequest = ({ transactionRequest, turnOnModal }) => {
  return (
    <div>
      <div className="movements__row">
        <div className="movements__value">{transactionRequest.sender}</div>
        <div className="movements__type movements__type--deposit">
          {transactionRequest.amount} {transactionRequest.cryptocurrency}
        </div>
      </div>
    </div>
  );
};

export default TransactionRequest;
