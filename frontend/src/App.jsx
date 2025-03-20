import { Routes, Route } from "react-router-dom"
import MainPage from "./pages/MainPage.jsx"
import AuthPage from "./pages/AuthPage.jsx"
import { useEffect } from "react"
import authStore from "./store/authStore.js"

const App = () => {
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      authStore.setIsAuth(true);
      authStore.setUser();
    }
  }, [])
  
  return (
    <Routes>
      <Route path="/" element={<MainPage/>}/>
      <Route path="/auth" element={<AuthPage/>}/>
    </Routes>
  )
}

export default App
