export default class APIService {
  static async RegisterNewUser(body) {
    const resp = await fetch("http://localhost/registerUser", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const data = await resp.json();
    console.log(data);

    return data;
  }
}
