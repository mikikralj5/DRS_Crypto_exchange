export default class APIService {
  static async RegisterNewUser(body) {
    const resp = await fetch("http://127.0.0.1:5000/registerUser", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
  }
}
