import logo from "../assets/logo.png";

const Footer = () => {
    return (
        <footer className="bg-black text-white py-4">
            <div className="container text-lg flex items-center flex-col">
                <div className="flex justify-start gap-x-3 items-center mb-2">
                    <img
                        src={logo}
                        width={25}
                        height={14}
                    />
                    <div>
                        Remark
                    </div>
                </div>
                <div className="text-base text-grayText">
                    © 2025 Remark
                </div>
            </div>
        </footer>
    )
}

export default Footer;