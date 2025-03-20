import { Link } from "react-router-dom";

const MainHeader = () => {
    return (
        <div className="bg-pageColor">
            <section className="bg-black pt-[140px] pb-[240px] rounded-b-[15%] shadow-xl">
                <div className="container text-white">
                    <h2 className="text-4xl mb-4">
                        Отточите своё мышление.
                    </h2>
                    <p className="text-xl text-grayText mb-[75px] max-w-[500px]">
                        Бесплатное и гибкое приложение для ваших личных мыслей.
                    </p>
                    <Link className="bg-green px-[70px] py-[10px] rounded-lg" to="/workspace">
                        Начать
                    </Link>
                </div>
            </section>
        </div>
    )
}

export default MainHeader;