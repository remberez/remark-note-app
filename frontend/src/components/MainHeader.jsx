const MainHeader = () => {
    return (
        <div className="bg-pageColor">
            <section className="bg-black pt-[140px] pb-[240px] rounded-b-[15%] shadow-xl">
                <div className="container text-white">
                    <h2 className="text-4xl">
                        Отточите своё мышление.
                    </h2>
                    <p className="text-xl text-grayText mb-[75px]">
                        Бесплатное и гибкое приложение для ваших личных мыслей.
                    </p>
                    <button className="bg-green px-[70px] py-[10px] rounded-lg">
                        Начать
                    </button>
                </div>
            </section>
        </div>
    )
}

export default MainHeader;