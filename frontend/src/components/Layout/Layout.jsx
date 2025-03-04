import { Outlet } from "react-router-dom";
import Header from "./Header"

const Layout = () => {
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
