import logo from "../assets/logo.png";
import { Link } from "react-router-dom";

const Header = () => {
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
                            <Link>Аккаунт</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </header>
    )
}

export default Header;