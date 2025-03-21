import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import NoteService from "../services/noteService";

const NoteTextField = () => {
    const {noteId} = useParams()
    const [textData, setTextData] = useState({});

    useEffect(() => {
        const fetchNote = async (noteId) => {
            const response = await NoteService.fetchDetailNote(noteId);
            setTextData(response);
            setIsInitialized(true);
        }
        fetchNote(noteId);
    }, [noteId])

    useEffect(() => {
        const interval = setInterval(async () => {
                await NoteService.updateNote(textData, noteId);
        }, 350);

        return () => clearInterval(interval);
    }, [textData]);

    return (
        <section className="bg-black overflow-hidden">
            <input
                value={textData.title}
                onChange={e => setTextData({...textData, title: e.target.value})} 
                className="outline-none bg-black w-full px-60 pt-10 text-yellow text-2xl"
            />
            <textarea
                className="bg-black text-white p-2 resize-none outline-none h-full w-full px-60 pt-10"
                value={textData.text}
                onChange={e => setTextData({...textData, text: e.target.value})}
            />
        </section>
    )
}

export default NoteTextField;