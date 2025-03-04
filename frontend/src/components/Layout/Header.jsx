import { observer } from "mobx-react";
import { useContext } from "react";
import { AuthContext } from "../../App";

const Header = observer(() => {
    const authStore = useContext(AuthContext);

    return (
        <header className="bg-darkBlue">
            <div className="container flex justify-between py-6">
                <h2 className="text-white text-2xl ">
                    My Notes
                </h2>
                <div className="text-white text-xl">
                    {
                        authStore.isAuth ? 
                        authStore.user.email :
                        "NAVBAR"
                    }
                </div>
            </div>
        </header>
    )
})

export default Header;