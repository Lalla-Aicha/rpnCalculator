import React, { useState } from 'react';
import axios from 'axios';

function Calculator() {
  const [expression, setExpression] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = () => {
    const expArray = expression.split(" ");  // Convertit l'entrée en tableau
    axios.post('http://localhost:8000/calculate/', expArray)
      .then(response => setResult(response.data.result))
      .catch(error => console.error(error));
  };

  // Fonction pour télécharger le fichier CSV
  const handleDownloadCSV = () => {
    // Redirige l'utilisateur vers l'URL du CSV
    window.location.href = 'http://localhost:8000/operations/csv/';
  };

  return (
    <div>
      <h1>Calculatrice NPI</h1>
      <input
        type="text"
        value={expression}
        onChange={e => setExpression(e.target.value)}
        placeholder="Entrez une expression NPI (ex : 3 4 +)"
      />
      <button onClick={handleSubmit}>Calculer</button>
      {result !== null && <h2>Résultat : {result}</h2>}

      {/* Ajouter un bouton pour télécharger le fichier CSV */}
      <button onClick={handleDownloadCSV}>Télécharger le fichier CSV</button>
    </div>
  );
}

export default Calculator;
