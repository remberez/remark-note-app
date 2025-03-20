import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import NoteService from "../services/noteService";

const NoteTextField = () => {
    const {noteId} = useParams()
    const [textData, setTextData] = useState({});

    useEffect(() => {
        const fetchNote = async (noteId) => {
            const response = await NoteService.fetchDetailNote(noteId);
            console.log(response.text);
            setTextData(response);
        }
        fetchNote(noteId);
    }, [noteId])
    return (
        <section className="bg-black overflow-hidden">
            <textarea
                className="bg-black text-white p-2 resize-none outline-none h-full w-full px-60 pt-10"
                value={textData.text}
                onChange={e => setTextData({...textData, text: e.target.value})}
            />
        </section>
    )
}

export default NoteTextField;