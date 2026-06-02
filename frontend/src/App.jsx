import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      console.log(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <h1>Choisir un fichier</h1>

      <input type="file" onChange={handleFileChange} />

      {file && <p>Fichier sélectionné: {file.name}</p>}

      <button onClick={uploadFile}>
        Envoyer
      </button>
    </div>
  );
}

export default App;