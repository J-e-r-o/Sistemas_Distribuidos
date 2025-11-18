// src/api.js
const API_BASE_URL = "http://localhost:8000"; // Fix_Me: Cambiar URL si es necesario
t
export async function login(username, password) {
  const response = await fetch(`${API_BASE_URL}/login/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include", // para enviar cookies de sesión
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    let message = "Credenciales inválidas";
    try {
      const errorData = await response.json();
      if (errorData.detail) message = errorData.detail;
    } catch (_) {}
    throw new Error(message);
  }

  return true;
}

export async function fetchPedidos() {
  const response = await fetch(`${API_BASE_URL}/pedidos/`, {
    method: "GET",
    credentials: "include",
  });

  if (!response.ok) {
    throw new Error("No se pudieron obtener los pedidos");
  }

  return response.json(); // se espera un array
}
