import { makeAutoObservable } from "mobx";

class AuthStore {
    isAuth = false;

    constructor() {
        makeAutoObservable(this);
    }

    setIsAuth(value) {
        this.isAuth = value;
    }

    setToken(token) {
        if (token) {
            localStorage.setItem("token", token);
            this.setIsAuth(true);
        } else {
            localStorage.removeItem("token");
        }
    }
}