import { Routes } from "react-router-dom"
import { Route } from "react-router-dom"
import Layout from "./components/Layout/Layout"
import AuthForm from "./components/auth/AuthForm"

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout/>}>
        <Route path="auth" element={<AuthForm/>}/>
      </Route>
    </Routes>
  )
}

export default App
