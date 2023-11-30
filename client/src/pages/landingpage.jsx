import React from "react";
import VidUpload from "../components/videoSubmit";

function Landingpage(){

    return(
        <div>
            <div className="main-form vert-flex">
                <div className="hori-flex">
                    <div className="mb-3 file-submit">
                        <VidUpload/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Landingpage;