import React from "react";

const TransactionRequest = ({ transactionRequest, turnOnModal }) => {
  return (
    <div>
      <div className="movements__row">
        <div className="movements__type movements__type--pending">
          {transactionRequest.amount} {transactionRequest.cryptocurrency}
        </div>
        <div className="movements__value">
          <label style={{ color: "green", cursor: "pointer" }}>ACCEPT</label>
        </div>
        <div className="movements__value">
          <label style={{ color: "red", cursor: "pointer" }}>DECLINE</label>
        </div>
      </div>
    </div>
  );
};

export default TransactionRequest;
