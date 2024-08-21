// frontend/src/components/SalesReport.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const SalesReport = () => {
  const [report, setReport] = useState({ total_sales: 0, total_revenue: 0 });

  useEffect(() => {
    api.get('reports/sales_report/')
      .then(response => {
        setReport(response.data);
      })
      .catch(error => {
        console.error('Erro ao obter relatório de vendas:', error);
      });
  }, []);

  return (
    <div>
      <h2>Relatório de Vendas</h2>
      <p>Total de Vendas: {report.total_sales}</p>
      <p>Receita Total: R$ {report.total_revenue}</p>
    </div>
  );
};

export default SalesReport;
