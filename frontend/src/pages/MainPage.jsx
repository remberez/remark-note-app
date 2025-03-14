import Footer from "../components/Footer";
import Header from "../components/Header";

const MainPage = () => {
    return (
        <div className="min-h-screen flex flex-col">
            <Header />
            <main className="flex-grow">
                {/* Контент */}
            </main>
            <Footer />
        </div>
    )
}

export default MainPage;