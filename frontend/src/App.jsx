import { Routes, Route } from "react-router-dom"
import MainPage from "./pages/MainPage.jsx"
import AuthPage from "./pages/AuthPage.jsx"
import { useEffect } from "react"
import authStore from "./store/authStore.js"
import WorkSpacePage from "./pages/WorkSpacePage.jsx"
import NoteTextField from "./components/NoteTextField.jsx"

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
      <Route path="/workspace" element={<WorkSpacePage />}>
        <Route path="note/:noteId" element={<NoteTextField />} />
    </Route>
    </Routes>
  )
}

export default App
