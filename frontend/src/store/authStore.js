import { makeAutoObservable } from "mobx";
import AuthService from "../api/authService";
import UserService from "../api/userService";

class AuthStore {
    isAuth = false;
    user = {};

    constructor() {
        makeAutoObservable(this);
    }

    setIsAuth(value) {
        this.isAuth = value;
    }

    async login(username, password) {
        const response = await AuthService.login(username, password);
        localStorage.setItem("token", response.data.access_token);
        this.setIsAuth(true);
        this.setUser();
    }

    async setUser() {
        if (this.isAuth) {
            this.user = await UserService.fetchMe();
        }
    }

    async checkAuth() {
        if (localStorage.getItem("token")) {
            this.setIsAuth(true);
            this.setUser();
        }
    }
}

export default AuthStore;
