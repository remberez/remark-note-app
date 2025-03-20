import NoteTextField from "../components/NoteTextField";
import TabLine from "../components/TabLine";

const WorkSpacePage = () => {
    return (
        <div className="h-[100vh] bg-pageColor grid grid-cols-[1fr_5fr] grid-rows-[1fr_15fr] font-unbounded">
            <div className="border border-gray-500">1</div>
            <TabLine/>
            <div className="border border-gray-500">3</div>
            <NoteTextField/>
        </div>
    );
};

export default WorkSpacePage;