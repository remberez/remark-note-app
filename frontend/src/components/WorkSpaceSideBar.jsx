import { RiStickyNoteAddLine } from "react-icons/ri";
import { FaFolderPlus } from "react-icons/fa";
import { FaSortAmountDownAlt } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import NoteService from "../services/noteService";
import { MdFavorite } from "react-icons/md";

const SideBar = ({ setOpenNotes }) => {
    const [notes, setNotes] = useState([]);
    const [contextMenu, setContextMenu] = useState({ visible: false, x: 0, y: 0, noteId: null });
    const contextMenuRef = useRef(null);
    const [isOnlyFavorites, setIsOnlyFavorites] = useState(false);

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

    async function favoriteHandle(noteId) {
        await NoteService.addInFavorite(noteId);
        setContextMenu(false);
    }

    async function favoriteSwitchHandle(e) {
        e.preventDefault();
        if (!isOnlyFavorites) {
            const data = await NoteService.getFavoritesNotes();
            console.log(data);
            setNotes(data);
        } else {
            setNotes(await NoteService.fetchMyNotes());
        }
        setIsOnlyFavorites(!isOnlyFavorites);
    }

    return (
        <aside className="flex bg-lightGray overflow-hidden">
            <div className="w-[70px] border-r-2 border-veryLightGray">
                
            </div>
            <div className="border-r-2 border-veryLightGray w-full pl-4 pt-4">
                <div className="flex justify-start items-center gap-x-5">
                    <button onClick={addNote}>
                        <RiStickyNoteAddLine fill="white" size="20"/>
                    </button>
                    <button>
                        <FaFolderPlus fill="white" size="20"/>
                    </button>
                    <button>
                        <FaSortAmountDownAlt fill="white" size="20"/>         
                    </button>
                    <div className="relative group">
                        <button
                            onClick={favoriteSwitchHandle}
                            className={isOnlyFavorites ? "bg-blue-600 p-2 rounded-lg" : "p-2"}
                        >
                            <MdFavorite fill="white" size="22"/>
                        </button>
                        <div className="absolute hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded top-[100%] bg-black">
                            Избранные
                        </div>
                    </div>
                </div>
                <ul className="text-white flex flex-col mt-4 overflow-y-scroll styledScroll h-[92%] gap-y-2">
                    {
                        notes.map((value) => (
                            <li>
                                <NavLink
                                    to={`/workspace/note/${value.id}`}
                                    onClick={e => onNoteClick(e, value.title, value.id)}
                                    onContextMenu={e => handleContextMenu(e, value.id)}
                                    key={value.id}
                                    className={({ isActive }) => 
                                        isActive 
                                            ? 'bg-grayBgText px-2 py-2 rounded-lg w-full block hover:bg-gray-700' 
                                            : 'px-2 py-2 rounded-lg w-full block hover:bg-gray-700'
                                        }
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
                                        className="absolute z-1000 bg-white rounded-lg"
                                    >
                                        <ul className="flex flex-col gap-y-2 p-3">
                                            <li
                                                className="text-red-500"
                                            >
                                                <button onClick={() => handleDelete(contextMenu.noteId)}                                                >
                                                    Удалить
                                                </button>
                                            </li>
                                            <li className="text-black">
                                                <button onClick={() => favoriteHandle(contextMenu.noteId)}>
                                                    В избранное
                                                </button>
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