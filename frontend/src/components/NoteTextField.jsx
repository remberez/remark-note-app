import { useParams } from "react-router-dom";

const NoteTextField = () => {
    const {noteId} = useParams()

    return (
        <section className="bg-black overflow-hidden">
            <textarea
                className="bg-black text-white p-2 resize-none outline-none h-full w-full px-60 pt-10"
            />
        </section>
    )
}

export default NoteTextField;