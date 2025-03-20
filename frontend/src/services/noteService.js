import { api } from ".";

class NoteService {
    static async fetchMyNotes() {
        try {
            const response = await api.get("/notes/my");
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }

    static async fetchDetailNote(noteId) {
        try {
            const response = await api.get(`/notes/${noteId}`);
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }
}

export default NoteService;