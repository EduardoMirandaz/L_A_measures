import { OrcamentoGradesPage } from "./pages/OrcamentoGradesPage.tsx";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";


function App() {

  return(
    <Router>
        <Routes>
            <Route path="/orcamentos/grades" element={<OrcamentoGradesPage/>}/>
        </Routes>
    </Router>
);
}

export default App
