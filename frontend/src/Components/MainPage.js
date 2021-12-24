import React from "react";

const MainPage = () => {
  return (
    <main className="app">
      <div className="balance">
        <div>
          <p className="balance__label">Current balance</p>
          <p className="balance__date">
            As of <span className="date">05/03/2037</span>
          </p>
        </div>
        <p className="balance__value">0000€</p>
      </div>

      <div className="movements">
        <div className="movements__row">
          <div className="movements__type movements__type--deposit">
            2 deposit
          </div>
          <div className="movements__date">3 days ago</div>
          <div className="movements__value">4 000€</div>
        </div>
        <div className="movements__row">
          <div className="movements__type movements__type--withdrawal">
            1 withdrawal
          </div>
          <div className="movements__date">24/01/2037</div>
          <div className="movements__value">-378€</div>
        </div>
      </div>

      <div className="summary">
        <p className="summary__label">In</p>
        <p className="summary__value summary__value--in">0000€</p>
        <p className="summary__label">Out</p>
        <p className="summary__value summary__value--out">0000€</p>
        <p className="summary__label">Interest</p>
        <p className="summary__value summary__value--interest">0000€</p>
        <button className="btn--sort">&downarrow; SORT</button>
      </div>

      <div className="operation operation--transfer">
        <h2>Transfer money</h2>
        <form className="form form--transfer">
          <input type="text" className="form__input form__input--to" />
          <input type="number" className="form__input form__input--amount" />
          <button className="form__btn form__btn--transfer">&rarr;</button>
          <label className="form__label">Transfer to</label>
          <label className="form__label">Amount</label>
        </form>
      </div>

      <div className="operation operation--loan">
        <h2>Request loan</h2>
        <form className="form form--loan">
          <input
            type="number"
            className="form__input form__input--loan-amount"
          />
          <button className="form__btn form__btn--loan">&rarr;</button>
          <label className="form__label form__label--loan">Amount</label>
        </form>
      </div>

      <div className="operation operation--close">
        <h2>Close account</h2>
        <form className="form form--close">
          <input type="text" className="form__input form__input--user" />
          <input
            type="password"
            maxlength="6"
            className="form__input form__input--pin"
          />
          <button className="form__btn form__btn--close">&rarr;</button>
          <label className="form__label">Confirm user</label>
          <label className="form__label">Confirm PIN</label>
        </form>
      </div>
    </main>
  );
};

export default MainPage;
