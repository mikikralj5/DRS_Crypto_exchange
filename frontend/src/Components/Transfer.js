import React from "react";

const Transfer = ({ currencySymbols }) => {
  return (
    <div>
      <div className="operation operation--transfer">
        <h2>Transfer</h2>
        <form className="form form--transfer">
          <input type="text" className="form__input form__input--to" />
          <input type="text" className="form__input form__input--to" />
          <select name="currency" className="form__input form__input--to">
            {currencySymbols.map((symbol, index) => (
              <option key={index}>{symbol}</option>
            ))}
          </select>
          <button className="form__btn form__btn--transfer">&rarr;</button>
          <label className="form__label">Transfer to</label>
          <label className="form__label">Amount</label>
          <label className="form__label">Currency</label>
        </form>
      </div>
    </div>
  );
};

export default Transfer;
