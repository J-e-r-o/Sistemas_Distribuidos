// src/pages/LoginPage.jsx
import React, { useState } from "react";
import { USERS } from "../users";

function LoginPage({ onLoginSuccess }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    setErrorMsg("");

    // Buscar usuario en el archivo USERS
    const foundUser = USERS.find(
      (u) => u.username === username && u.password === password
    );

    if (foundUser) {
      onLoginSuccess(foundUser); // pasamos el usuario entero si querés usar el rol después
    } else {
      setErrorMsg("Usuario o contraseña incorrectos");
    }
  };

  return (
    <div className="card">
      <h2>Iniciar sesión</h2>
      <form onSubmit={handleSubmit} className="form">
        <label>
          Usuario
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>

        <label>
          Contraseña
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>

        {errorMsg && <p className="error">{errorMsg}</p>}

        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
}

export default LoginPage;
