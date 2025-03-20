import { useEffect, useState } from "react";
import TabLine from "../components/TabLine";
import SideBar from "../components/WorkSpaceSideBar";
import { Outlet, useNavigate } from "react-router-dom";

const WorkSpacePage = () => {
    const [openNotes, setOpenNotes] = useState([]);
    const navigate = useNavigate();

    function pushOpenNotes(id, title) {
        const ids = openNotes.map(value => value.id);
        if (ids.includes(id)) {
            return
        }
        setOpenNotes([...openNotes, {id, title}]);
    }

    function removeOpenNotes(id) {
        setOpenNotes(openNotes.filter(note => note.id !== id));
        navigate(`/workspace/note/${openNotes.at(-2).id}`)
    }

    useEffect(() => {
        if (openNotes.length > 0) {
            navigate(`/workspace/note/${openNotes.at(-1).id}`);
        } else {
            navigate('/workspace');
        }
    }, [openNotes]);

    return (
        <div className="h-[100vh] bg-pageColor grid grid-cols-[1fr_5fr] grid-rows-[1fr_15fr] font-unbounded">
            <div></div>
            <TabLine notes={openNotes} removeNote={removeOpenNotes}/>
            <SideBar setOpenNotes={pushOpenNotes}/>
            <Outlet/>
        </div>
    );
};

export default WorkSpacePage;