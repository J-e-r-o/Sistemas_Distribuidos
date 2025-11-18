// src/api.js
const API_BASE_URL = "http://localhost:8000"; // ajusta si es otro host/puerto

// 1) Obtener catálogo de productos
export async function fetchProductos() {
  const response = await fetch(`${API_BASE_URL}/api/v1/productos/`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("No se pudieron obtener los productos");
  }

  return response.json(); // devuelve array de productos
}

// 2) Crear un pedido (cuando quieras usarlo)
export async function crearPedido(detalles) {
  const response = await fetch(`${API_BASE_URL}/api/v1/pedidos/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ detalles }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.error || "No se pudo crear el pedido");
  }

  return response.json(); // devuelve el pedido creado con total_pedido y detalles
}
