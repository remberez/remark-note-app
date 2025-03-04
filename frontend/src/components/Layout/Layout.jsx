import { Outlet } from "react-router-dom";
import Header from "./Header"
import { useContext, useEffect } from "react";
import { AuthContext } from "../../App";

const Layout = () => {
    const authStore = useContext(AuthContext);
    useEffect(() => {
        authStore.checkAuth();
    }, []);

    return (
        <div className="font-heebo min-h-screen flex flex-col">
            <Header />
            <main className="bg-lightDarkBlue flex-1">
                <Outlet />
            </main>
        </div>
    )
}

export default Layout;
