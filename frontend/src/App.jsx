import { Routes } from "react-router-dom"
import { Route } from "react-router-dom"
import Layout from "./components/Layout/Layout"
import AuthForm from "./components/auth/AuthForm"
import { createContext } from "react";
import AuthStore from "./store/authStore";

const authStore = new AuthStore();
export const AuthContext = createContext(authStore);

function App() {

  return (
    <AuthContext.Provider value={authStore}>
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route path="auth" element={<AuthForm/>}/>
        </Route>
      </Routes>
    </AuthContext.Provider>
  )
}

export default App
