import React from "react";
import CryptoAll from "./CryptoAll";

const CryptoAllList = ({ cryptoList }) => {
  return (
    <div>
      {cryptoList.map((currency) => (
        <CryptoAll currency={currency} />
      ))}
    </div>
  );
};

export default CryptoAllList;
