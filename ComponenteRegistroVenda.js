// frontend/src/components/SaleForm.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const SaleForm = () => {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState('');
  const [quantity, setQuantity] = useState(1);

  useEffect(() => {
    api.get('products/')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar produtos:', error);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('sales/', {
      product: { id: selectedProduct },
      quantity: quantity,
    })
      .then(response => {
        alert('Venda registrada com sucesso!');
      })
      .catch(error => {
        console.error('Erro ao registrar venda:', error);
      });
  };

  return (
    <div>
      <h2>Registrar Venda</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Produto:</label>
          <select value={selectedProduct} onChange={(e) => setSelectedProduct(e.target.value)} required>
            <option value="">Selecione um produto</option>
            {products.map(product => (
              <option key={product.id} value={product.id}>
                {product.name} (Estoque: {product.quantity_in_stock})
              </option>
            ))}
          </select>
        </div>
        <div>
          <label>Quantidade:</label>
          <input
            type="number"
            value={quantity}
            min="1"
            onChange={(e) => setQuantity(e.target.value)}
            required
          />
        </div>
        <button type="submit">Registrar Venda</button>
      </form>
    </div>
  );
};

export default SaleForm;
