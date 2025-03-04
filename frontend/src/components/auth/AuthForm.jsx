import { useState } from "react";
import AuthService from "../../api/authService";

const AuthForm = () => {
    async function onSubmit(e) {
        e.preventDefault();
        await AuthService.login(username, password);
    }

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    return (
        <section className="w-max container mt-20 bg-white px-5 py-3">
            <h2 className="text-center text-xl mb-4 font-bold">
                Авторизация
            </h2>
            <form onSubmit={onSubmit} method="post">
                <div className="mb-4 flex gap-x-2">
                    <label htmlFor="username">
                        Логин
                    </label>
                    <input type="text" name="username" id="username" value={username} onChange={e => setUsername(e.target.value)}/>
                </div>
                <div className="mb-4 flex gap-x-2">
                    <label htmlFor="password">
                        Пароль
                    </label>
                    <input type="password" name="password" id="password" value={password} onChange={e => setPassword(e.target.value)}/>
                </div>
                <button type="submit" className="bg-lightDarkBlue text-white px-5 py-2 block w-full">
                    Войти
                </button>
            </form>
        </section>
    )
}

export default AuthForm;