import { Routes, Route } from "react-router-dom"
import MainPage from "./pages/MainPage.jsx"
import RegisterPage from "./pages/RegisterPage.jsx"

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<MainPage/>}/>
      <Route path="/auth" element={<RegisterPage/>}/>
    </Routes>
  )
}

export default App
