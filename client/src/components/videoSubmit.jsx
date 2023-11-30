import React from "react";
import axios from "axios";
import { useState } from "react";

function VidUpload(){
    const base = process.env.REACT_APP_server_link;
    const [video, videoChange] = useState(null);

    function setVideo(event){
        videoChange(event.target.files[0])
    }


    async function uploadVideo(event){
        

        const formData = new FormData();
        formData.append("tobeanalyzed",video);

        axios
        .post(`${base}/upload`,formData)
        .then((res) => {
            console.log(res.data);
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
        </div>
    )
}

export default VidUpload;