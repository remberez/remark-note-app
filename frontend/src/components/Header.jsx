import logo from "../assets/logo.png";
import { Link } from "react-router-dom";
import authStore from "../store/authStore";
import { observer } from "mobx-react-lite";

const Header = observer(() => {
    return (
        <header className="bg-black font-unbounded">
            <nav className="container flex justify-between text-white py-6 items-center">
                <div className="flex items-center gap-x-2">
                    <img
                        src={logo}
                        width={37}
                        height={29}
                    />
                    <div className="text-2xl">
                        Remark
                    </div>
                </div>
                <div>
                    <ul className="flex gap-x-6 text-grayText text-sm">
                        <li>
                            <Link>Сообщество</Link>
                        </li>
                        <li>
                            {
                                authStore.isAuth ? 
                                <Link>{authStore.user?.email?.split("@")[0]}</Link> :
                                <Link to={"/auth"}>Аккаунт</Link>
                            }
                        </li>
                    </ul>
                </div>
            </nav>
        </header>
    )
})

export default Header;