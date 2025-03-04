import $api from "./api";

class UserService {
    static async fetchMe() {
        try {
            const token = localStorage.getItem("token");

            if (!token) {
                throw new Error("Токен не найден.");
            }

            const response = await $api.get("/users/me");
            return response.data;
        } catch (error) {
            console.error("Ошибка при запросе профиля", error);
        }
    } 
}

export default UserService;