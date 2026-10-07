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
            const response = await axios.post("http://localhost:8000/upload",
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
        catch(error){
            console.error(error);
            alert(
                error.response?.data?.detail || "Upload Failed...."
            );

        } finally{
            setLoading(false);
        }
    };
    const askQuestion = async (question)=>{
        try{
            setLoading(true)
            setAnswer("")
            setSources([])
            const response = await axios.post(
                "http://localhost:8000/ask",
                {
                    question
                }
            );
            setAnswer(response.data.answer);
            setSources(response.data.sources);

        }
        catch(error){
            alert{
                error.response?.data?.detail || "Something went wrong"
            };
        } finally{
            setLoading(false)
        }
    };
}
