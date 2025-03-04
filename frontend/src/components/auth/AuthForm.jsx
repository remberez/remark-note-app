import { useContext, useState } from "react";
import { AuthContext } from "../../App";
import Button from '@mui/material/Button';
import { TextField } from "@mui/material";

const AuthForm = () => {
    const authStore = useContext(AuthContext);

    async function onSubmit(e) {
        e.preventDefault();
        await authStore.login(username, password);
    }

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    return (
        <section className="w-max container mt-20 bg-white px-12 py-7 rounded">
            <h2 className="text-center text-xl mb-4 font-bold">
                Авторизация
            </h2>
            <form onSubmit={onSubmit} method="post">
                <div className="flex flex-col gap-y-4">
                    <TextField 
                        id="username" 
                        label="Логин" 
                        variant="outlined" 
                        value={username}
                        onChange={e => setUsername(e.target.value)}
                        size="small"
                    />
                    <TextField 
                        id="password" 
                        label="Пароль" 
                        variant="outlined" 
                        value={password} 
                        onChange={e => setPassword(e.target.value)}
                        size="small"
                        type="password"
                    />
                    <Button variant="contained" type="submit">
                        Войти
                    </Button>
                </div>
            </form>
        </section>
    )
}

export default AuthForm;