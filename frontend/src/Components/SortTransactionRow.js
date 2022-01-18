import React from "react";
import httpClient from "../httpClient";

const SortTransactionRow = ({ updateTransactions }) => {
  const sortTransactions = async (sortType) => {
    const resp = await httpClient.patch(
      "http://127.0.0.1:5000/sortTransactions",
      { sort_by: "amount", sort_type: sortType }
    );

    console.log(resp.data);
    updateTransactions(resp.data);
  };
  return (
    <div>
      <div className="movements__row">
        <div className="movements__sort">SORT</div>
        <div
          className="movements__value__sort"
          onClick={() => sortTransactions("Asc")}
        >
          &uarr;
        </div>
        <div
          className="movements__value__sort"
          onClick={() => sortTransactions("Dsc")}
        >
          &darr;
        </div>
      </div>
    </div>
  );
};

export default SortTransactionRow;
