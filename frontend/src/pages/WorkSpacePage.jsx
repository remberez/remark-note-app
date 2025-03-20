import { useState } from "react";
import NoteTextField from "../components/NoteTextField";
import TabLine from "../components/TabLine";
import SideBar from "../components/WorkSpaceSideBar";

const WorkSpacePage = () => {
    const [openNotes, setOpenNotes] = useState([]);

    function pushOpenNotes(id, title) {
        const ids = openNotes.map(value => value.id);
        if (ids.includes(id)) {
            return
        }
        setOpenNotes([...openNotes, {id, title}]);
    }

    function removeOpenNotes(id) {
        setOpenNotes(openNotes.filter(note => note.id !== id));
    }

    return (
        <div className="h-[100vh] bg-pageColor grid grid-cols-[1fr_5fr] grid-rows-[1fr_15fr] font-unbounded">
            <div></div>
            <TabLine notes={openNotes} removeNote={removeOpenNotes}/>
            <SideBar setOpenNotes={pushOpenNotes}/>
            <NoteTextField/>
        </div>
    );
};

export default WorkSpacePage;