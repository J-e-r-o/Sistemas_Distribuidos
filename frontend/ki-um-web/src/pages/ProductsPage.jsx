// src/pages/ProductsPage.jsx
import React, { useEffect, useState } from "react";
import { fetchPedidos } from "../api";

function ProductsPage({ onLogout }) {
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState("");

  useEffect(() => {
    const cargarProductos = async () => {
      try {
        const data = await fetchPedidos();
        setProductos(data);
      } catch (err) {
        setErrorMsg(err.message || "Error al cargar los productos");
      } finally {
        setLoading(false);
      }
    };

    cargarProductos();
  }, []);

  if (loading) {
    return <p>Cargando productos...</p>;
  }

  if (errorMsg) {
    return (
      <div>
        <p className="error">{errorMsg}</p>
        <button onClick={onLogout}>Volver al login</button>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="header-row">
        <h2>Listado de productos</h2>
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
              <th>Precio</th>
            </tr>
          </thead>
          <tbody>
            {productos.map((p) => (
              <tr key={p.id}>
                <td>{p.id}</td>
                <td>{p.nombre || p.nombre_producto}</td>
                <td>${p.precio}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ProductsPage;
