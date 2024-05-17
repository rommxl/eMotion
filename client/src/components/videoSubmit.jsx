import React from "react";
import axios from "axios";
import { useState } from "react";
import Result from "./result";

function VidUpload(){
    const base = process.env.REACT_APP_server_link;
    const [video, videoChange] = useState(null);
    const [result,setResult] = useState({});

    function setVideo(event){
        videoChange(event.target.files[0])    //assigning media to a variable
    }


    function uploadVideo(event){
        

        const formData = new FormData();
        formData.append("tobeanalyzed",video);   //send media using formdata

        axios
        .post(`${base}/upload`,formData)
        .then((res) => {
            setResult(res.data)
            console.log(result);
        })
        event.preventDefault();
    }

    return (
        <div>
            <form onSubmit={uploadVideo}  method="post" encType="multipart/form-data">
                <input className="form-control" type="file" name="tobeanalyzed" onChange={setVideo}/>
                <div className="submit-button-container">
                    <div className="btn-group btn-group-lg submit" role="group">
                        <button type="submit" className="btn btn-primary">Upload</button>
                    </div>
                </div>
            </form>
            <Result/>
        </div>
    )
}

export default VidUpload;