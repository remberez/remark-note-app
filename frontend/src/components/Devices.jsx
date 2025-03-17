import laptop from "../assets/laptop.png";
import phone from "../assets/iphone.png";

const Devices = () => {
    return (
        <section className="bg-pageColor h-[650px]">
            <div className="container relative">
                <div className="absolute top-[-180px] left-[-130px]">
                    <img
                        src={laptop}
                        width={1251}
                        height={719}
                    />
                    <img
                        src={phone}
                        width={398}
                        height={720}
                        className="absolute top-[80px] right-[-100px]"
                    />
                </div>
            </div>
        </section>
    )
}

export default Devices;