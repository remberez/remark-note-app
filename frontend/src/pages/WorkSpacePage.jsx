import NoteTextField from "../components/NoteTextField";
import TabLine from "../components/TabLine";
import SideBar from "../components/WorkSpaceSideBar";

const WorkSpacePage = () => {
    return (
        <div className="h-[100vh] bg-pageColor grid grid-cols-[1fr_5fr] grid-rows-[1fr_15fr] font-unbounded">
            <div></div>
            <TabLine/>
            <SideBar/>
            <NoteTextField/>
        </div>
    );
};

export default WorkSpacePage;