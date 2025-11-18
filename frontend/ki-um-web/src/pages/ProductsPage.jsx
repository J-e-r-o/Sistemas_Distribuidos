// src/pages/ProductsPage.jsx
import React, { useEffect, useState } from "react";
import { fetchProductos } from "../api";

function ProductsPage({ onLogout, user }) {
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState("");

  useEffect(() => {
    const cargarProductos = async () => {
      try {
        const data = await fetchProductos();
        setProductos(data);
      } catch (err) {
        setErrorMsg(err.message || "Error al cargar los productos");
      } finally {
        setLoading(false);
      }
    };

    cargarProductos();
  }, []);

  if (loading) return <p>Cargando productos...</p>;

  if (errorMsg) {
    return (
      <div className="card">
        <p className="error">{errorMsg}</p>
        <button onClick={onLogout}>Volver al login</button>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="header-row">
        <div>
          <h2>Catálogo de productos</h2>
          {user && <p style={{ fontSize: 14 }}>Logueado como: <b>{user.username}</b></p>}
        </div>
        <button onClick={onLogout}>Cerrar sesión</button>
      </div>

      {productos.length === 0 ? (
        <p>No hay productos cargados.</p>
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Producto</th>
              <th>Descripción</th>
              <th>Precio</th>
              <th>Stock</th>
              <th>Disponible</th>
            </tr>
          </thead>
          <tbody>
            {productos.map((p) => (
              <tr key={p.id}>
                <td>{p.id}</td>
                <td>{p.nombre}</td>
                <td>{p.descripcion}</td>
                <td>${p.precio}</td>
                <td>{p.stock_actual}</td>
                <td>{p.esta_disponible ? "Sí" : "No"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ProductsPage;
