import { Link } from "react-router-dom";
import appLogo from "../assets/app-logo.png";

const DescriptionItem = ({ title, description }) => {
    return (
        <div className="border-b border-gray-500 pb-6">
            <h3 className="text-white text-2xl mb-2">
                {title}
            </h3>
            <p className="text-grayText text-lg">
                {description}
            </p>
        </div>
    );
};

const AppDescription = () => {
    return (
        <section className="bg-pageColor">
            <div className="container flex items-start justify-between px-20 gap-x-16 pb-20">
                <ul className="flex flex-col gap-y-4">
                    <li>
                        <DescriptionItem
                            title={"Ваши мысли принадлежат вам."}
                            description={"Remark хранит заметки в частном порядке на вашем устройстве, чтобы вы могли быстро получить к ним доступ даже в автономном режиме. Никто другой не сможет их прочитать, даже мы."}
                        />
                    </li>
                    <li>
                        <DescriptionItem
                            title={"Ваш разум уникален."}
                            description={"Благодаря тысячам плагинов и тем, вы можете придать Remark форму, соответствующую вашему образу мышления."}
                        />
                    </li>
                    <li>
                        <DescriptionItem
                            title={"Ваши знания должны сохраниться."}
                            description={"Remark использует открытые форматы файлов, поэтому вы никогда не будете привязаны к ним. Вы владеете своими данными в долгосрочной перспективе."}
                        />
                    </li>
                </ul>
                <div className="flex flex-col items-center">
                    <img
                        src={appLogo}
                        width={1000}
                        height={1000}
                        className="mb-6"
                    />
                    <div className="text-4xl text-white mb-4">
                        Remark
                    </div>
                    <div className="text-center text-lg text-grayText">
                        Бессплатно, без лимитов.
                    </div>
                    <Link className="text-green underline">
                        Начать сейчас.
                    </Link>
                </div>
            </div>
        </section>
    )
}

export default AppDescription;