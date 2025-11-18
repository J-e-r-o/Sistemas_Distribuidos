// src/App.jsx
import React, { useState } from "react";
import LoginPage from "./pages/LoginPage.jsx";
import ProductsPage from "./pages/ProductsPage.jsx";

function App() {
  const [currentUser, setCurrentUser] = useState(null);

  const handleLoginSuccess = (user) => {
    setCurrentUser(user);
  };

  const handleLogout = () => {
    setCurrentUser(null);
  };

  return (
    <div className="app-container">
      <h1>Ki-UM</h1>
      {!currentUser ? (
        <LoginPage onLoginSuccess={handleLoginSuccess} />
      ) : (
        <ProductsPage user={currentUser} onLogout={handleLogout} />
      )}
    </div>
  );
}

export default App;
