import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const uploadFile = async () => {
    if (!file) return 
  

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setData(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1> Dashboard BIA</h1>

      <input type="file" onChange={handleFileChange} />

      {file && <p> Fichier sélectionné: {file.name}</p>}

      <button onClick={uploadFile}>
        Analyser
      </button>

      {/* TABLE */}
      {data.length > 0 && (
        <table
          border="1"
          cellPadding="10"
          style={{
            borderCollapse: "collapse",
            width: "100%"
          }}
        >
          <thead style={{ background: "#f2f2f2" }}>
            <tr>
              <th>Processus</th>
              <th>Département</th>
              <th>Criticité</th>
              <th>RTO</th>
              <th>RPO</th>
              <th>MTPD</th>
            </tr>
          </thead>

          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>{item.processus}</td>
                <td>{item.departement}</td>
                <td>{item.criticite}</td>
                <td>{item.RTO}</td>
                <td>{item.RPO}</td>
                <td>{item.MTPD}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;