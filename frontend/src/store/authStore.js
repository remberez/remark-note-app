import { makeAutoObservable } from "mobx";
import AuthService from "../api/authService";

class AuthStore {
    isAuth = false;

    constructor() {
        makeAutoObservable(this);
    }

    async login(username, password) {
        const response = await AuthService.login(username, password);
        localStorage.setItem("token", response.data.access_token);
        this.isAuth = true;
    }
}

export default AuthStore;
