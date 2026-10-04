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
}
