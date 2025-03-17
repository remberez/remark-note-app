import Devices from "../components/Devices";
import Footer from "../components/Footer";
import Header from "../components/Header";
import MainHeader from "../components/MainHeader";

const MainPage = () => {
    return (
        <div className="min-h-screen flex flex-col font-unbounded">
            <Header />
            <main className="flex-grow">
                <MainHeader/>
                <Devices/>
            </main>
            <Footer />
        </div>
    )
}

export default MainPage;