import React from "react";

const Transaction = ({ transaction }) => {
  return (
    <div>
      <div className="movements__row">
        <div className="movements__type movements__type--deposit">
          {transaction.sender}
        </div>
        <div className="movements__date">3 days ago</div>
        <div className="movements__value">{transaction.amount}</div>
      </div>
    </div>
  );
};

export default Transaction;
