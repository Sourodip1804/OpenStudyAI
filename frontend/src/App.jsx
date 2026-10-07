import { useState} from "react"
import axios from "axios"

import Navbar from "./components/Navbar";
import Upload from "./components/Uploadbox"
import Chatbox from "./components/Chatbox "
import Sidebar from "./components/Sidebar"

function App(){
    const [uploaded, setUploaded] = useState(false)
    const [filename, setFilename] = useState("")
    const [answer, setAnswer] = useState("")
    const [sources, setSources] = useState([])
    const [loading, setLoading] = useState(false)
    const [activeFeature, setActiveFeature] = useState("ask");

    // arrow function for uploadPDF
    const uploadPDF = async (file)=>{
        const formData = new FormData();
        formData.append("file", file);
        try{
            setLoading(true)
            const response = await axios.post("https://localhost:8000/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );
            setUploaded(true)
            setFilename(response.data.filename)
            alert("PDF uploaded successfully!")

        }
        catch(error)
    }
}
