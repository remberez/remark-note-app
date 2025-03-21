import { RiStickyNoteAddLine } from "react-icons/ri";
import { FaFolderPlus } from "react-icons/fa";
import { FaSortAmountDownAlt } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import NoteService from "../services/noteService";

const SideBar = ({ setOpenNotes }) => {
    const [notes, setNotes] = useState([]);
    const [contextMenu, setContextMenu] = useState({ visible: false, x: 0, y: 0, noteId: null });
    const contextMenuRef = useRef(null);

    const handleContextMenu = (e, noteId) => {
        e.preventDefault();
        setContextMenu({
            visible: true,
            x: e.pageX,
            y: e.pageY,
            noteId: noteId,
        });
    };

    useEffect(() => {
        const fetchNotes = async () => {
            const notesData = await NoteService.fetchMyNotes();
            setNotes(notesData)
        }
        
        fetchNotes();
    }, [])

    function onNoteClick(e, title, id) {
        setOpenNotes(id, title);
    }

    async function addNote() {
        const response = await NoteService.createNote();
        if (response.status === 200) {
            setNotes([...notes, response.data])
        }
    }

    async function handleDelete(noteId) {
        const responseStatus = await NoteService.deleteNote(noteId);

        if (responseStatus === 204) {
            setNotes(notes.filter(value => value.id !== noteId))
        }
        setContextMenu(false);
    }

    useEffect(() => {
        const handleClickOutside = (e) => {
            if (contextMenuRef.current && !contextMenuRef.current.contains(e.target)) {
                setContextMenu({ visible: false, x: 0, y: 0 });
            }
        };
    
        document.addEventListener('click', handleClickOutside);
        return () => {
            document.removeEventListener('click', handleClickOutside);
        };
    }, []);

    return (
        <aside className="flex bg-lightGray overflow-hidden">
            <div className="w-[70px] border-r-2 border-veryLightGray">
                
            </div>
            <div className="border-r-2 border-veryLightGray w-full pl-4 pt-4">
                <div className="flex justify-start items-start gap-x-5">
                    <button onClick={addNote}>
                        <RiStickyNoteAddLine fill="white" size="20"/>
                    </button>
                    <button>
                        <FaFolderPlus fill="white" size="20"/>
                    </button>
                    <button>
                        <FaSortAmountDownAlt fill="white" size="20"/>         
                    </button>
                </div>
                <ul className="text-white flex flex-col mt-4 overflow-y-scroll styledScroll h-[92%]">
                    {
                        notes.map((value) => (
                            <li>
                                <NavLink
                                    to={`/workspace/note/${value.id}`}
                                    onClick={e => onNoteClick(e, value.title, value.id)}
                                    onContextMenu={e => handleContextMenu(e, value.id)}
                                    key={value.id}
                                    className={({ isActive }) => isActive ? 'bg-grayBgText px-2 py-2 rounded-lg w-full block' : 'px-2 py-2 w-full block'}
                                >
                                    { value.title }
                                </NavLink>
                                {contextMenu.visible && (
                                    <div
                                        style={{
                                            top: contextMenu.y,
                                            left: contextMenu.x,
                                            border: "1px solid #ccc",
                                            boxShadow: "0 2px 10px rgba(0, 0, 0, 0.1)",
                                        }}
                                        ref={contextMenuRef}
                                        className="absolute z-1000 bg-white"
                                    >
                                        <ul>
                                            <li
                                                style={{
                                                    padding: "8px 16px",
                                                    cursor: "pointer",
                                                    color: "red",
                                                }}
                                                onClick={() => handleDelete(contextMenu.noteId)}
                                            >
                                                Удалить
                                            </li>
                                        </ul>
                                    </div>
                                )}
                            </li>
                        ))
                    }
                </ul>
            </div>
        </aside>
    )
}

export default SideBar;