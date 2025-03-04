import $api from "./api";

class AuthService {
    static async login(username, password) {
        try {
            const params = new FormData();
            params.append('grant_type', 'password');
            params.append('username', username);
            params.append('password', password);
    
            const response = await $api.post("/auth/login/", params, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            });
            
            return response;

        } catch (error) {
            console.error("Ошибка при входе: ", error);
        }
    }
}

export default AuthService;
