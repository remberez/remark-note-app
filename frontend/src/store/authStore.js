import { makeAutoObservable } from "mobx";
import AuthService from "../services/AuthService";

class AuthStore {
    isAuth = false;
    user = {};

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

    async setUser() {
        const data = await AuthService.fetchMe();
        this.user = data;
    }
}

const authStore = new AuthStore();
export default authStore;