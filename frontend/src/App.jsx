import { Routes, Route } from "react-router-dom"
import MainPage from "./pages/MainPage.jsx"
import AuthPage from "./pages/AuthPage.jsx"

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<MainPage/>}/>
      <Route path="/auth" element={<AuthPage/>}/>
    </Routes>
  )
}

export default App
